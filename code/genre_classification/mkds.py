#!/usr/bin/python

import sys
from os.path import join as _opj

from mvpa2.datasets.sources.openfmri import OpenFMRIDataset
from mvpa2.datasets.eventrelated import fit_event_hrf_model
from mvpa2.base.hdf5 import h5save
from nilearn.image import smooth_img
import nibabel as nb

datapath = 'BASEDIR'
of = OpenFMRIDataset(datapath)

sub = int(sys.argv[1]) + 1


def smooth(img):
    # we need to preserve the original header because the smoothing function
    # fucks the TR up
    nimg = smooth_img(img, fwhm=2.0)
    return nb.Nifti1Image(nimg.get_data(),
                          img.get_affine(),
                          header=img.get_header())

ds = of.get_model_bold_dataset(
    model_id=1, subj_id=sub,
    flavor='dico_bold7Tp1_to_subjbold7Tp1',
    # full brain
    mask=_opj(
        datapath, 'sub%.3i' % sub, 'templates', 'bold7Tp1',
        'qa', 'jointfgbrainmask_bold7Tp1_to_subjbold7Tp1.nii.gz'),
    preproc_img=smooth,
    # HP filtering is done by NiPy's GLM
    modelfx=fit_event_hrf_model,
    time_attr='time_coords',
    condition_attr='condition')

h5save(_opj('data', 'sub%.3i_2.0mm_hrf.hdf5' % sub), ds)
