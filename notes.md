markdown file for report notes (or something along those lines)

## Changes to codebase
#### dynamic.py
Change to `Mission` class to implement `Mission.from_csv`.

#### control.py
Added module to implement PD controller with initial values `K_P` = 0.6, `K_D` = 0.15; use a class with methods instead of functions so that attributes like $K_P$, $K_D$ can be saved to the `Controller` object
Now changed to `K_P` = 0.07, `K_D` = 0.8 since originally not stable; still a bit rubbish though

## Coding problems
Could not get `PYTHONPATH` to behave nicely via .env file for several hours, not worth staying up for, don't do this. This [thread on Stack Overflow](https://stackoverflow.com/a/62454184) was helpful; Windows uses different syntax, which is why the .env file was not working. Use `;` as path separator and `/` as directory separator.
~~Operated on the PATH string because Python turns `\n` into a new line when passing as an argument, so needed to replace with `/n`.~~ Was not necessary... somehow??
Turns out there was no D action due to forgetting that the local variable is not stored between each call of `control.Controller.run_controller()`. Now fixed


## Solved issues
Implemented `Mission.from_csv` in **dynamic.py**, casting into type _np.ndarray_ as suggested by annotations. 
Implemented PD controller in **control.py**

## Outstanding issues / Improvements to be made
PD controller is a bit naff, maybe try PID?