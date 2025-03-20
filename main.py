import flet as ft


def main(page: ft.Page):
    texto = ft.Text(
        value="Deploy com Framework Flet feito com sucesso",
        size=40,
        weight="bold",
    )

    page.add(texto)


ft.app(target=main)
