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
        valid = True
        #first, second, third = sets.split(";")
        games = sets.split(";")
        for game in games:
            g = game.split(",")
            for i in g:
                i = i.strip()
                num, color = i.split(" ")
                if int(balls[color]) < int(num):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            ans += int(game_id)

print(ans)
