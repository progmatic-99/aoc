balls = {
        "red": "12",
        "green": "13",
        "blue": "14"
}
ans = 0

with open("puzzle-2.txt", "r") as input_file:
    for line in input_file.readlines():
        game_no, sets = line.split(":")
        _, game_id = game_no.split(" ")
        games = sets.split(";")
        print(games)
        red, green, blue = 0, 0, 0
        for game in games:
            g = game.split(",")
            for i in g:
                i = i.strip()
                num, color = i.split(" ")
                num = int(num)
                if color == "red":
                    red = max(red, num)
                elif color == "green":
                    green = max(green, num)
                else:
                    blue = max(blue, num)
        print(red, green, blue)
        ans += (red * green * blue)

print(ans)
