all: pics

# Optionally some PICS could be ignored. By default XXX ones.
# PICS_IGNORE must contain a rule for grep
PICS_IGNORE ?= "study_workflow"

# For every .svg we must have a pdf
PICS=$(shell find . -iname \*svg \
	| sed -e 's/svg/pdf/g' -e 's/\([^\]\)\([ \t:]\)/\1\\\\\2/g' \
	| grep -v -e $(PICS_IGNORE) )

pics: $(PICS)

clean:
	for p in *.svg; do rm -f $${p%*.svg}.eps $${p%*.svg}.eps $${p%*.svg}.pdf; done

.PHONY: ignore-%
ignore-%:
	@grep -q "^$*$$" .gitignore || { \
	  echo "$*" >> .gitignore; echo "Ignore $@"; }

#
# Inkscape rendered figures
#
%.pdf: %.svg ignore-%.pdf
	@echo "Rendering $@"
	@inkscape -z -f "$<" -A "$@"

%.eps: %.svg ignore-%.eps
	@echo "Rendering $@"
	@inkscape -z -f "$<" -E "$@"

%_600dpi.png: %.svg ignore-%_600dpi.png
	@echo "Rendering $@"
	@inkscape -z -f "$<" -e "$@" -d 600

.PHONY: all pics
