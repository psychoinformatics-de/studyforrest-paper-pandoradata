Figures
-------

To build raw version of all figures run ``make figures``. All figures are stored
in ``paper/pics/generated`` in SVG format.

By default python3 is used but the use of python2 can be forced by running:

  ``make figures PYTHON=python``

or something equivalent.


Manuscript
----------

Run ``make paper`` or:

Enter directory ``paper/``.

First thing is to run ``make fancyboilerplate``.

Run ``make`` to compile a PDF.

If it is necessary to generate a Word-like document, ofr whatever reason, first
run ``make plainboilerplate``, next run ``make p.odt`` to compile an OpenOffice
document (needs tex4ht installed).
