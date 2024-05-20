import sqlite3
from tkinter import messagebox

class RegistrationSystem:
    def __init__(self):
        self.conn = sqlite3.connect('bancoapam.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS bancoapam
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            cpf TEXT,
                            matricula TEXT NOT NULL,
                            email TEXT NOT NULL,
                            telefone TEXT NOT NULL,
                            sexo TEXT NOT NULL,
                            data TEXT NOT NULL,
                            endereco TEXT NOT NULL,
                            temperamento TEXT NOT NULL,
                            imagem TEXT NOT NULL)''')
        self.conn.commit()

    def register_apam(self, apam):
        self.c.execute("INSERT INTO bancoapam(name, cpf, data, email, endereco, matricula, telefone, sexo, temperamento, imagem) VALUES (?,?,?,?,?,?,?,?,?,?)", 
                        (apam))
        self.conn.commit()
        # Mostrando mesnsagem de sucesso
        messagebox.showinfo('Sucesso', 'Registrado com Sucesso!')
        print("Registrado com Sucesso!")

    def view_all_bancoapam(self):
        self.c.execute("SELECT * FROM bancoapam")
        data = self.c.fetchall()
        return data

    def search_apam(self, id):
        self.c.execute("SELECT * FROM bancoapam WHERE id=?", (id,))
        data = self.c.fetchone()
        if data:
            return data
        else:
            messagebox.showerror('Erro', f'Nenhum ID {id} encontrado!')

    def update_apam(self, valor_atualizado):
        data = valor_atualizado
        if data:
            query = "UPDATE bancoapam SET name=?, cpf=?, data=?, email=?, endereco=?, matricula=?, telefone=?, sexo=?, temperamento=?, imagem=? WHERE id=?"
            self.c.execute(query,valor_atualizado)
            self.conn.commit()
            messagebox.showinfo('Sucesso', f'Informação do ID {valor_atualizado[10]} foi atualizado!')
        else:
            messagebox.showerror('Erro', f"Nenhum ID {valor_atualizado[10]} encontrado!")
            print(f"Nenhum ID '{valor_atualizado[10]}' encontrado!")

    def delete_apam(self, id):
        self.c.execute("SELECT * FROM bancoapam WHERE id=?", (id,))
        data = self.c.fetchone()
        if data:
            self.c.execute("DELETE FROM bancoapam WHERE id=?", (id,))
            self.conn.commit()
            messagebox.showinfo('Sucesso', f"Informação do ID {id} foi deletado!")
            print(f"Informação do ID '{id}' foi deletado!")
        else:
            messagebox.showerror('Erro', f"Nenhum ID {id} encontrado!")
            print(f"Nenhum ID '{id}' encontrado!")


# create a registration system instance
registration_system = RegistrationSystem()