import colorgram

colors = colorgram.extract('image.jpg', 30)

color_list = []
for item in colors:

    rgb_list = list(item.rgb)
    rgb_tuple = tuple(rgb_list)
    color_list.append(rgb_tuple)

print(color_list)