#!/bin/bash

. /etc/fsl/fsl.sh

set -u
set -e

sub="$(zeropad $1 3)"
nperm=$2
iter=$3
iter="$(( $iter % $nperm ))"

if [ "$iter" = "0" ]; then
	PYTHONPATH=~/PyMVPA \
		~/PyMVPA/bin/pymvpa2 searchlight \
			-i data/sub${sub}_2.0mm_hrf.hdf5 \
			--ds-preproc-fx pymvpa2_zscore_ds.py \
			--payload pymvpa2_cv_setup.py \
			--neighbors 2 \
			--scatter-rois 2 \
			--nproc 1 \
			-o results/sub${sub}_2.0mm_hrf_sl_orig.hdf5
else
	iter="$(zeropad $iter 3)"
	PYTHONPATH=~/PyMVPA \
		~/PyMVPA/bin/pymvpa2 searchlight \
			-i data/sub${sub}_2.0mm_hrf.hdf5 \
			--ds-preproc-fx pymvpa2_permute_ds.py \
			--payload pymvpa2_cv_setup.py \
			--neighbors 2 \
			--scatter-rois 2 \
			--nproc 1 \
			-o results/sub${sub}_2.0mm_hrf_sl_perm${iter}.hdf5
	# save some space: we only need the samples
	PYTHONPATH=~/PyMVPA \
		~/PyMVPA/bin/pymvpa2 dump \
			-i results/sub${sub}_2.0mm_hrf_sl_perm${iter}.hdf5 \
			-o results/sub${sub}_2.0mm_hrf_sl_perm${iter}.npy \
			-f npy \
			-s
	rm results/sub${sub}_2.0mm_hrf_sl_perm${iter}.hdf5
fi
