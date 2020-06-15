LATEXMK = latexmk

all : bib/pds.bib
	${LATEXMK}

bib/pds.bib :
	git submodule init
	git submodule update

clean :
	${LATEXMK} -C

.PHONY : all clean
