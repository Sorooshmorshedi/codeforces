input = [
4,
'rgbBRG',
'RgbrBG',
'bBrRgG',
'rgRGBb'
]
x = 0
while x < input[0]:
    x += 1
    map = input[x]
    road = []
    for i in range(0, len(map)):
        if map[i] == map[i].lower():
            road.append(map[i])
        elif map[i] != map[i].lower():
            if map[i].lower() in road:
                road.append(map[i])
            else:
                print('No')
        if len(road) == 6:
            print('yes')
