import flet as ft
import random

def main(page: ft.Page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    start_image = ft.Image(
        src = "images/dice.png",
        width = 300,
        height = 300,
    )

    def change_image(e):
        images = [
            "images/die1.png",
            "images/die2.png",
            "images/die3.png",
            "images/die4.png",
            "images/die5.png",
            "images/die6.png"
        ]
        start_image.src = random.choice(images)
        page.update()

    change_button = ft.Button(
        content = ft.Text("Click to roll the dice!"),
        on_click = change_image
    )

    page.add(start_image, change_button)
ft.run(main, assets_dir = "assets")