# Module: Replit Project Name Generator
#
# Author: t-mthy
#
# Description: Similar function as Replit's automatic randomized project name
# when creating new Repls
# ==============================================================================


import requests
from random import randint
import os


def clear():
    return os.system('cls')


def randomize_word(list):
    # len-1 prevent list out of bound
    rand_idx = randint(0, len(list) - 1)
    rand_word = list[rand_idx].capitalize()

    return rand_word


def link_word(list):
    ans = ''

    for i in range(3):
        ans += randomize_word(list)
        if i < 2:
            ans += '-'

    return ans


url = 'https://www.mit.edu/~ecprice/wordlist.10000'

# get all data from page
req = requests.get(url)

# data to text
txt = req.text
word_list = txt.split()

# link 3 randomized words from list
res = link_word(word_list)

clear()
print("\n\n" + res + "\n\n")
req.close()
