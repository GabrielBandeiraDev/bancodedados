import flet as ft
from banco import *
from util import *


def main(page: ft.Page):
    def cadastrar(e):
        if not Validacao.validarNome(nome.value):
            nome.error_text = "Preencha o Campo Nome Adequadamente"
        if not Validacao.validarCPF(cpf.value):
            cpf.error_text = "Preencha o Campo CPF Adequadamente"
        if not Validacao.validarRG(rg.value):
            rg.error_text = "Preencha o Campo RG Adequadamente"
        page.update()

    
    page.title = "SISTEMA DE CADASTRO | ASSOCIAÇÃO MATO-GROSSENSE PROTETORA DOS ANIMAIS (APAM)"
    # page.bgcolor = '#feffff'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # label_style_color = ft.TextStyle(color=ft.colors.BLACK87)
    page.scroll = 'auto'

    # Campos
    nome = ft.TextField(
        label='Nome completo',
        focused_border_color=ft.colors.BLACK,
        value='', 
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE, border_radius=10,
        autofocus=True
        )
    cpf = ft.TextField(
        label='CPF',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300, 
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    rg = ft.TextField(
        label='RG',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    email = ft.TextField(
        label='Email',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    estado_civil = ft.Dropdown(
        label='Estado Civil',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        color=ft.colors.WHITE,
        border_radius=10,
        options=[
            ft.dropdown.Option('Solteiro(a)'),
            ft.dropdown.Option('Casado(a)'),
            ft.dropdown.Option('Divorciado(a)'),
            ft.dropdown.Option('Viúvo(a)'),
            ft.dropdown.Option('Outro')
        ])
    celular = ft.TextField(
        label='Telefone Celular',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    sexo = ft.Dropdown(
        label='Sexo',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        color=ft.colors.WHITE,
        border_radius=10,
        options=[
            ft.dropdown.Option('M'),
            ft.dropdown.Option('F'),
            ft.dropdown.Option('Prefiro Não Responder')
        ])
    # Pesq como trabalhar com datas no flet
    data = ft.TextField(
        label='Data',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    data_nasc = ft.TextField(
        label='Data de Nascimento',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    naturalidade = ft.Dropdown(
        label='Naturalidade',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        color=ft.colors.WHITE,
        border_radius=10,
        options=[
        ft.dropdown.Option('AC'),
        ft.dropdown.Option('AL'),
        ft.dropdown.Option('AM'),
        ft.dropdown.Option('AP'),
        ft.dropdown.Option('BA'),
        ft.dropdown.Option('CE'),
        ft.dropdown.Option('DF'),
        ft.dropdown.Option('ES'),
        ft.dropdown.Option('GO'),
        ft.dropdown.Option('MA'),
        ft.dropdown.Option('MG'),
        ft.dropdown.Option('MS'),
        ft.dropdown.Option('MT'),
        ft.dropdown.Option('PA'),
        ft.dropdown.Option('PB'),
        ft.dropdown.Option('PE'),
        ft.dropdown.Option('PI'),
        ft.dropdown.Option('PR'),
        ft.dropdown.Option('RJ'),
        ft.dropdown.Option('RN'),
        ft.dropdown.Option('RO'),
        ft.dropdown.Option('RR'),
        ft.dropdown.Option('RS'),
        ft.dropdown.Option('SC'),
        ft.dropdown.Option('SE'),
        ft.dropdown.Option('SP'),
        ft.dropdown.Option('TO')
    ])
    # Botão para escolher no mapa, google maps API
    endereco = ft.TextField(
        label='Endereço',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10)
    valor_colaborar = ft.TextField(
        label='Com Qual Valor Pode Colaborar',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    empresa_trabalha = ft.TextField(
        label='Nome da Empresa em que Trabalha',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    endereco_empresa_trabalha = ft.TextField(
        label='Endereço Empresa em que Trabalha',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    profisao = ft.TextField(
        label='Profissão',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    ajudar_APAM = ft.TextField(
        label='Como Pode Ajuar a APAM?',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=920,
        text_align=ft.TextAlign.LEFT,
        color=ft.colors.WHITE,
        border_radius=10,
        multiline=True,
        max_lines=5,
        min_lines=1,
        max_length=500
        )
    outras_ajudas = ft.TextField(
        label='Outras Formas de Ajudar a APAM',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=920,
        text_align=ft.TextAlign.LEFT,
        color=ft.colors.WHITE,
        border_radius=10,
        multiline=True,
        max_lines=5,
        min_lines=1,
        max_length=500
        )
    expectativas = ft.TextField(
        label='Quais São Suas Expectativas com Relação ao Trabalho Voluntario',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=920,
        text_align=ft.TextAlign.LEFT,
        color=ft.colors.WHITE,
        border_radius=10,
        multiline=True,
        max_lines=5,
        min_lines=1,
        max_length=500
        )

    page.add(
        ft.Column([
            ft.Row([
                ft.IconButton(ft.icons.MENU, icon_color=ft.colors.WHITE)
            ], alignment=ft.MainAxisAlignment.START)
        ]),
        ft.Column([
            ft.Row(
                [nome,
                cpf,
                rg],
                alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(
                [email,
                estado_civil,
                celular], 
                alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(
                [sexo,
                 data,
                 data_nasc],
                alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(
                [naturalidade,
                 endereco,
                 valor_colaborar], 
                alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(
                [empresa_trabalha,
                 endereco_empresa_trabalha,
                 profisao], 
                alignment=ft.MainAxisAlignment.CENTER),
            
            ft.Container(height=30),
            
            ft.Column([
                ft.Row(
                    [ajudar_APAM],
                    alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    [outras_ajudas],
                    alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    [expectativas],
                    alignment=ft.MainAxisAlignment.CENTER)
            ])
        ]),
        
        ft.Container(height=30),
        
        ft.Column([
            ft.Row([
                ft.ElevatedButton(text='Cadastrar', on_click=cadastrar, width=300, height=40, color=ft.colors.WHITE)
                ], alignment=ft.MainAxisAlignment.END)
        ])
    )

ft.app(target=main)
