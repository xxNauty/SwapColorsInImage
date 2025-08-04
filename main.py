from PIL import Image
from itertools import permutations

def blur() -> None:
    input_image = Image.open("input/input.jpg")
    input_pixel_map = input_image.load()

    width, height = input_image.size
    mode = input_image.mode

    output_image = Image.new(mode, (width, height))
    output_pixel_map = output_image.load()

    values = ['r', 'g', 'b']

    for permutation in list(permutations(values)):
        for i in range(width):
            for j in range(height):
                r, g, b = input_pixel_map[i, j]

                color_values = {
                    'r': r,
                    'g': g,
                    'b': b
                }

                r_value = color_values[permutation[0]]
                g_value = color_values[permutation[1]]
                b_value = color_values[permutation[2]]

                # print(permutation[0] + permutation[1] + permutation[2])
                # print(color_values[permutation[0]] + color_values[permutation[1]] + color_values[permutation[2]])

                output_pixel_map[i, j] = (r_value, g_value, b_value)

        colors = permutation[0] + permutation[1] + permutation[2]
        filename = colors if colors != "rgb" else "input"
        output_image.save("output/" + filename + ".jpg", format="jpeg")

blur()
