from PIL import Image, ImageDraw, ImageFont

class PageTwo:
    def __init__(self):
        self.image_path = "/home/simon/PycharmProjects/orcamentoAupetitoso/lib/2.png"
        self.output_path = "/home/simon/PycharmProjects/orcamentoAupetitoso/data/2.png"

    def main(self):
        image = Image.open(self.image_path)
        image.save(self.output_path)
        print(f"Image saved at {self.output_path}")


if __name__ == "__main__":
    PageTwo().main()