name = input()
mapdict = {'é': 'e', 'ë': 'e', 'á': 'a', "å": "a", "œ": "oe", "æ": "ae"}
newmap = name.maketrans(mapdict)
newstr = name.translate(newmap)
print(newstr)
