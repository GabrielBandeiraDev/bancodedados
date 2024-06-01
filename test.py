import flet as ft

def main(page: ft.Page):
    test = ft.InputFilter(regex_string=r"[0-9]")
    a = ft.TextField(
        hint_text='+# (###) ###-##-##',
        input_filter=test
    )

    page.add(a)

ft.app(target=main)
