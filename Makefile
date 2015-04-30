PYTHON = python3

all: paper

paper:
	$(MAKE) -C paper fancyboilerplate p.pdf
	cp paper/p.pdf paper.pdf

figures:
	$(PYTHON) code/fig_stim_specgram.py

clean:
	-rm -f paper.pdf
	-rm -rf paper/pics/generated/*.svg

.PHONY: paper figures
