
def main():
    elfArray = [0]
    currentElf = 0
    output = [0, 0, 0]
    file = open("day1/input.txt")
    for i, line in enumerate(file):

        if line.strip() == "":
            if currentElf == 0:
                output[0] = elfArray[currentElf]
                output.sort
            currentElf += 1
            elfArray.append(0)
        else:
            elfArray[currentElf] += int(line)
        if len(elfArray) > 1:
            for j, elf in enumerate(output):
                if elf < elfArray[currentElf]:
                    output[j] = elfArray[currentElf]
                    output.sort()
                    break
    value = 0
    for out in output:
        value += out
        print(value)

    return output


if __name__ == "__main__":
    output = main()
    print(output)
