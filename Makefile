PDFS =  \
				SANAN_Patrick_CV.pdf \
				SANAN_Patrick_publications_list.pdf

BIBFILES = pds.bib

# any plots to be generated with python scripts of the same name
PLOT_PDFS=

PDFLATEX=pdflatex --halt-on-error
BIBTEX=bibtex
PYTHON3=python3

all : $(PDFS)

plots : $(PLOT_PDFS)

%.pdf : %.tex $(BIBFILES) plots
	$(PDFLATEX) $<
	$(BIBTEX) $(<:.tex=)
	$(PDFLATEX) $<
	$(PDFLATEX) $<

images/%.pdf : images/%.py
	$(PYTHON3) $<
	mv $(@:images/%=%) images

# Keep the intermediate images
.SECONDARY : $(PLOT_PDFS)

# Remove intermediate files
clean :
	rm -f *.aux *.log *.bbl *.blg *-blx.bib *.nav *.snm *.toc *.vrb *.run.xml *.out *.spl *.fls *.fdb_latexmk
	rm -f $(PDFS) $(PLOT_PDFS)

.PHONY : all clean plots
