# {{cookiecutter.package_name}}

*TODO: brief description of what this extension does*

## Prerequisites

*TODO: document anything needed before installing this extension such as external API keys or hardware needed*

## Installation

To install this extension into your development environment run:

```bash
make install
```

## Details

### Testing

```bash
make test
```

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
