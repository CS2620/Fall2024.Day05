from PIL import Image

image = Image.open("images.jpeg")

data = image.load()
print(image.width)
print(image.height)


def scale(original_image, amount):
    blank_image = Image.new("RGB", (int(original_image.width*amount), int(original_image.height*amount)))
    blank_image_data = blank_image.load()
    original_data = original_image.load()

    for y in range(blank_image.height):
        for x in range(blank_image.width):

            current_x = x
            current_y = y

            pixel = original_data[int(current_x/amount), int(current_y/amount)]

            blank_image_data[x,y] = pixel
    
    return blank_image



image_scale = scale(image, .1)
image_scale.save("scale.png")


