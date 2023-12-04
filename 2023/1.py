sum = 0

with open("puzzle.txt", "r") as f:
    for line in f.readlines():
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

        if len(calibrated_value) > 0:
            sum += int(calibrated_value)

print(sum)
