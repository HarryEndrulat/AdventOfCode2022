
def main():
    file = open("input.txt")
    output = 0
    for line in file.readlines():
        line = line.strip()
        elf1, elf2 = line.split(",")
        elf1Start, elf1End = elf1.split("-")
        elf2Start, elf2End = elf2.split("-")
        elf1Start, elf1End, elf2Start, elf2End = int(elf1Start), int(elf1End), int(elf2Start), int(elf2End)
        if (elf2Start<=elf1End and elf2End>=elf1Start) or (elf1Start<=elf2End and elf1End>=elf2Start):
            output += 1
    return output


print(main())
