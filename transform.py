from PIL import Image

image = Image.open("images.jpeg")

data = image.load()
print(image.width)
print(image.height)


def rotate_90(original_image):
    blank_image = Image.new("RGB", (original_image.height, original_image.width))
    blank_image_data = blank_image.load()
    original_data = original_image.load()

    for y in range(original_image.height):
        for x in range(original_image.width):
            pixel = original_data[x,y]
            blank_image_data[-y+original_image.height-1,x] = pixel
    
    return blank_image

def translate(original_image, dx, dy):
    blank_image = Image.new("RGB", (original_image.width + dx, original_image.height + dy))
    blank_image_data = blank_image.load()
    original_data = original_image.load()

    for y in range(original_image.height):
        for x in range(original_image.width):
            pixel = original_data[x,y]
            blank_image_data[x+dx,y+dy] = pixel
    
    return blank_image

def transform(original_image, a, b, c, d, e, f):
    blank_image = Image.new("RGB", (original_image.width , original_image.height))
    blank_image_data = blank_image.load()
    original_data = original_image.load()

    for y in range(original_image.height):
        for x in range(original_image.width):
            pixel = original_data[x,y]

            new_x = x * a + y * b + 1 * c
            new_y = x * d + y * e + 1 * f

            blank_image_data[new_x, new_y] = pixel
    
    return blank_image

image_rotate_90 = rotate_90(image)
image_rotate_90.save("rotate_90.png")

image_translate = translate(image, 200, 72)
image_translate.save("translate.png")

image_transform = transform(image, -1, 0, (image.width-1), 0, 1, 0)
image_transform.save("transform.png")


