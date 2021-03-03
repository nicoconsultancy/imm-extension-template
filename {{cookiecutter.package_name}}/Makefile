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
	docker exec -w "/$(EXTENSION)" -e DATABASE_URL="sqlite://:memory:" $(WORKSPACE) pytest -x

bump-version:
	@test $(version) || ( echo "Missing version argument"; exit 1 )

	$(call notice,Update the version number for this extension to $(version))
	sed -i.bak 's/\(^version =\).*/\1 "$(version)"/' pyproject.toml

wheel:
	python setup.py bdist_wheel
	! (unzip -Z1 dist/$(PACKAGE)-$(version)-*.whl | grep .py$$)
	! (unzip -Z1 dist/$(PACKAGE)-$(version)-*.whl | grep .c$$)

prepare-release: bump-version wheel
	$(call notice,The release has been prepared)

publish-release:
	@test $(version) || ( echo "Missing version argument"; exit 1 )
	@test $(IMM_STORE_TOKEN) || ( echo "Missing IMM_STORE_TOKEN environment variable"; exit 1 )
	@test $(IMM_STORE_URL) || ( echo "Missing IMM_STORE_URL environment variable"; exit 1 )
	@test $(PRIVATE_PYPI_USERNAME) || ( echo "Missing PRIVATE_PYPI_USERNAME environment variable"; exit 1 )
	@test $(PRIVATE_PYPI_PASSWORD) || ( echo "Missing PRIVATE_PYPI_PASSWORD environment variable"; exit 1 )

	$(call notice,Uploading the Python packages to the repository)
	twine upload \
		--username="$(PRIVATE_PYPI_USERNAME)" \
		--password="$(PRIVATE_PYPI_PASSWORD)" \
		--non-interactive \
		--repository-url \
		 https://pip.immsuite.cloud dist/$(PACKAGE)-$(version)-*.whl

	$(call notice,Uploading the metadata to the extension store)
	IMM_STORE_URL="$(IMM_STORE_URL)" IMM_STORE_TOKEN="$(IMM_STORE_TOKEN)" python scripts/publish.py

clean:
	python setup.py clean
	rm -rf dist/ build/
	find $(PACKAGE) -name "*.c" -delete
	find $(PACKAGE) -name "*.bak" -delete

open:
	xdg-open http://localhost:8000/api/extension/$(PACKAGE)/index

update-template:
	cruft update

.PHONY: install uninstall test coverage open update-template bump-version clean prepare-release publish-release wheel
.DEFAULT_GOAL := install
