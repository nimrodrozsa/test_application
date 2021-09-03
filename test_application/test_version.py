from os import error
import requests
import json
import sys

file_location = "C:\\Users\\rozsa\\Desktop\\test_application\\test_application\\version.txt"

def print_number(new_number):
    with open(file_location, "w") as f:
                f.write(str(new_number))
                f.close()

response = requests.get(
    'http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000'
)
new_number = response.json()[0]

try:
    r = open(file_location, "r")
    # with open(r"C:\Users\rozsa\Desktop\test application\version.txt") as r:
    number = int(r.readline())
    if number < new_number:
        print_number(new_number)
except (IOError, FileNotFoundError,) as e:
    print(e)
    print_number(new_number)
except:
    print('Exception:', sys.exc_info()[0])


    
    



