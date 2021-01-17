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
    > py -m pip --version          # run pip library module as a script
    > pip show <module>            # show pip module
    > pip install -U <module>      # upgrade -U == --upgrade
	> pip install -U pip           # update pip  
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

### Distutils
setuptools: is a collection of enhancements to the Python distutils that allow you to more easily build and distribute Python distributions, 
especially ones that have dependencies on other packages.

    > python setup.py --help-commands
The setup script is the centre of all activity in building, distributing, and installing modules using the Distutils.
To create a source distribution for this module, you would create a setup script, setup.py, containing the above code, 
and run this command from a terminal:

    > python setup.py sdist
If an end-user wishes to install your foo module, all they have to do is download foo-1.0.tar.gz (or .zip),
unpack it, and—from the foo-1.0 directory—run

    > python setup.py install

### Style Guide

PEP 8 -- Style Guide for Python Code. https://www.python.org/dev/peps/pep-0008/

### FastAPI
> FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
> Standards-based: OpenAPI: http://localhost:8000/docs  # openApi by swagger UI   
> Standards-based: OpenAPI: http://localhost:8000/redoc   # openApi by ReDoc   

Dependencias:
* Starlette (Web). Starlette is a lightweight ASGI (Asynchronous Server Gateway Interface) framework/toolkit, which is ideal for building high performance async services. https://www.starlette.io/
* Pydantic (data). Data validation and settings management using python type annotations. https://pydantic-docs.helpmanual.io/
* uvicorn - for the server that loads and serves your application. Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools. https://www.uvicorn.org/

Instalación:

    > pip install fastapi
    > pip install uvicorn

Ejecución por código:

    if __name__ == "__main__":
        uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)
        
Ejecución por consola:

    > uvicorn src.main:app --reload  --port 8083
    > http://localhost:8000/docs (openAPI)

### JWT
> We need to install `PyJWT` to generate and verify the JWT tokens in Python.

    > pip install pyjwt