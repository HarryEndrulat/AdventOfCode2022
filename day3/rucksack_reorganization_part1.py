
def main():
    file = open("input.txt")
    output = 0
    for line in file.readlines():
        line = line.strip()
        n = len(line)
        half = int(n / 2)
        firstHalf = line[:half]
        secondHalf = line[half:]
        firstHalfDict = {}
        secondHalfDict = {}
        i = 0
        while i < n / 2:
            firstHalfDict[firstHalf[i]] = firstHalfDict.get(firstHalf[i], 0) + 1
            secondHalfDict[secondHalf[i]] = secondHalfDict.get(secondHalf[i], 0) + 1
            i += 1
        for key in firstHalfDict.keys():
            if key in secondHalfDict.keys():
                if key.isupper():
                    output += ord(key) - 38
                    break
                else:
                    output += ord(key) - 96
                    break
    return output



print(main())
