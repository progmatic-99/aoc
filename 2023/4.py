POINTS = []

with open("puzzle-4.txt", "r") as f:
    for line in f.readlines():
        game, nums = line.split(":")
        game_no = int(game.split(" ")[-1])
        winning_str, my_str = nums.split("|")
        winning_nums = winning_str.strip().split(" ")
        my_nums = my_str.strip().split(" ")

        pts = 0
        for i in my_nums:
            if i in winning_nums and i.isnumeric():
                pts += 1

        cnt = POINTS.count(game_no)
        while cnt:
            for i in range(1, pts+1):
                POINTS.append(game_no + i)
            cnt -= 1

        for i in range(0, pts+1):
            POINTS.append(game_no + i)

print(POINTS)
print(len(POINTS))

