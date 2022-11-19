all : pds.bib
	latexmk
	latexmk -c

pds.bib :
	ln -s ${HOME}/academic/bib/pds.bib $@

clean :
	 latexmk -C

.PHONY : all clean
