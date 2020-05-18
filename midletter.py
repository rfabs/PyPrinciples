#Write a function named mid that takes a string as its parameter. 
#Your function should extract and return the middle letter. 
#If there is no middle letter, your function should return the empty string.
#
#For example, mid("abc") should return "b" and mid("aaaa") should return "".

str_inp = input("Enter a string: ")

def mid(letters):
    lst = list(letters)
    if len(lst) % 2 == 0:
        return ""
    else:
        odd_mid = int(len(lst) / 2) 
        return lst[odd_mid]

#mid("abc")
answer = mid(str_inp)

print(answer)
