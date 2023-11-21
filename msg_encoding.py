from PIL import Image
import os

# Function to check if a file exists
def file_exists(file_path):
    return os.path.exists(file_path)

# Creating an image object
image_path = 'C:/Users/shova/Desktop/original_image.jpg'

if not file_exists(image_path):
    print("Error: The specified image file does not exist.")
    exit()

org_img = Image.open(image_path)

# Loading pixel values of the original image, each entry is pixel value, i.e., RGB values as a sublist
org_pixelMap = org_img.load()

# Creating a new image object with the image mode and dimensions as that of the original image
enc_img = Image.new(org_img.mode, org_img.size)
enc_pixelsMap = enc_img.load()

# Reading the message to be encrypted from the user
msg = input("Enter the message:\t")

if not msg:
    print("Error: Message cannot be empty.")
    exit()

msg_index = 0

# Finding the length of the message
msg_len = len(msg)

# Traversing through the pixel values
for row in range(org_img.size[0]):
    for col in range(org_img.size[1]):

        # Fetching RGB value of a pixel to sublist
        r, g, b = org_pixelMap[row, col]

        if row == 0 and col == 0:
            # Encoding the length of the message in the top-left pixel
            ascii_val = msg_len
            enc_pixelsMap[row, col] = (ascii_val, g, b)
        elif msg_index < msg_len:
            # Encoding ASCII values of the message characters in subsequent pixels
            char = msg[msg_index]
            ascii_val = ord(char)
            enc_pixelsMap[row, col] = (ascii_val, g, b)
            msg_index += 1
        else:
            # Copying the remaining pixels from the original image
            enc_pixelsMap[row, col] = (r, g, b)

org_img.close()

# Display the encrypted image
enc_img.show()

# Save the encrypted image
enc_img.save("C:/Users/shova/Desktop/encrypted_image.png")
enc_img.close()