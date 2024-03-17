from numpy.random import choice
from numpy.random import randint
from numpy import array
from re import split


def instantiate_exercise(exercise):
    def fill_param():
        digit = choice(
            a=[-3, -2, -1, 0, 1, 2, 3, "a", "b", "x", "y"],
            size=1,
            p=array([0.1, 0.1, 0.1, 0.05, 0.1, 0.1, 0.1, 0.075, 0.075, 0.125, 0.075 ])
        )
        return(str(digit[0]))

    def get_sign():
        sign = choice(
            a=["+", "-", "*", ":"],
            size=1,
            p=array([0.3, 0.3, 0.3, 0.1])
        )
        return(sign[0])

    rand_set = exercise.randomize[randint(len(exercise.randomize))]
    print(exercise.math)
    print(rand_set)
    for var in split(",\s*", rand_set):
        print(var)
        exercise.math = exercise.math.replace(var, fill_param())
    for sign_replace in ["SS", "S1", "S2", "S3", "S4"]:
        exercise.math = exercise.math.replace(sign_replace, get_sign())

    print(exercise.math)
    

    return(exercise)
