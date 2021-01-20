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

bump-version:
	@test $(version) || ( echo "Missing version argument"; exit 1 )

	$(call notice,Update the version number for this extension to $(version))
	sed -i.bak 's/\(^version =\).*/\1 "$(version)"/' pyproject.toml

wheel:
	$(PYTHON) setup.py bdist_wheel
	! (unzip -Z1 dist/*.whl | grep .py$$)
	! (unzip -Z1 dist/*.whl | grep .c$$)

prepare-release: bump-version wheel
	$(call notice,The release has been prepared)

publish-release:
	@test $(version) || ( echo "Missing version argument"; exit 1 )
	$(call notice,Uploading the Python packages to the repository)
	~/.imm/bin/twine upload --repository-url https://pip.immsuite.cloud dist/$(PACKAGE)-$(version)-*.whl && $(PYTHON) scripts/publish.py

	$(call notice,Uploading the metadata to the extension store)
	curl --location "https://store.immsuite.com/api/v1/extensions/store/$(PACKAGE)/upload" -u "user:pass" --form "file=@pyproject.toml"

clean:
	$(PYTHON) setup.py clean
	rm -rf dist/ build/
	find $(PACKAGE) -name "*.c" -delete
	find $(PACKAGE) -name "*.bak" -delete


open:
	xdg-open http://localhost:8000/api/extension/$(PACKAGE)/index

update-template:
	cruft update

.PHONY: install uninstall test coverage open update-template
.DEFAULT_GOAL := install
