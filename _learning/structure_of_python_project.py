"""
Organize the project
"""
# Found this in Pandas.__init__. So checked. It is actually pretty useful.
# https://stackoverflow.com/questions/35727134/module-imports-and-init-py-in-python
#  files inside your package generally shouldn't contain a
#  if __name__ == '__main__'
#  This is because running a file as a script means it won't be considered part of the package that it belongs to,
#  so it won't be able to make relative imports.


"""
Recommended structure
autility/
    autility/
        ...
    scripts/
        ...
    setup.py
    
"""
