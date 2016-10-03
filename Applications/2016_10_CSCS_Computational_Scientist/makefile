PDFS = SANAN_patrick_CSCS_2016_10.pdf

PDFLATEX=pdflatex --halt-on-error

all : $(PDFS)

%.pdf : %.tex 
	$(PDFLATEX) $<

# Remove intermediate files
clean : 
	rm -f *.aux *.log *.bbl *.blg *-blx.bib *.nav *.snm *.toc *.vrb *.run.xml *.out

# Remove intermediate files and final files
allclean : clean
	rm -f $(PDFS)

.PHONY : all clean allclean
