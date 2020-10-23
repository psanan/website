all : pds.bib
	latexmk

pds.bib :
	ln -s ${HOME}/work/bib/pds.bib $@

clean :
	 latexmk -C

.PHONY : all clean
