PYTHON = python3

all: data figures paper.pdf

data:
	[ ! -d data ] && git clone http://psydata.ovgu.de/forrest_gump/.git data || git -C data pull
	cd data && git annex get \
		sub*/BOLD/task002_run*/bold_dico_moco.txt \
		stimulus/task002/stimuli/*

paper.pdf: figures
	$(MAKE) -C paper fancyboilerplate all
	cp paper/p.pdf paper.pdf

figures: data \
         paper/pics/stimulus_specgrams.svg \
         paper/pics/generated/motionqc.svg 

pymvpa:
	git clone https://github.com/PyMVPA/PyMVPA.git pymvpa

paper/pics/generated/stimulus_specgrams.svg: code/figures/fig_stim_specgram.py
	$(PYTHON) $<

paper/pics/generated/motionqc.svg: pymvpa
	PATH=$${PWD}/pymvpa/bin:$${PATH} \
	PYTHONPATH=$${PWD}/pymvpa:$${PYTHONPATH} \
	pymvpa2 ofmotionqc --path data -t 2 --estimate-fname bold_dico_moco.txt \
		--estimate-order transrot --outlier-stdthresh 2 \
		--outlier-minthresh 1.4 --savefig $@

clean:
	-rm -f paper.pdf
	-rm -rf paper/pics/generated/*.svg
	$(MAKE) -C paper clean

distclean: clean
	-chmod -R u+w data/.git/annex/objects/*
	-rm -rf data pymvpa

.PHONY: figures clean distclean
