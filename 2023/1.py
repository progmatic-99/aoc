sum = 0
numbers = [
        ("zero", "0"),
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9")
]


def convert_to_number(line: str) -> str:
    for i in range(len(numbers)-1, 0, -1):
        idx = line.find(numbers[i][0])
        if idx != -1:
            ns = f"{numbers[i][0][0]}{numbers[i][1]}{numbers[i][0][-1]}"
            line = line.replace(numbers[i][0], ns)
 
    return line

print(convert_to_number("eighthree"))
print(convert_to_number("zoneight34"))

with open("1-part_2.txt", "r") as f:
    for line in f.readlines():
        line = convert_to_number(line)
        start = 0
        end = len(line) - 1
        calibrated_value = ""
        while True:
            if line[start].isnumeric():
                calibrated_value += line[start]
                break
            start += 1
        while True:
            if line[end].isnumeric():
                calibrated_value += line[end]
                break
            end -= 1

#        print(calibrated_value)
        if len(calibrated_value) > 0:
            sum += int(calibrated_value)

print(sum)
