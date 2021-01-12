# Python
> Python es un lenguaje de programación interpretado, dinámico y multiplataforma.
> Es multiparadigma: soporta orientación a objetos, programación imperativa y programación funcional.
> Es administrado por la Python Software Foundation. Posee una licencia de código abierto. https://www.python.org/

## Instalación
> https://www.python.org/downloads/   

Datos locales de instalación: `C:\Users\equipo\AppData\Local\Programs\Python\Python39`.   
CLI:   

    > python --version
    > py -V             # py==python -V==--version
	> py -h             # -h==--help
	> py -0             # List the available pythons

### pip
> pip is the package installer for Python

    > pip list                     # List installed packages
    > pip --version
    > py -m pip --version          #  run pip library module as a script
    > pip show pip                 # show pip version
    > pip install -U <module>      # upgrade
	> pip install -U pip           # update pip  -U == --upgrade
	> py -m pip unistall <module>  # unistall

### PyPI (https://pypi.org/)
> The Python Package Index (PyPI) is a repository of software for the Python programming language.
The Python Package Index is the key repository for Python distributions 
where you can find Python software created and shared by other developers to install and use in your own programs.

### virtual environment
> a self-contained directory tree that contains a Python installation for a particular version of Python, 
plus a number of additional packages.

     > py -m venv <project-name\venv>  # create a vistual environment
	 > venv\Scripts\activate.bat
	 > venv\Scripts\deactivate.bat

### tests
     > python -m unittest discover tests

### Distutils
setuptools: is a collection of enhancements to the Python distutils that allow you to more easily build and distribute Python distributions, 
especially ones that have dependencies on other packages.
