from numpy import empty, where

with open("input.txt", "r") as file:
    img_data = file.read()

WIDTH = 25
HEIGHT = 6

def get_layers(data):
    layers = []
    layer, count = empty((HEIGHT, WIDTH), dtype=str), {"0": 0, "1": 0, "2": 0}
    selected_layer, selected_count = None, {"0": WIDTH*HEIGHT, "1": 0, "2": 0}
    for index, pixel in enumerate(data):
        index = index - len(layers)*WIDTH*HEIGHT
        layer[index/WIDTH, index%WIDTH] = pixel
        count[pixel] += 1
        if index == WIDTH*HEIGHT-1:
            layers.append(layer)
            if selected_count["0"] > count["0"]:
                selected_count = count
                selected_layer = layer
            count, layer = {"0": 0, "1": 0, "2": 0}, empty((HEIGHT, WIDTH), dtype=str)
    return layers, selected_count

layers, selected_count = get_layers(img_data)
print("The result is : " + str(selected_count["1"] * selected_count["2"]))

# PART 2

BLACK = "0"
WHITE = "1"
TRANSPARENT = "2"

def render_layer(layer):
    stringified_pixels = ""
    for row in layer:
        for pixel in row:
            if pixel == BLACK:
                stringified_pixels += " "
            elif pixel == WHITE:
                stringified_pixels += "0"
        stringified_pixels += "\n"
    return stringified_pixels

final_layer = layers[0]
for layer in layers[1:]:
    final_layer = where(final_layer == TRANSPARENT, layer, final_layer)
print(render_layer(final_layer))