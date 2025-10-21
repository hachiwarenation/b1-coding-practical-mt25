markdown file for report notes (or something along those lines)

## Changes to codebase
#### dynamic.py
Change to `Mission` class to implement `Mission.from_csv`.
Add **control.py** module to implement PD controller

## Coding problems
Could not get `PYTHONPATH` to behave nicely via .env file for several hours, not worth staying up for, don't do this. This [thread on Stack Overflow](https://stackoverflow.com/a/62454184) was helpful; Windows uses different syntax, which is why the .env file was not working. Use `;` as path separator and `/` as directory separator.
~~Operated on the PATH string because Python turns `\n` into a new line when passing as an argument, so needed to replace with `/n`.~~ Was not necessary... somehow??


## Solved issues
Implemented `Mission.from_csv` in **dynamic.py**, casting into type _np.ndarray_ as suggested by annotations. 
Implemented PD controller in **control.py**

## Outstanding issues / Improvements to be made