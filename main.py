import pandas as pd
import random
from string import ascii_letters

def rand_string():
    return "".join([ascii_letters[random.randint(0,len(ascii_letters))-1] for y in range(random.randint(4,12))])

def rand_string_list():
    return [rand_string() for y in range(115)]

def rand_int_list():
    return [random.randint(0,2500) for y in range(115)]

def randDf():
    return pd.DataFrame(
            {
                rand_string():(rand_int_list() if x%7==0 else rand_string_list())
                for x in range(10)
            }
        )

print(randDf().head())