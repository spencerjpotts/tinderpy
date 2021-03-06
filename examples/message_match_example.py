'''
# file: message_match_example.py
# Author: 
# Date: 3/18/2019
# Description: 
    Example of Tinderpy auto messaging 

'''

# imoort the tinderpy.py module to have access to the api.
import tinderpy
import time

# assign the variable 'user' to the class Object 'User'
user = tinderpy.User('X-AUTH-TOKEN')

# prompt user welcome message and also include the logged users name using the users object 'user'.name()
print("[!] Welcome ", user.name)

# obtain all matches for the current logged account.
while True:
    # get the matches in the list
    matches = user.matches()
    for match in matches:
        if len(match.messages) is 0:
            match.message("Hey! {0} of the person that match how are you? you are so bea.......".format(match.name))

    # pause script for 5 minutes.
    time.sleep(300)
