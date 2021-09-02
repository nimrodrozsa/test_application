import requests
import json

response = requests.get(
    'http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000'
)

print(response.json())
with open(r"C:\Users\rozsa\Desktop\test application\version.txt") as r:
    number = int(r.readline())

    print(number)
    new_number = response.json()[0]
    if number < new_number:
        print(new_number > number)
        with open("C:\\Users\\rozsa\\Desktop\\test application\\version.txt", "w") as f:
            f.write(str(new_number))
            f.close()
    else:
        print(False)

    
    



