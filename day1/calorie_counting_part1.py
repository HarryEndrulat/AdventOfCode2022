
def main():
    elfArray = [0]
    currentElf = 0
    output = 0
    #calorieCount = 0
    file = open("input.txt")
    for i, line in enumerate(file):
        if line.strip() == "":
            if currentElf == 0:
                output = elfArray[currentElf]
            currentElf += 1
            elfArray.append(0)
        else:
            elfArray[currentElf] += int(line)
        if len(elfArray) > 1 and elfArray[currentElf] > output:
            output = elfArray[currentElf]
    return output


if __name__ == "__main__":
    output = main()
