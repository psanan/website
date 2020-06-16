all : bib/pds.bib
	latexmk

bib/pds.bib :
	git submodule init
	git submodule update

clean :
	 latexmk -C

.PHONY : all clean
