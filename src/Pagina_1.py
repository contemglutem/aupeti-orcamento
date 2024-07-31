from PIL import Image, ImageDraw, ImageFont

class PageOne:
    def __init__(self):
        self.image_path = "/home/simon/PycharmProjects/orcamentoAupetitoso/lib/1.png"
        self.font_path = "/home/simon/PycharmProjects/orcamentoAupetitoso/letter_font/honey_crepes/Honey Crepes.ttf"
        self.output_path = "/home/simon/PycharmProjects/orcamentoAupetitoso/data/1.png"
        self.font_size = 42

        self.nome = "Nala"
        self.peso = "13"
        self.tutor = "Carol"

    def main(self):
        font = ImageFont.truetype(self.font_path, self.font_size)
        image = Image.open(self.image_path)
        draw = ImageDraw.Draw(image)

        # Define positions for the text (x, y)
        nome_position = (200, 130)   # Adjust these positions as needed
        peso_position = (200, 210)
        tutor_position = (200, 280)

        # Add text to the image
        draw.text(nome_position, f"{self.nome}", font=font, fill="white")
        draw.text(peso_position, f"{self.peso} kg", font=font, fill="white")
        draw.text(tutor_position, f"{self.tutor}", font=font, fill="white")

        # Save the edited image
        image.save(self.output_path)

        print(f"Image saved at {self.output_path}")


if __name__ == "__main__":
    PageOne().main()
