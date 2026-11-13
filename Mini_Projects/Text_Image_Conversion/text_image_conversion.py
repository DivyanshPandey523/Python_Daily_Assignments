# Mini Project: Text and Image Conversion
# Install Pillow before running:
# pip install pillow
#
# This program saves typed text as an image.
# It can also convert an image into simple ASCII text.

from PIL import Image, ImageDraw, ImageFont

# Part 1: Save typed text as an image
text = input("Enter a short text: ")

image = Image.new("RGB", (600, 200), "white")
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

draw.text((20, 80), text, fill="black", font=font)
image.save("text_image.png")

print("Text image saved as text_image.png")


# Part 2: Convert an image into ASCII text
image_path = input("Enter image file path for ASCII conversion: ")

try:
    picture = Image.open(image_path).convert("L")

    new_width = 60
    new_height = max(1, int(picture.height * new_width / picture.width / 2))
    picture = picture.resize((new_width, new_height))

    characters = "@%#*+=-:. "
    pixels = picture.getdata()
    ascii_text = ""

    for index, pixel in enumerate(pixels):
        character_index = pixel * (len(characters) - 1) // 255
        ascii_text = ascii_text + characters[character_index]

        if (index + 1) % new_width == 0:
            ascii_text = ascii_text + "\n"

    with open("image_as_text.txt", "w", encoding="utf-8") as file:
        file.write(ascii_text)

    print("ASCII text saved as image_as_text.txt")

except FileNotFoundError:
    print("Image file not found. Please check the file path.")
except Exception as error:
    print("Something went wrong:", error)
