input = [6, 6, 4]
length = input[0] ; width = input[1] ; tile = input[2]
tile_length = int(length / tile)
if length % tile != 0:
     tile_length += 1  
tile_width = int(width / tile)
if width % tile != 0:
    tile_width += 1
tile_number = tile_length * tile_width
print(tile_number)
