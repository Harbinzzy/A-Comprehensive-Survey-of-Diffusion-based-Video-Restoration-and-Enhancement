.PHONY: paper figures check clean
paper:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper.tex
	cp build/paper.pdf paper.pdf
figures:
	python scripts/make_figures.py
check:
	python scripts/validate_sources.py
clean:
	latexmk -c -outdir=build paper.tex
