import sys
import os
from PIL import Image, ImageOps

valid_extentions = [".png", ".jpg", ".jpeg"]

def validate_args():
    if len(sys.argv) > 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too mant command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_extentions:
        sys.exit("Invalid input file extension")
    if output_ext not in valid_extentions:
        sys.exit("invalid output file extension")
    if input_ext != output_ext:
        sys.exit("Input and output file have different extension")
    if not os.path.isfile(input_file):
        sys.exit("Input file does not exist")

    return input_file, output_file

def apply_shirt(input_file, output_file):
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("shirt.png not found")

    size = shirt.size  # (width, height)

    try:
        photo = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Could not open input image")

    # Resize & crop to match shirt's size
    photo = ImageOps.fit(photo, size)

    # Paste shirt on top, using shirt as mask for transparency
    photo.paste(shirt, shirt)

    # Save final image
    photo.save(output_file)


def main():
    input_file, output_file = validate_args()
    apply_shirt(input_file, output_file)

if __name__ == "__main__":
    main()
