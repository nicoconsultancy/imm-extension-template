# Extension Template

### Prerequisites

To use this template you need to install [cookiecutter](https://github.com/cookiecutter/cookiecutter) first.

### Creating an extension from the template

Run:

`$ cookiecutter https://www.immsuite.com/dist/imm-extension-template.zip`

This will create a new extension in the current folder. You will be prompted to enter a name for your extension.

Examples of valid extension names are: `imm_santander_bikes`, `imm_default_classifications`, `imm_unsplash_images`. No spaces, no dashes.

##### Development Notes

`cookiecutter` doesn't support loading a template from a private git repository. 

If you update this repo you need to zip up the contents and upload it to `www.immsuite.com/dist/imm-extension-template.zip`.
