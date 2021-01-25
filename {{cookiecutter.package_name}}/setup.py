import os
import re
import sys

from setuptools import find_packages
from setuptools import glob
from setuptools import setup
from setuptools.command.build_py import build_py

try:
    import toml
except ImportError:
    sys.exit("missing required package: toml")

try:
    from Cython.Build import cythonize
    from Cython.Compiler import Options
    from Cython.Distutils import Extension
except ImportError:
    sys.exit("missing required package: cython")

# [ Read the extension's metadata from pyproject.toml ] --------------------------------------------------------------
try:
    pyproject = toml.load(open("pyproject.toml"))
except FileNotFoundError:
    raise
except toml.TomlDecodeError:
    raise ValueError("Syntax error in pyproject.toml file")
else:
    metadata = pyproject.get("imm-extension", {})

    assert "name" in metadata, "pyproject.toml is missing required key from the [imm-extension] section: name"
    assert "vendor" in metadata, "pyproject.toml is missing required key from the [imm-extension] section: vendor"
    assert "url" in metadata, "pyproject.toml is missing required key from the [imm-extension] section: url"
    assert "support" in metadata, "pyproject.toml is missing required key from the [imm-extension] section: support"
    assert "description" in metadata, "pyproject.toml is missing required key from the [imm-extension] section: description"
    assert "location" in metadata, "pyproject.toml is missing required key from the [imm-extension] section: location"
    assert "version" in metadata, "pyproject.toml is missing required key from the [imm-extension] section: version"

    package = metadata.get("location").split(".")[0].lower()  # "imm_sample.ext:ext" -> "imm-sample"

# [ Read the extension's dependencies from from requirements.txt ] ---------------------------------------------------
requirements = []
if os.path.exists("requirements.txt"):
    for line in open("requirements.txt").readlines():
        line = line.strip()
        if not line or line.startswith("-") or line.startswith("#"):
            # editable package or a comment, skip it
            continue
        requirements.append(line)


# [ Use cython to compile all .py files to .so ] ---------------------------------------------------------------------
def get_ext_modules():
    if "build_ext" not in sys.argv and "bdist_wheel" not in sys.argv:
        # this isn't a binary build, so we dont need to cythonize the source
        return None

    # cython compiles all the .py files to .so objects that are included in the .whl
    # this should ONLY be run with bdist_wheel and NEVER sdist

    Options.docstrings = False
    Options.fast_fail = True
    Options.warning_errors = True
    Options.error_on_unknown_names = True
    Options.error_on_uninitialized = True
    compiler_directives = {
        "binding": True,  # default in cython 3
        "language_level": "3",
        "warn.unreachable": False,
    }

    # we need to create an Extension for each source .py file in the project
    # so that cython will compile it to .so
    packages = find_packages()
    source_py_files = []
    for pkg in packages:
        for source_py in glob.glob(pkg.replace(".", os.sep) + os.sep + "*.py"):
            module = source_py[:-3]  # strip .py
            module = module.replace(os.sep, ".")
            extension = Extension(module, [source_py])
            source_py_files.append(extension)

    return cythonize(source_py_files, compiler_directives=compiler_directives)


# [ Don't add the .py files to the build ] ---------------------------------------------------------------------------
class SkipSourceFilesBuildPy(build_py):
    def run(self):
        # normally this build_py step will include .py files in the distribution
        # we want to skip that step, but we need to run build_package_data so that
        # the files specified in setup(..., package_data={}) get included
        build_py.build_package_data(self)

    def exclude_data_files(self, package, src_dir, files):
        # don't add .py or .c source code files to the build
        banned_file_extensions = [
            ".py",
            ".c",
        ]
        return super().exclude_data_files(
            package, src_dir, [f for f in files if os.path.splitext(f)[1] not in banned_file_extensions]
        )


# [ Collect files to be included in the package ] --------------------------------------------------------------------


def get_package_data(folder):
    include_files = []
    for rule in metadata.get("include-files", []):
        for f in glob.glob(os.path.join(folder, rule), recursive=True):
            # strip the package/ prefix from he beginning of the path
            include_files.append(f[len(folder) + 1 :])
    return {folder: include_files}


######################################################################################################################


setup(
    name=re.sub(r"[-_.]+", "-", package),
    version=metadata.get("version"),
    description=metadata.get("name"),
    long_description=metadata.get("description"),
    url=metadata.get("url"),
    author=metadata.get("vendor"),
    author_email=metadata.get("support"),
    packages=find_packages(),
    cmdclass={"build_py": SkipSourceFilesBuildPy},
    ext_modules=get_ext_modules(),
    include_package_data=False,  # don't read MANIFEST.in, use package_data below
    package_data=get_package_data(package),
    entry_points={
        "imm_extension": [
            package + " = " + metadata.get("location"),  # "{package} = import_path.to.extension:extension"
        ]
    },
    python_requires=">=3.8, <4",
    install_requires=requirements,
    zip_safe=False,
)
