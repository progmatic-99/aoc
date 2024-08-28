from typing import TypedDict

dict_name = None
SEEDS = None
seed_soil = {}
soil_fert = {}
fert_water = {}
water_light = {}
light_temp = {}
temp_humid = {}
humid_loca = {}


def make_dict(val: int, key: int, rng: int, conv_dict: TypedDict):
    for i in range(0, rng+1):
        conv_dict[key+i] = val
        val += 1


with open("test", "r") as f:
    for line_no, line in enumerate(f.readlines()):
        if line_no == 0:
            nums = line.split(":")[-1].strip()
            seeds = nums.split(" ")
            SEEDS = seeds
            continue
        if line_no == 2:
            dict_name = seed_soil
        if line_no == 51:
            dict_name = soil_fert
        if line_no == 81:
            dict_name = fert_water
        if line_no == 127:
            dict_name = water_light
        if line_no == 138:
            dict_name = light_temp
        if line_no == 172:
            dict_name = temp_humid
        if line_no == 210:
            dict_name = humid_loca

        if line.strip() and line_no not in [0,2,51,81,127,138,172,210]:
            val, key, rng = line.split(" ")
            make_dict(int(val), int(key), int(rng), dict_name)

locations = []
for seed in SEEDS:
    soil = seed_soil.get(seed, seed) 
    fert = soil_fert.get(soil, soil)
    water = fert_water.get(fert, fert)
    light = water_light.get(water, water)
    temp = light_temp.get(light, light)
    humid = temp_humid.get(temp, temp)
    loca = humid_loca.get(humid, humid)

    locations.append(int(loca))

locations.sort()
print(locations[0])
