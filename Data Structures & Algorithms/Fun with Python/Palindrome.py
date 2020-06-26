#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

os.system('cls' if os.name == 'nt' else 'clear')


print("This program will determine if your word is a palindrome.")
print("What is a palindrome?")
print("A palindrome is a word that is the same spelled backwards as it is spelled forwards.")
print("For example 'Racecar' is a palindrome.")
input("Press enter to continue...")


def split(word):
    return [char for char in word]

def count(word):
    return len(word)

def reverse(word):
    counter = count(word) - 1
    reversedString = ''
    for i in range(count(word)):
        reversedString += split(word)[counter]
        counter -= 1
    return reversedString

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    inputString = input("Enter a word: ")
    normalizedString = inputString.lower()

    if(normalizedString == reverse(normalizedString)):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

    print()
    input("Press enter to next word...")

