# The goal of this challenge is to analyze a string to check if it contains
# two of the same letter in a row. For example, the string "hello" has l twice in a row,
# while the string "nono" does not have two identical letters in a row.

# Define a function named double_letters that takes a single parameter.
# The parameter is a string. Your function must return True if there are
# two identical letters in a row in the string, and False otherwise.

def double_letters(word):
    if len(word) < 2:
        return False
    else:
        id = 0
        for let in word:
            #if let[id] == let[id+1]:
            arg = let
            id += 1
        return arg, id


answer1 = double_letters("hello")
answer2 = double_letters("nano")
answer3 = double_letters("a")
print(answer1, answer2, answer3)
