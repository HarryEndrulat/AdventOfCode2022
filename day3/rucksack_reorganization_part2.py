"""
if i mod 3 == 0 move next group
for each group:
    make a dictionary of each line
    find the keys dictionary 1 and 2 have in common and compare that set to dict 3 this ist quite as bad as n^2?
"""


def main():
    file = open("input.txt")
    output = 0
    firstDict = {}
    secondDict = {}
    thirdDict = {}
    i = 0
    for line in file.readlines():
        line = line.strip()
        n = len(line)
        j = 0
        while j < n:
            if i % 3 == 0:
                firstDict[line[j]] = firstDict.get(line[j], 0) + 1
            if i % 3 == 1:
                secondDict[line[j]] = secondDict.get(line[j], 0) + 1
            if i % 3 == 2:
                thirdDict[line[j]] = thirdDict.get(line[j], 0) + 1
            j += 1

        if i % 3 == 2:
            firstAndSecondDictKeys = []
            for key in firstDict.keys():
                if key in secondDict.keys():
                    firstAndSecondDictKeys.append(key)
            for key in firstAndSecondDictKeys:
                if key in thirdDict.keys():
                    if key.isupper():
                        output += ord(key) - 38
                        break
                    else:
                        output += ord(key) - 96
                        break
            firstDict = {}
            secondDict = {}
            thirdDict = {}
        i += 1
    return output


print(main())
