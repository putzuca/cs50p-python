from PIL import Image, ImageFilter


def main():
    with Image.open("Tsunami_by_hokusai_19th_century.jpg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpg")
main()