import flet as ft
import datetime
from banco import *
from util import *


def main(page: ft.Page):
    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Image(src="assets/logo.png", width=150, height=150),
            ft.Container(height=20),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                label="About Us",
                icon=ft.icons.PEOPLE,
                selected_icon_content=ft.Icon(ft.icons.PEOPLE),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.DEVELOPER_BOARD),
                label="Developers",
                selected_icon=ft.Icon(ft.icons.DEVELOPER_BOARD),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PERSON_SEARCH),
                label="Perfis Registrados",
                selected_icon=ft.icons.PERSON_SEARCH,
            ),
            ft.Divider(thickness=2)
        ],
    )
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Hello, world!"),
        action="Alright!",
    )


    def menu(e):
        page.drawer.open = True
        page.drawer.update()

    def acessar(e):
        def close_dlg_no(e):
            dlg_modal.open = False
            page.update()

        def close_dlg_yes(e):
            dlg_modal.open = False
            page.snack_bar = ft.SnackBar(ft.Text("Cadastro Realizado com Sucesso"))
            page.snack_bar.open = True
            page.update()

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Por Favor Confirme"),
            content=ft.Text("Não Nenhum Erro nos Cadastro?"),
            actions=[
                ft.TextButton("Não", on_click=close_dlg_no),
                ft.TextButton("Sim", on_click=close_dlg_yes),
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        def cadastrar(e):
            if not Validacao.validarNome(nome.value):
                nome.error_text = "Preencha o Campo Nome Adequadamente"
            if not Validacao.validarCPF(cpf.value):
                cpf.error_text = "Preencha o Campo CPF Adequadamente"
            if not Validacao.validarRG(rg.value):
                rg.error_text = "Preencha o Campo RG Adequadamente"
            else:
                page.dialog = dlg_modal
                dlg_modal.open = True
            page.update()
        
        if user.value == "Admin123" and senha.value == "Admin123":
            page.clean()
            page.window_width = 1200
            page.window_height = 800
            
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
                border_radius=10,
                input_filter=ft.InputFilter(r"[0-9]")
                )
            rg = ft.TextField(
                label='RG',
                focused_border_color=ft.colors.BLACK,
                value='',
                width=300,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.WHITE,
                border_radius=10,
                input_filter=ft.InputFilter(r"[0-9]")
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
                border_radius=10,
                input_filter=ft.InputFilter(r"[0-9]")
                )
            sexo = ft.Dropdown(
                hint_text='Sexo',
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
            # Criar date_picker_nasc
            date_picker = ft.DatePicker(
                first_date=datetime.datetime(2023, 10, 1),
                last_date=datetime.datetime(2024, 10, 1),
            )
            data_field = ft.TextField(
                hint_text='Data',
                read_only=True,
                focused_border_color=ft.colors.BLACK,
                value='',
                width=240,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.WHITE,
                border_radius=10
                )
            data_bnt = ft.IconButton(
                icon=ft.icons.CALENDAR_MONTH,
                icon_color=ft.colors.WHITE,
                height=50,
                width=50,
                on_click=lambda _: date_picker.pick_date()  # Criar uma função
                )
            data_nasc_field = ft.TextField(
                hint_text='Data de Nascimento',
                read_only=True,
                focused_border_color=ft.colors.BLACK,
                value='',
                width=240,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.WHITE,
                border_radius=10
                )
            data_nasc_bnt = ft.IconButton(
                icon=ft.icons.CALENDAR_MONTH,
                icon_color=ft.colors.WHITE,
                height=50,
                width=50,
                on_click=lambda _: date_picker.pick_date()
                )
            page.overlay.append(date_picker)
            naturalidade = ft.Dropdown(
                hint_text='Naturalidade',
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
                hint_text='Endereço',
                read_only=True,
                focused_border_color=ft.colors.BLACK,
                value='',
                width=240,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.WHITE,
                border_radius=10
                )
            endereco_bnt = ft.IconButton(
                icon=ft.icons.MAP,
                height=50,
                width=50,
                icon_color=ft.colors.WHITE
            )
            valor_colaborar = ft.TextField(
                label='Com Qual Valor Pode Colaborar',
                focused_border_color=ft.colors.BLACK,
                value='',
                width=300,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.WHITE,
                border_radius=10,
                input_filter=ft.InputFilter(r"[0-9]")
                )
            empresa_trabalha = ft.TextField(
                hint_text='Nome da Empresa em que Trabalha',
                focused_border_color=ft.colors.BLACK,
                value='',
                width=300,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.WHITE,
                border_radius=10
                )
            endereco_empresa_trabalha = ft.TextField(
                hint_text='Endereço Empresa em que Trabalha',
                read_only=True,
                focused_border_color=ft.colors.BLACK,
                value='',
                width=240,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.WHITE,
                border_radius=10
                )
            endereco_empresa_trabalha_bnt = ft.IconButton(
                icon=ft.icons.MAP,
                height=50,
                width=50,
                icon_color=ft.colors.WHITE
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
                        ft.IconButton(ft.icons.MENU, icon_color=ft.colors.WHITE, on_click=menu)
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
                        data_field,
                        data_bnt,
                        data_nasc_field,
                        data_nasc_bnt],
                        alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(
                        [naturalidade,
                        endereco,
                        endereco_bnt,
                        valor_colaborar], 
                        alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(
                        [empresa_trabalha,
                        endereco_empresa_trabalha,
                        endereco_empresa_trabalha_bnt,
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
        else:
            user.error_text = "Usuário ou Senha Invalido"
            senha.error_text = "Usuário ou Senha Invalido"
        page.update()
        

    page.title = "SISTEMA DE CADASTRO | ASSOCIAÇÃO MATO-GROSSENSE PROTETORA DOS ANIMAIS (APAM)"
    # page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.INDIGO_900
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # label_style_color = ft.TextStyle(color=ft.colors.BLACK87)
    page.window_height = 400
    page.window_width = 400
    page.scroll = 'auto'

    # Campos
    user = ft.TextField(
        label='Nome de Usuário',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.LEFT,
        color=ft.colors.WHITE, border_radius=10,
        autofocus=True
        )
    senha = ft.TextField(
        label='Senha',
        focused_border_color=ft.colors.BLACK,
        value='',
        width=300,
        text_align=ft.TextAlign.LEFT,
        color=ft.colors.WHITE, border_radius=10,
        password=True,
        can_reveal_password=True
        )

    page.add(
        ft.Image(src="assets/logo.png", width=120, height=120),
        ft.Container(height=20),
        ft.Row([
            ft.Column(
                [user,
                senha,
                ft.ElevatedButton(text='Acessar', on_click=acessar, width=300, height=40, color=ft.colors.WHITE)],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )
ft.app(target=main)
    