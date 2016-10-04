STATEMENT=SANAN_Patrick_rOpenSci_Research_Statement
COVER=SANAN_Patrick_rOpenSci_Cover
PDFS = $(STATEMENT).pdf $(COVER).pdf

PDFLATEX=pdflatex  --halt-on-error
BIBTEX=bibtex

BIBFILES=refs.bib

all : $(PDFS)

$(STATEMENT).pdf : $(STATEMENT).tex $(BIBFILES)
	$(PDFLATEX) $<
	$(BIBTEX) $(<:.tex=)
	$(PDFLATEX) $<
	$(PDFLATEX) $<

$(COVER).pdf : $(COVER).tex 
	$(PDFLATEX) $<

# Remove intermediate files
clean : 
	rm -f *.aux *.log *.bbl *.blg *-blx.bib *.nav *.snm *.toc *.vrb *.run.xml *.out

# Remove intermediate files and final files
allclean : clean
	rm -f $(PDFS)

.PHONY : all clean allclean
