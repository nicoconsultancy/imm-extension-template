bold := $(shell tput bold)
byel := $(bold)$(shell tput setaf 11)
end := $(shell tput sgr0)
# extracts the package name from imm-extension.location in pyproject.toml
PACKAGE = $(shell sed -n 's/.*location *= "*\([^ ]*.*\)/\1/p' ./pyproject.toml | cut -d. -f1)

install:
	@printf "$(byel)========== Installing ==========$(end)\n"
	~/.imm/bin/pip install -r requirements.txt

uninstall:
	@printf "$(byel)========== Uninstalling ==========$(end)\n"
	~/.imm/bin/pip uninstall $(PACKAGE)

test:
	@printf "$(byel)========== Testing Extension ==========$(end)\n"
	~/.imm/bin/run-inside-environment imm-cli django test $(PACKAGE)

coverage:
	@printf "$(byel)========== Test Coverage ==========$(end)\n"
	~/.imm/bin/run-inside-environment coverage run --source=$(PACKAGE) ~/.imm/bin/imm-cli django test $(PACKAGE)
	~/.imm/bin/run-inside-environment coverage report -m
	~/.imm/bin/run-inside-environment coverage xml

open:
	xdg-open http://localhost:8000/api/extension/$(PACKAGE)/index

.PHONY: install uninstall test coverage open
.DEFAULT_GOAL := install