from PIL import Image
import os

# Function to check if a file exists
def file_exists(file_path):
    return os.path.exists(file_path)

# Creating an Image Object
image_path = 'C:/Users/shova/Desktop/encrypted_image.png'

if not file_exists(image_path):
    print("Error: The specified image file does not exist.")
    exit()

enc_img = Image.open(image_path)

# Loading pixel values of the encrypted image, each entry is a pixel value, i.e., RGB values as a sublist
enc_pixelMap = enc_img.load()

# Creating an empty string for our hidden message
msg = ""
msg_index = 0

# Traversing through the pixel values
for row in range(enc_img.size[0]):
    for col in range(enc_img.size[1]):

        # Fetching the RGB value of a pixel to a sublist
        rgb_list = enc_pixelMap[row, col]
        r = rgb_list[0]  # R value

        if col == 0 and row == 0:
            # Extracting the length of the message from the top-left pixel
            msg_len = r
        elif msg_index < msg_len:
            # Extracting ASCII values of the message characters from subsequent pixels
            msg += chr(r)
            msg_index += 1

enc_img.close()

# Check if the message was successfully extracted
if msg:
    print("Hidden message extracted successfully:\n\n")
    print(msg)
else:
    print("Error: No hidden message found in the provided image.")     