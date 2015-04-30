SRC=p.tex

all: pics p.pdf
p.pdf: boilerplate.tex p.bbl

fancyboilerplate: fancyboilerplate-stamp
fancyboilerplate-stamp: boilerplate_common.tex boilerplate_fancy.tex
	rm -f plainboilerplate-stamp
	rm -f p.aux
	cat boilerplate_fancy.tex boilerplate_common.tex > boilerplate.tex
	touch $@

plainboilerplate: plainboilerplate-stamp
plainboilerplate-stamp: boilerplate_common.tex boilerplate_plain.tex
	rm -f fancyboilerplate-stamp
	rm -f p.aux
	cat boilerplate_plain.tex boilerplate_common.tex > boilerplate.tex
	touch $@

p.odt: p.pdf
	/usr/share/tex4ht/oolatex p.tex '' '' '' '-interaction=nonstopmode'

pics:
	# for final
	# $(MAKE) -C pics
	$(MAKE) -C pics/generated

clean::
	rm -f revision.log boilerplate.tex *-stamp
	$(MAKE) -C pics clean
	-rm -f *.4ct *.4tc *.idv *.lg *.tmp p.odt *.xref


#
# Private parts: do not touch!
#
pdf: $(SRC:.tex=.pdf) $(SRC:.rst=.pdf)
bib: $(SRC:.tex=.bbl)

TEXFLAGS += -interaction=nonstopmode
PDFLATEX=TEXINPUTS=.:sty:$(TETEXSRC): pdflatex $(TEXFLAGS) -shell-escape
BSTDIR = sty
%.pdf %.aux: %.tex $(MSRC)
	rm -f $*.log
	@run=0; while ( [ ! -e "$*.log" ] || grep -q "Rerun to get" "$*.log" ) && [ $$run -lt 5 ]; do \
	     echo "** Re-running pdftex. Run $$run **";    \
		 $(PDFLATEX) $< >/dev/null 2>&1 || cat $*.log; \
		 run=$$(($$run+1)); \
    done

BIBTEX = bibtex
%.bbl: %.aux
	env BIBINPUTS=$(BIBDIR): BSTINPUTS=$(BSTDIR): $(BIBTEX) $(BIBFLAGS) $*

## Helper if interested in providing proper version tag within the manuscript
ASRC=$(SRC) $(MSRC) $(SSRC)
cleanexts=dvi aux bbl blg end ps pdf djvu log idx toc lot lof ttt tpt fff out nav snm vrb cb cb2
clean::
	rm -f $(foreach file,$(ASRC:.tex=) $(ASRC:.rst=),$(addprefix $(file)., $(cleanexts))) $(MISCTRASH) *~
	rm -f comment.cut
	rm -f revision.tex texput.log
	rm -f $(CODE_TEX) code.sty $(CODE:.py=-snippet*.*)


.PHONY: pics fancyboilerplate plainboilerplate
