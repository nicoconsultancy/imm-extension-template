# {{cookiecutter.package_name}}

[!Build and upload extension](https://github.com/nicoconsultancy/{{ cookiecutter.package_name|replace("_","-") }}/workflows/Build%20and%20upload%20extension/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


*TODO: brief description of what this extension does*

## Setup

### Prerequisites

*TODO: document anything needed before installing this extension such as external API keys or hardware needed*

### Installation

To install this extension into your [development-environment](https://github.com/nicoconsultancy/imm-development-environment) run:

```bash
make install
```

### Workflow

In order for the workflows to work correctly, there are some *soft* rules on branch naming to follow. When working on issues, bugfix branches should be named as follows:
```bash
fix/\${ISSUE_NUMBER}-\*\*
```

While features/enhancements should be:
```bash
feat/\${ISSUE_NUMBER}-\*\*
```

After the issue number, there should be a **short** description of the feature/issue. For example a branch could be `feat/11-cool-feature`.

This way, the system will detect what the next version will be automatically. Additionally, you can manually add the labels `major`, `minor` or `patch` to a pull request in github to determine what the next version will be.

### Testing

You will need the development environment running.

```bash
make test
```

## Details

### Viewing

While developing, assuming the extension is using views (and the default view is named `index.html`), you can run the following to quickly open the extension in your default browser:

```bash
make open
```

This is setup for linux by default. In order to make this work for Mac, change line line 26 in the `Makefile` to the following:

```bash
    open http://localhost:8000/api/extension/$(PACKAGE)/index
```

### Operation

*TODO: Document how the extension works*

### Settings

*TODO: Document the settings*

## Changelog

See full list of changes [here](./CHANGELOG.md)
