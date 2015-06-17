#!/usr/bin/python

import time
from os.path import join as _opj
import numpy as np
import nibabel as nb
from mvpa2.base.hdf5 import h5load, h5save
from mvpa2.datasets import Dataset
from mvpa2.datasets.mri import map2nifti
from mvpa2.algorithms.group_clusterthr import GroupClusterThreshold

orig = []
perms = []
perm_count = []

subj_ids = range(1, 21)

# load all subjs
print 'Loading subjs', time.asctime()
for subj in subj_ids:
    print 'Loading subj %i' % subj
    sds = h5load(_opj('grp_results', 'grpspace_sub%.3i.hdf5' % subj))
    orig.append(sds.samples[0])
    perms.append(sds.samples[1:])
    perm_count.append(len(sds) - 1)

print 'Merge data', time.asctime()
orig_ds = Dataset(orig, sa=dict(subj=subj_ids), fa=sds.fa, a=sds.a)
perm_ds = Dataset(np.vstack(perms),
                  sa=dict(subj=np.repeat(subj_ids, perm_count)),
                  fa=sds.fa,
                  a=sds.a)
# some magic to drop the memory demand
del orig
del perms

print 'Train thresholder', time.asctime()
thr = GroupClusterThreshold(
    n_bootstrap=10000, chunk_attr='subj', n_blocks=100,
    feature_thresh_prob=0.001, n_proc=1, fwe_rate=0.05)
thr.train(perm_ds)

print 'Treshold', time.asctime()
res = thr(orig_ds)
h5save('grpavg_stats.hdf5', res, compression=9)

print 'Store results', time.asctime()
nb.save(map2nifti(res, res.samples), 'avg_acc.nii.gz')
nb.save(map2nifti(res, res.fa.clusters_fwe_thresh), 'fwecorrected_clusters.nii.gz')
nb.save(map2nifti(res, res.fa.featurewise_thresh), 'featurewise_thresh.nii.gz')
