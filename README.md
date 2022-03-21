

# Environment settings

Check the presence of python3

    python3 -V

response (for instance) Python 3.9.5

Create a venv 

    python3 -m venv venv_ml
    
activate it
    
    python -m pip install -r requirements


## Activate the environment

   CDP_M1_T01_numpy$ . ./venv_ml/bin/activate 

If, inside svcode, the venv is not fisible, serach for it in the tobbar, and add it by selecting the bin/python3.9

## Set kaggle user credential

Make sure your kaggle credential is located in /home/\<user\>/.kaggle folder (see this [help](https://medium.com/@c.venkataramanan1/setting-up-kaggle-api-in-linux-b05332cde53a) to get it).

Then change permissions

    chmod 600 /home/<username>/.kaggle/kaggle.json

## VSCode settings

If you use vscode read the doc: 
https://code.visualstudio.com/docs/datascience/jupyter-notebooks


# M1 T01: Practice with NumPy numerical programming

## Description
Familiarize yourself with Numerical Programming through the NumPy library.

## Level 1

### Exercises 1

Create a function that, given an array of one dimension, gives you a basic statistical summary of the data. If it detects that the array has more than one dimension, it should display an error message.

### Exercises 2

Create a function that generates an NxN square of random numbers between 0 and 100.

- Exercises 3

Create a function that given a two-dimensional table, calculates the totals per row and the totals per column.

- Exercises 4

Manually implements a function that calculates the correlation coefficient. Learn about its uses and interpretation.
