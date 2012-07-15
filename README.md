# BRASS
This is an idea I've had for a while: a reimagining of Wasteland written in python. Its a work in progress (and has been for some time).

## Requirements

The only major requirements are pyglet (and python 2.6 or greater). For more details, please see the pip_freeze.txt file for the list of libs installed as I was doing development.

## Running
To start:

> python src/game.py brass.game 

## Tests
The tests are broken down into two types at the moment, automated tests and manual tests.

### Automated Tests
To run the automated tests, simply run =nosetests= at the project root.

### Manual Tests
To get the manual tests to run, it might be necessary to set the PYTHONPATH in order for it to find the code correctly. This should do the trick:

> export PYTHONPATH=./src

 
