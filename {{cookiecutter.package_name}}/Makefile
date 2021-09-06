# extracts the package name from imm-extension.location in pyproject.toml
PACKAGE = $(shell sed -n 's/.*location *= "*\([^ ]*.*\)/\1/p' ./pyproject.toml | cut -d. -f1)
EXTENSION = $(shell sed -n 's/.*extension *= "*\([^ ]*.*\)"/\1/p' ./pyproject.toml | cut -d. -f1)

define notice
      @echo "\n== $1 =="
endef


lint:
	pre-commit run --all-files

test:
	$(call notice,Testing Extension)
	docker exec \
		-w "/imm-api/src/extensions/$(shell basename $(CURDIR))" \
		-e DATABASE_URL="sqlite://:memory:" \
		$(shell docker ps -q -f "name=imm_run_") \
		pytest -x

set-version-number:
	@test $(version) || ( echo "Missing version argument"; exit 1 )

	$(call notice,Update the version number for this extension to $(version))
	sed -i.bak 's/\(^version =\).*/\1 "$(version)"/' pyproject.toml

build:
	python setup.py bdist_wheel
	! (unzip -Z1 dist/$(PACKAGE)-*.whl | grep .py$$)
	! (unzip -Z1 dist/$(PACKAGE)-*.whl | grep .c$$)

clean:
	python setup.py clean
	rm -rf dist/ build/
	find $(PACKAGE) -name "*.c" -delete
	find $(PACKAGE) -name "*.bak" -delete

open:
	xdg-open http://localhost:8000/api/extension/$(PACKAGE)/index

update-template:
	cruft update

.PHONY: lint test open update-template set-version-number clean build
