## The library 'spotify' cannot be found in Visual Studio code Mac OS

### This can apply to the other library

solotion

1. In VS code `import sys` for finding the package install path
2. In VS code `sys.executable` to examine which python is called from
3. go to `terminal`  type `pip show xxx` to find the path of installed packages 
4. In VS code `sys.path.append('[path]')` change the which path to search the path.