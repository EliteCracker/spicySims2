import json
import random
import os

# var `data` (dict) is the json data from the file
# var `mainKeys` (array) is the top level keys from the json file

# gets all top-level keys (variable `mainKeys``)
def getKeys(jsonData):
    keys = []
    for key in jsonData.keys():
        if type(jsonData[key]) != dict:
            keys.append(key)
        else:
            keys += getKeys(jsonData[key])
    return keys

# Counts number of values a certain key has
def countValues(key):
    count = -1
    for values in data[key]:
        count += 1
    return count

# Draws turn-ons & off. Checks if next randint == previous. If so, redraw. Put this in a function to keep main() "concise"
def getTurns():
    firstTurn = random.randint(0, countValues("turns"))
    secondTurn = random.randint(0, countValues("turns"))
    while secondTurn == firstTurn:
        secondTurn = random.randint(0, countValues("turns"))
    thirdTurn = random.randint(0, countValues("turns"))
    while thirdTurn == secondTurn or thirdTurn == firstTurn:
        thirdTurn = random.randint(0, countValues("turns"))
    return firstTurn, secondTurn, thirdTurn

# prsnly, this could be optimized. this took 15 minutes alone lol
# Draws 5 random number points. Summed together, it equals 25. 
def getPersonality():
    points = []
    while True:
        sum = 0
        total = 25
        while total > 0:
            thru = random.randint(0,total)
            points.append(thru)
            total -= thru
        for x in range(len(points)):
            sum += points[x]
        if len(points) == 5 and sum == 25:
            break
        else:
            points = []
    return points

def main():
    global data
    global mainKeys
    random.seed()
    # open and load json file
    with open("listOfRandoms.json") as file:
        data = json.load(file)
    # get keys from json file
    mainKeys = getKeys(data)
    # Random choices block
    for key in mainKeys:
        # Specific turn ons and off block. 
        if key == "turns":
            firstTurn, secondTurn, thirdTurn = getTurns()
            print(f"1st Turn-On: {data[key][firstTurn]}\n2nd Turn-On: {data[key][secondTurn]}\nTurn-Off: {data[key][thirdTurn]}")
            continue
        # Specific personality block.
        if key == "personality":
            points = getPersonality()
            for x in random.sample(range(0,5), k=5):
                print(f"{data[key][x]}: {points[x]}")
            continue
        # Every other key block
        print(f"{key}: {data[key][random.randint(0, countValues(key))]}")


if __name__ == "__main__":
    main()