# Pokemon_App
    This is the code that is used to generate and use pokemon data
 
# Folder Structure
## venv
    Venv is a virtual environment module that is used to handle dependencies. This way no matter what's on my computer, I can activate this virtual environment (venv) and have everything work as expected. I installed with this with python3 so after activating the venv you can use pip and python as a proxy for pip3 and python3. 
    To create a venv:                    `python3 -m venv <folder_name> --prompt="<terminal_name>" --upgrade-deps`
    To activate a venv:                  `source <folder_name>/bin/activate`
    To install packages into venv:       `python -m pip install <package-name>`
    To install dependencies from .txt.:  `python -m pip install -r requirements.txt`
    To list packages & versions in venv: `python -m pip list`
    Save dependencies in .txt file:      `python -m pip freeze > requirements.txt`
    To deactivate venv:                  `deactivate`

    Link to more info: https://realpython.com/python-virtual-environments-a-primer/

### venv/bin: 
    bin contains the executable files of your virtual environment. Most notable are the Python interpreter (python) and the pip executable (pip), as well as their respective symlinks (python3, python3.10, pip3, pip3.10). The folder also contains activation scripts for your virtual environment. Your specific activation script depends on what shell you use.

### venv/include:
    include is an initially empty folder that Python uses to include C header files for packages you might install that depend on C extensions.

### venv/lib/python3.10/site-packages:
    lib contains the site-packages directory nested in a folder that designates the Python version (python3.10). site-packages is one of the main reasons for creating your virtual environment. This folder is where you’ll install external packages that you want to use within your virtual environment. By default, your virtual environment comes preinstalled with two dependencies, pip and setuptools.

#### site-packages/_distutils_hack:
    Ensures that when performing package installations, Python picks the local ._distutils submodule of setuptools over the standard library’s distutils module.

#### site-packages/pkg_resources:
    Helps applications discover plugins automatically and allows Python packages to access their resource files. It’s distributed together with setuptools.

#### site-packages/{name}-{version}.dist-info
    Contain package distribution information that exists to record information about installed packages.

#### site-packages/distutils-precedence.pth 
    This file helps set the path precedence for distutils imports and works together with _distutils_hack to ensure that Python prefers the version of distutils that comes bundled with setuptools over the built-in one.

### venv/pyvenv.cfg:
    pyvenv.cfg is a crucial file for your virtual environment. It contains only a couple of key-value pairs that Python uses to set variables in the sys module that determine which Python interpreter and which site-packages directory the current Python session will use. You’ll learn more about the settings in this file when you read about how a virtual environment works.