import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from PIL import ImageTk, Image
from banco import RegistrationSystem

class VisualizarPerfil(tk.Toplevel):
    def __init__(self, master=None, user_id=None):
        super().__init__(master)
        self.title(f"Perfil colaborador - APAM")
        self.geometry('1000x600')
        self.configure(background="#feffff")
        self.user_id = user_id
        self.registration_system = RegistrationSystem()
        self.create_widgets()
        self.load_user_data()

    def create_widgets(self):
        # Frame superior
        self.frame_logo = tk.Frame(self, width=1200, height=70, bg="#003452")
        self.frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=tk.NSEW, columnspan=5)

        # Logo
        self.app_lg = Image.open('assets/logo.png')
        self.app_lg = self.app_lg.resize((65, 65))
        self.app_lg = ImageTk.PhotoImage(self.app_lg)
        self.app_logo = tk.Label(self.frame_logo, image=self.app_lg, text="APAM - Associação Mato-Grossense Protetora dos Animais", width=1200, compound=tk.LEFT, anchor=tk.NW, font=('Verdana 15'), bg="#003452", fg="#feffff", padx=20)
        self.app_logo.place(x=5, y=0)

        # Frame de detalhes
        self.frame_detalhes = tk.Frame(self, width=885, height=460, bg="#feffff", relief=tk.SOLID)
        self.frame_detalhes.grid(row=1, column=0, pady=10, padx=10, sticky=tk.NSEW, columnspan=5)

        # Campos de detalhes
        self.create_detail_fields()

    def create_detail_fields(self):
        labels = [
            ("NOME", 4, 10, 100),
            ("CPF", 4, 60, 20),
            ("RG", 197, 60, 20),
            ("DATA NASC.", 393, 60, 15),
            ("ESTADO CIVIL", 558, 60, 20),
            ("SEXO", 745, 60, 7),
            ("TELEFONE FIXO", 4, 109, 20),
            ("TELEFONE MÓVEL", 197, 109, 20),
            ("EMAIL", 393, 109, 30),
            ("NATURALIDADE", 665, 109, 17),
            ("ENDEREÇO", 4, 159, 44),
            ("PROFISSÃO", 393, 159, 30),
            ("NOME DA EMPRESA", 4, 209, 44),
            ("ENDEREÇO DA EMPRESA", 393, 209, 30),
            ("TELEFONE EMPRESA", 665, 209, 17),
            ("DATA REGISTRO", 665, 159, 17),
            ("EM QUE PODE AJUDAR APAM", 4, 259, 48, "scrolledtext"),
            ("EXPECTATIVA TRABALHO VOLUNTÁRIO", 430, 259, 46, "scrolledtext"),
            ("VALOR COLABORAR", 234, 345, 20),
            ("OUTRAS FORMAS DE AJUDAR APAM", 430, 345, 46, "scrolledtext")
        ]

        self.fields = {}

        for label in labels:
            l = tk.Label(self.frame_detalhes, text=label[0], height=1, anchor=tk.NW, font=('Ivy 10'), bg="#feffff", fg="#403d3d")
            l.place(x=label[1], y=label[2])
            if len(label) == 4:
                val = tk.Label(self.frame_detalhes, text="", width=label[3], anchor=tk.W, bg="#e5e5e5", relief=tk.SOLID)
                val.place(x=label[1], y=label[2] + 25)
                self.fields[label[0].replace(" ", "_").lower()] = val
            elif len(label) == 5 and label[4] == "scrolledtext":
                val = scrolledtext.ScrolledText(self.frame_detalhes, width=label[3], height=3, wrap=tk.WORD, state=tk.DISABLED, bg="#e5e5e5")
                val.place(x=label[1], y=label[2] + 25)
                self.fields[label[0].replace(" ", "_").lower()] = val

        # Image placeholder
        self.canvas = tk.Canvas(self.frame_detalhes, width=110, height=110, bg="#e5e5e5", relief=tk.SOLID)
        self.canvas.place(x=4, y=343)

    def load_user_data(self):
        user_data = self.registration_system.search_apam(self.user_id)
        print(f"User Data: {user_data}")  # Adicionando depuração para ver os dados do usuário
        if user_data:
            fields = {
                "nome": user_data[3],
                "cpf": user_data[4],
                "rg": user_data[5],
                "data_nasc.": user_data[6],
                "estado_civil": user_data[9],
                "sexo": user_data[7],
                "telefone_fixo": user_data[11],
                "telefone_móvel": user_data[12],
                "email": user_data[2],
                "naturalidade": user_data[8],
                "endereço": user_data[10],
                "profissão": user_data[16],
                "nome_da_empresa": user_data[13],
                "endereço_da_empresa": user_data[14],
                "telefone_empresa": user_data[15],
                "data_registro": user_data[1],
                "em_que_pode_ajudar_apam": user_data[18],
                "expectativa_trabalho_voluntário": user_data[20],
                "valor_colaborar": user_data[17],
                "outras_formas_de_ajudar_apam": user_data[19]
            }

            for field_name, value in fields.items():
                field = self.fields.get(field_name)
                print(f"Setting field {field_name} to {value}")  # Depuração para verificar os valores dos campos
                if isinstance(field, scrolledtext.ScrolledText):
                    field.config(state=tk.NORMAL)
                    field.insert(tk.END, value)
                    field.config(state=tk.DISABLED)
                elif field:
                    field.config(text=value)

#             # Carregar e exibir a imagem do perfil
#             try:
#                 image_path = user_data[21]  # Certifique-se de que o caminho da imagem está correto
#                 self.image = Image.open(image_path)
#                 self.image = self.image.resize((110, 110), Image.Resampling.LANCZOS)
#                 self.image = ImageTk.PhotoImage(self.image)
#                 self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
#             except Exception as e:
#                 print(f"Erro ao carregar a imagem: {e}")
#                 self.canvas.create_text(55, 55, text="Sem foto", fill="black")
