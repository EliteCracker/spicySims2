import json
import random
import os

''' 
1 read json file
2 get keys from json file and store in list
3 for each key:
    get total values
    generate random number from [0,total values]
    print "key:key[random number]"
'''
# var `data` (dict) is the json data from the file
# var `mainKeys` (array) is the top level keys from the json file

def getKeys(jsonData):
    keys = []
    for key in jsonData.keys():
        if type(jsonData[key]) != dict:
            keys.append(key)
        else:
            keys += getKeys(jsonData[key])
    return keys

def countValues(jsonData,keys,keyIndex):
    count = 0
    for values in jsonData[keys[keyIndex]]:
        count += 1
    return count

def main():
    # open and load json file
    with open("listOfRandoms.json") as file:
        data = json.load(file)

    # get keys from json file
    mainKeys = getKeys(data)

    #

if __name__ == "__main__":
    main()