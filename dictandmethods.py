# Dictionary are mutable

# this will an empty dictionary
a1 = {}

marksDict = {"john": 23, "jimmy": 100, "fred": 10, "jim": 40}
print(marksDict["john"])

# dictionary are mutable
marksDict['alan'] = 89
print(marksDict)

# this will prevent from showing error incase the key is not present
print(marksDict.get('alan'))

print(marksDict.keys())
