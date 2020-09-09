from typing import List
import requests


def badsum(x: int, y: int) -> int:
    
    # returns the sum of x and y
    return x + y


def writefile():
    pass


def getexternaldata():
    
    response = requests.get("http://www.google.nl")
    
    with open("data.txt") as f:
        f.write(response.text)


