# Note: in most cases it's easier to use latexmk

PDFS =  \
				Patrick_Sanan_CV.pdf \
				Patrick_Sanan_Resume.pdf \
				Patrick_Sanan_publications_list.pdf

BIBFILES = pds.bib

PDFLATEX=pdflatex --halt-on-error
BIBTEX=bibtex

all : $(PDFS)

# Usual pdfs (w/ bibtex)
%.pdf : %.tex $(BIBFILES)
	$(PDFLATEX) $<
	$(BIBTEX) $(<:.tex=)
	$(PDFLATEX) $<
	$(PDFLATEX) $<

# Simple pdfs (no bibtex)
Patrick_Sanan_Resume.pdf : Patrick_Sanan_Resume.tex
	$(PDFLATEX) $<
	$(PDFLATEX) $<

# Inclusion dependencies
Patrick_Sanan_CV.pdf : \
	av.inc.tex \
	computer.inc.tex \
	education.inc.tex \
	employment.inc.tex \
	honors.inc.tex \
	info.inc.tex \
	posters.inc.tex \
	software.inc.tex \
	talks.inc.tex \
	teaching.inc.tex

Patrick_Sanan_Resume.pdf : \
	education.inc.tex \
	employment.inc.tex \
	info.inc.tex \
	interests.inc.tex

# Remove intermediate files
clean :
	rm -f *.aux *.log *.bbl *.blg *-blx.bib *.nav *.snm *.toc *.vrb *.run.xml *.out *.spl *.fls *.fdb_latexmk
	rm -f $(PDFS)

.PHONY : all clean
