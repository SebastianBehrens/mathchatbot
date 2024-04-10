from numpy.random import choice
from numpy.random import randint
from numpy import array
from re import split
import logging

def instantiate_exercise(exercise) -> str:
    
    def fill_param(hint) -> int:
        if hint == "any":
            digit = choice(
                a=[-3, -2, -1, 0, 1, 2, 3, "a", "b", "x", "y"],
                size=1,
                p=array([0.1, 0.1, 0.1, 0.05, 0.1, 0.1, 0.1, 0.075, 0.075, 0.125, 0.075 ])
            )
        elif hint == "positive":
            digit = choice(
                a=[1, 2, 3, "a", "b", "x", "y"],
                size=1,
                p=array([0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1])
            )
        elif hint == "nonzero":
            digit = choice(
                a=[-3, -2, -1, 1, 2, 3, "a", "b", "x", "y"],
                size=1,
                p=array([0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.025, 0.025, 0.025, 0.025 ])
            )
        elif hint == "vars":
            digit = choice(
                a=["a", "b", "x", "y", "l", "m", "n", "k", "p", "z"],
                size=1,
                p=array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
            )
        else:
            logging.error(f"Unseen hint ({hint}) received in fill_param.")
            raise Exception(f"Unseen hint ({hint}) received in fill_param.")
        return(str(digit[0]))

    def get_sign(hint) -> str:
        if hint in ["SS", "S1", "S2", "S3", "S4"]:
            sign = choice(
                a=["+", "-", "*", ":"],
                size=1,
                p=array([0.3, 0.3, 0.3, 0.1])
            )
        elif hint == "SPM":
            sign = choice(
                a=["+", "-"],
                size=1,
                p=array([0.5, 0.5])
            )
        return(sign[0])

    if exercise.vars is not None:
        for var in exercise.vars.keys():
            exercise.math = exercise.math.replace(var, fill_param(exercise.vars[var]))
        for sign_replace in ["SS", "S1", "S2", "S3", "S4", "SPM"]:
            exercise.math = exercise.math.replace(sign_replace, get_sign(sign_replace))

    return(exercise)
