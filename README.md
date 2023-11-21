# messagehiding
Steganography is the hiding of a secret message within an ordinary message and the extraction of it at its destination. Here we use an image to hide the textual message.
REQUIREMENTS

PIL package of python is neccessay to run the program. The instruction to install PIL is given below:

--->>> pip install pillow

pip is python package installer, it must be install first although its preinstalled in many Linux Distributions.

--->>> sudo apt-get install python-pip

orginal_image is the carrier image.

encrypted_image is the carrier image with hidden data, also this is the image which we transmit via network.

Here program encoder is ran, and the user is asked enter the message that is to be transmitted and at reciver's end decoder program will print the hidden message to the user's terminal.
