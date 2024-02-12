import json
from pip._vendor import requests

# ---- functions for API ----
def get_dad_joke():  
    url = 'https://icanhazdadjoke.com/'
    heads = {'Accept': 'application/json'}
    response = requests.get(url, headers=heads).json()
    return response

# reveive a list and a string
# search for a string
# return a list
def make_sublist(lst, word):
    pass


# ---- functions to get data from a text file
# reads from a file
# returns one string
def get_one_string(filename):
    pass


# reads from a file
# returns a list of floats
def get_float_list(filename):
    pass




# ---- functions for strings ----

# receives a string
# removes newlines
# returns a string
def clean_string(s, drop_list):
    pass



# receives a string, splits to list of strings
# returns a dictionary with key:value = item:count
def create_counts_dict(s):
    pass



