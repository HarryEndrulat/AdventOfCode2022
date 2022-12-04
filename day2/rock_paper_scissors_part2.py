
def main():
    """
    A = rock
    B = paper
    C = scissors
    X = lose
    Y = tie
    Z = win
    """
    file = open("day2/input.txt")
    total = 0
    for line in file.readlines():
        line = line.strip()
        opponentPlay, myPlay = line.split(" ")
        match opponentPlay:
            case 'A':
                match myPlay:
                    case 'X':
                        total += 3
                    case 'Y':
                        total += 4
                    case 'Z':
                        total += 8
            case 'B':
                match myPlay:
                    case 'X':
                        total += 1
                    case 'Y':
                        total += 5
                    case 'Z':
                        total += 9
            case 'C':
                match myPlay:
                    case 'X':
                        total += 2
                    case 'Y':
                        total += 6
                    case 'Z':
                        total += 7
    return total


if __name__ == "__main__":
    output = main()
    print(output)
