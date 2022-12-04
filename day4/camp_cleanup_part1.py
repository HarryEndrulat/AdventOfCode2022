def main():
    file = open("input.txt")
    output = 0
    for line in file.readlines():
        line = line.strip()
        elf1, elf2 = line.split(",")
        elf1Start, elf1End = elf1.split("-")
        elf2Start, elf2End = elf2.split("-")
        elf1Start, elf1End, elf2Start, elf2End = int(elf1Start), int(elf1End), int(elf2Start), int(elf2End)
        if (elf1Start >= elf2Start and elf1End <= elf2End) or (elf2Start >= elf1Start and elf2End <= elf1End):
            output += 1
    return output


print(main())
