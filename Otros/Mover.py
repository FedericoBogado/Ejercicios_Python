from PIL import Image
import os


def run():
    downloads_folder = "C:/Users/dakra/BrawlhallaRenders/"
    pictures_folder = "E:/Youtube/Imagenes/"

    for filename in os.listdir(downloads_folder):
        name, extension = os.path.splitext(downloads_folder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloads_folder + filename)
            picture.save(pictures_folder + "compressed_" + filename, optimize=True, quality=60)
            os.remove(downloads_folder + filename)
            print(name + ":" + extension)


if __name__ == "__main__":
    run()