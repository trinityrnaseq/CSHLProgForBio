The special __name__ variable in python is used to determine whether or not the code being executed is in the 'driver' script or an imported module.

Including the structure:
```
def main():
    pass

if __name__ == '__main__':
    main()
```

in your python scripts will allow you to have code only execute when you run that script, and not run if you 'import' it into another 'driver'.


