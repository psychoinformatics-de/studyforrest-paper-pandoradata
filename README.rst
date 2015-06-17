Article: 7-Tesla fMRI data on the perception of musical genres
==============================================================

This repository contains the sources of the publication:

  Michael Hanke, Richard Dinga, Christian Häusler, J. Swaroop
  Guntupalli, Michael Casey, Falko R. Kaule & Jörg Stadler.
  (2015). High-resolution 7-Tesla fMRI data on the perception of
  musical genres -- an extension to the *studyforrest* dataset.

This is an open access article distributed under the terms of the Creative
Commons Attribution Licence, which permits unrestricted use, distribution,
and reproduction in any medium, provided the original work is properly cited.


Instructions
------------

In order to build a preprint version of the article run `make` in the
root of the repository checkout. This will obtain the necessary data
portions from public sources, build all computationally inexpensive
statistics and figures from scratch and yield a PDF.

The following software is required:

- git
- git-annex
- PyMVPA (automatically cloned via Git)
- Inkscape
- TeX distribution (tested with TeX-Live)
