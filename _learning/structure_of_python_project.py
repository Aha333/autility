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

# 4. Pip install -e project_path
# This is very good!
# Another way it to run and set up the sys.path.add('.').
# But anyway,
"""
Last thing to note is that pip install will install the current package as it is right now. 
If you pip install a package you're developing and add some new files to it afterwards, 
these changes will not be reflected on the actual package installed beforehand.
 
 To avoid having to pip install the package again and again after each change, 
 you can pass the -e flag to make an editable install; in this case, changes to your files
  inside the project folder will automatically reflect in changes on your installed package in the site-packages folder.

So here I install this package in venv. then you can run it .
You can see if I quit, you would not be able to refer to the package!!
(venv) macbook-pro:autility dawei$ python ./scripts/plot_something.py 
after pip install -e

(venv) macbook-pro:autility dawei$ deactivate
macbook-pro:.. dawei$ python fullpath//scripts/plot_something.py 

Now you don't need to care about where you are.

Traceback (most recent call last):
  File "./scripts/plot_something.py", line 1, in <module>
    import autility.parallel.parallel_with_process_bar
ImportError: No module named autility.parallel.parallel_with_process_bar

"""