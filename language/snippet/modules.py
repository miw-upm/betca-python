# when the interpreter runs a module, the __name__ variable will be set as  __main__,
# But if the code is importing the module from another module, then the __name__  will be set to that module’s name.
# Execute only if run as a script
if __name__ == "__main__":
    print('running main... ')

