#!/usr/bin/python

import sys
import os
from os.path import join as _opj
from glob import glob
from tempfile import mkdtemp
import subprocess
import shutil
import numpy as np
import nibabel as nb
from mvpa2.base.hdf5 import h5load, h5save
from mvpa2.datasets.mri import map2nifti, fmri_dataset

# +1 to be compatible with condor submission
subj = int(sys.argv[1]) + 1

res_dir = 'grp_results'
if not os.path.exists(res_dir):
    os.makedirs(res_dir)

# because the stored SL results have no proper imghdr
subjtmpl = nb.load('BASEDIR/sub%.3i/templates/bold7Tp1/head.nii.gz' % subj)

# orig results
ds = h5load(_opj('results', 'sub%.3i_2.0mm_hrf_sl_orig.hdf5' % subj))
# load permutations and merge with orig results
data = np.vstack(
    [ds.samples[0]] +
    [np.load(fname)
     for fname in sorted(
         glob(_opj('results', 'sub%.3i_2.0mm_hrf_sl_perm*.npy' % subj)))])
#data = ds.samples

# write out as NIfTI
tdir = mkdtemp()
print tdir
orig_fname = _opj(tdir, 'data_in_orig.nii.gz')
group_fname = _opj(tdir, 'data_in_group.nii.gz')
nb.save(map2nifti(ds, data, imghdr=subjtmpl.get_header()), orig_fname)

# project into group space
ref_fname = "BASEDIR/templates/grpbold7Tp1/brain.nii.gz"
warp_fname = "BASEDIR/sub%.3i/templates/bold7Tp1/in_grpbold7Tp1/subj2tmpl_warp.nii.gz" % subj
subprocess.check_call(
    ["applywarp",
     "--in=%s" % orig_fname,
     "--out=%s" % group_fname,
     "--ref=%s" % ref_fname,
     "--warp=%s" % warp_fname])

# and back into a dataset
# group intersection brain mask
mask_fname = 'BASEDIR/templates/grpbold7Tp1/qa/subjbold7Tp1_to_grpbold7Tp1/brain_mask_intersection.nii.gz'
ds = fmri_dataset(group_fname, mask=mask_fname)
h5save(_opj(res_dir, 'grpspace_sub%.3i.hdf5' % subj), ds, compression=9)

# cleanup
shutil.rmtree(tdir)
