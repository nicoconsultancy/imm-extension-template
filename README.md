# Extension Template

### Prerequisites

To use this template you need to install [cruft](https://github.com/cruft/cruft) first:

```bash
pip3 install cruft==2.3
```

### Creating an extension from the template

Run:

`$ cruft create https://github.com/nicoconsultancy/imm-extension-template`

This will create a new extension in the current folder. You will be prompted to enter a name for your extension.

Examples of valid extension names are: `imm_santander_bikes`, `imm_default_classifications`, `imm_unsplash_images`. No spaces, no dashes.


### Updating an extisting extension from this template

If you created the extension using `cruft` then updating is as simple as running:

```bash
$ make update-template
```

### Updating an existing extension created with `cookiecutter`

There are a few steps to upgrade an older extension created using `cookiecutter`. First add these lines to your `pyproject.toml`:

```toml
[tool.cruft]
skip = ["imm_??????", "README.md", "CHANGELOG.md", "pyproject.toml"]
```

Replace `imm_??????` with the folder name of your extension.

Link cruft with this template repository so it knows where to get future updates:

```bash
$ cruft link https://github.com/nicoconsultancy/imm-extension-template -c 8c00f6db934016ab101c5264db29d7de9b030869
```

This should create a `.cruft.json` file. Commit that to the repo. Finally, run:

```bash
$ cruft update
```

to pull in the latest changes from this template. In future, you only need run `make update-template`.
