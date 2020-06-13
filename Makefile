LATEXMK = latexmk

all : bib/pds.bib
	${LATEXMK} Patrick_Sanan_CV
	${LATEXMK} Patrick_Sanan_Resume
	${LATEXMK} Patrick_Sanan_publications_list

bib/pds.bib :
	git submodule init
	git submodule update

clean :
	${LATEXMK} -C

.PHONY : all clean
