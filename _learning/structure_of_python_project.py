"""
Organize the project
"""
# Found this in Pandas.__init__. So checked. It is actually pretty useful.
# https://stackoverflow.com/questions/35727134/module-imports-and-init-py-in-python
#  1. files inside your package generally shouldn't contain a
#  if __name__ == '__main__'
#  This is because running a file as a script means it won't be considered part of the package that it belongs to,
#  so it won't be able to make relative imports.
#  2. The reason you want to add import to __init__ is because you want to simplify the user use the package namespace!!
#
"""
Recommended structure
autility/
    autility/
        ...
    scripts/
        ...
    setup.py
    
"""
# 3. Distribute your package!!
# https://packaging.python.org/tutorials/packaging-projects/
# Pretty good
