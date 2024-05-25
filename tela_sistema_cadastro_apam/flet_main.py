import flet as ft
from banco import *


def main(page: ft.Page):
    page.title = "SISTEMA DE CADASTRO | ASSOCIAÇÃO MATO-GROSSENSE PROTETORA DOS ANIMAIS (APAM)"
    # page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # label_style_color = ft.TextStyle(color=ft.colors.BLACK87)
    page.scroll = 'auto'
    page.add(
        ft.Column([
            ft.Row([
                ft.IconButton(ft.icons.MENU, icon_color=ft.colors.WHITE)
            ], alignment=ft.MainAxisAlignment.START)
        ]),
        ft.Column([
            ft.Row([
                ft.TextField(label='Nome completo', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10, autofocus=True),
                ft.TextField(label='CPF', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10),
                ft.TextField(label='RG', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10)
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.TextField(label='Email', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10),
                ft.TextField(label='Estado Civil', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10),
                ft.TextField(label='telefone Celular', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10)
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.TextField(label='Sexo', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10),
                ft.TextField(label='Data', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10),
                ft.TextField(label='Data de Nascimento', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10)
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.TextField(label='Naturalidade', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10),
                ft.TextField(label='Endereço', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10),
                ft.TextField(label='Com Qual Valor Pode Colaborar', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10)
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.TextField(label='Nome da Empresa em que Trabalha', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10),
                ft.TextField(label='Endereço Empresa em que Trabalha', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10),
                ft.TextField(label='Profissão', focused_border_color=ft.colors.BLACK, value='', width=300, height=40, text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE, border_radius=10)
            ], alignment=ft.MainAxisAlignment.CENTER),
            
            ft.Container(height=30),
            
            ft.Column([
                ft.Row([
                    ft.TextField(label='Profissão', focused_border_color=ft.colors.BLACK, value='', width=920,
                             text_align=ft.TextAlign.LEFT, color=ft.colors.WHITE, border_radius=10, multiline=True,
                             max_lines=3, min_lines=1, max_length=500)
                    ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.TextField(label='Profissão', focused_border_color=ft.colors.BLACK, value='', width=920,
                             text_align=ft.TextAlign.LEFT, color=ft.colors.WHITE, border_radius=10, multiline=True,
                             max_lines=3, min_lines=1, max_length=500)
                    ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.TextField(label='Profissão', focused_border_color=ft.colors.BLACK, value='', width=920,
                             text_align=ft.TextAlign.LEFT, color=ft.colors.WHITE, border_radius=10, multiline=True,
                             max_lines=3, min_lines=1, max_length=500)
                    ], alignment=ft.MainAxisAlignment.CENTER)
            ])
        ]),
        
        ft.Container(height=30),
        
        ft.Column([
            ft.Row([
                ft.ElevatedButton(text='Cadastrar', on_click=lambda _: cadastrar_usuario(page), width=300, height=40, color=ft.colors.WHITE)
                ], alignment=ft.MainAxisAlignment.END)
        ])
    )

ft.app(target=main)


# ft.TextField(
#     label="Auto adjusted height with max lines",
#     multiline=True,
#     min_lines=1,
#     max_lines=3,
# )