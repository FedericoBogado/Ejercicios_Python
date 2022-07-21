from PIL import Image
import os


def run():
    downloads_folder = "C:/Users/dakra/Downloads/"

    for filename in os.listdir(downloads_folder):
        name, extension = os.path.splitext(downloads_folder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloads_folder + filename)
            picture.save(downloads_folder + "compressed_" + filename, optimize=True, quality=60)


if __name__ == "__main__":
    run()