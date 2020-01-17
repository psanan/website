PDFS =  \
				Patrick_Sanan_CV.pdf \
				Patrick_Sanan_Resume.pdf \
				Patrick_Sanan_publications_list.pdf

BIBFILES = bib/pds.bib

LATEXMK = latexmk

all : ${PDFS}

bib/pds.bib :
	git submodule init
	git submodule update

%.pdf : %.tex ${BIBFILES}
	${LATEXMK} ${@:.pdf=}

clean :
	rm -f *.aux *.log *.bbl *.blg *-blx.bib *.nav *.snm *.toc *.vrb *.run.xml *.out *.spl *.fls *.fdb_latexmk
	rm -f ${PDFS}

.PHONY : all clean
