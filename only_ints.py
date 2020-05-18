# Write a function named only_ints that takes two parameters. 
# Your function should return True if both parameters are integers, and False otherwise.

# For example, calling only_ints(1, 2) should return True, 
# while calling only_ints("a", 1) should return False.

def only_ints(par1, par2):
    val1 = type(par1)
    val2 = type(par2)
    if (val1 == int and val2 == int):
        return True
    else:
        return False

answer1 = only_ints(1, 2)
answer2 = only_ints("a", 3)

print(answer1, answer2)
