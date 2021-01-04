.PHONY: help

help:
	@python -c "import re;help='\n'.join([line.replace('##','\n\t') for line in open('Makefile').readlines() if re.search('^[a-zA-Z0-9\-\_]*?\:[\s\S]*?$$',line,flags=re.I)]);print help"

.DEFAULT_GOAL := help

clean: ## clean target files
	rm -vrf dist
	rm -vrf build

gen_dep:
	pip freeze > requirements.txt

dep: gen_dep