# importing bare minimum to save time
from PIL import Image
from csv import writer
from glob import glob
from os import getcwd
import sys

# lowering the resolution by value of "step"
step = 10
name = "face_vector_"

if __name__ == "__main__":
    path = getcwd()
    dir = str(sys.argv[1])

    # file where the vectors are stored
    filename = "Vectors.csv"

    if len(sys.argv) == 3:
        filename = str(sys.argv[2])

    file = open(filename, "w")
    csvWriter = writer(file)

    print("current working directory: {}".format(path + "\\" + dir))
    print("Output format: Name, Width, Height, Reduced, ...Data...\n")

    # list of all .png files in the directory
    files = glob(path + "\\" + dir + "\\*.png")

    for i in range(len(files)):
        print("working on: {}".format(files[i]))
        img = Image.open(files[i])
        bw_vector = []
        for x in range(0, img.size[0], step):
            for y in range(0, img.size[1], step):
                # monochrome value computed by averaging RGB
                try:
                    bw_value = round(sum(img.getpixel((x, y)))/768, 3)
                except TypeError:
                    # in case pixel is already black and white
                    bw_value = img.getpixel((x, y))/256
                # adding value to vector
                bw_vector.append(bw_value)

        csvWriter.writerow([name + str(i), img.size[0], img.size[1], step] + bw_vector)
        img.close()

    print("\nData saved in {}".format(filename))
    file.close()

