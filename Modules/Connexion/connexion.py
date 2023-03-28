import tkinter as tk
from tkinter import *
from tkinter import messagebox
from ttkbootstrap import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os
import platform
import sys
import webbrowser
import subprocess

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Version import __version__
from Bdd import ConnexionBdd


class LoginApp(tk.Tk):
    def __init__(self, connexion):
        super().__init__()
        self.connexion = connexion
        self.geometry("1280x720")
        self.title("Samabox - Connexion")

        # Création du style ttkbootstrap
        self.style = Style()
        self.style.theme_use("superhero")

        # Création du cadre principal
        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(expand=True)

        # Récupère le chemin absolu du fichier Python en cours d'exécution
        self.chemin_python = os.path.abspath(__file__)
        # Récupère le répertoire parent du fichier Python (qui est le répertoire de travail actuel)
        self.repertoire_travail = os.path.dirname(self.chemin_python)
        if platform.system() == "Windows":
            self.file_path_icon1 = os.path.join(
                self.repertoire_travail, "images/user.png"
            )
            self.file_path_icon2 = os.path.join(
                self.repertoire_travail, "images/password.png"
            )
            self.file_path_icon3 = os.path.join(
                self.repertoire_travail, "images/code.ico"
            )
            LoginApp.iconbitmap(self, default=self.file_path_icon3)
        else:
            self.file_path_icon3 = os.path.join(
                self.repertoire_travail, "images/code.png"
            )
            self.file_path_icon1 = os.path.join(
                self.repertoire_travail, "images/user.png"
            )
            self.file_path_icon2 = os.path.join(
                self.repertoire_travail, "Modules/assets/images/password.png"
            )
            LoginApp.iconphoto(self, default=PhotoImage(file=self.file_path_icon3))

        # Remplacez par le chemin de votre image
        image = Image.open(self.file_path_icon1)
        image2 = Image.open(self.file_path_icon2)
        photo1 = ImageTk.PhotoImage(image)
        photo2 = ImageTk.PhotoImage(image2)

        title_label = ttk.Label(
            main_frame, text="Connexion à la Semabox", font=("Arial", 18, "bold")
        )
        title_label.grid(row=0, columnspan=2, pady=10)

        self.username_label = ttk.Label(
            main_frame,
            image=photo1,
            compound="left",
            text="Nom d'utilisateur:",
            font=("Arial", 12, "bold"),
        )
        self.username_label.image = photo1

        self.username_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.username_entry = ttk.Entry(main_frame, width=30)
        self.username_entry.grid(row=2, column=1, padx=10, pady=5)

        self.password_label = ttk.Label(
            main_frame,
            image=photo2,
            compound="left",
            text="Mot de passe:",
            font=("Arial", 12, "bold"),
        )
        self.password_label.image = photo2
        self.password_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.password_entry = ttk.Entry(main_frame, show="*", width=30)
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        # Ajout du texte "Version 2.0" en dessous du bouton de connexion
        version_label = ttk.Label(
            main_frame,
            text=f"Version {__version__}",
            font=("Helvetica", 10),
            foreground="gray",
        )
        version_label.grid(row=5, column=1, pady=10, sticky="e")

        # Ajout du lien GitHub à côté du texte de la version
        def open_github_link(event):
            webbrowser.open(
                "https://github.com/Foufou-exe/Semabox"
            )  # Remplacez par le lien de votre dépôt GitHub

        github_link = ttk.Label(
            main_frame,
            text="GitHub",
            font=("Helvetica", 10),
            foreground="gray",
            cursor="hand2",
        )
        github_link.grid(row=5, column=1, pady=10, sticky="w")
        github_link.bind("<Button-1>", open_github_link)

        # Création des boutons de connexion et d'inscription
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=1, pady=10)

        self.login_button = ttk.Button(
            button_frame,
            text="Se connecter",
            style="success.TButton",
            command=self.login,
        )
        self.login_button.pack(side="left", padx=5)

        self.register_button = ttk.Button(
            button_frame,
            text="S'inscrire",
            style="primary.TButton",
            command=self.register,
        )
        self.register_button.pack(side="left", padx=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        App_path = os.path.join(self.repertoire_travail, "../App/app.py")
        if self.connexion.check_credentials(username, password):
            messagebox.showinfo("Succès", "Connexion réussie!")
            LoginApp.destroy(self)
            subprocess.call(["python", App_path], shell=True)

        elif not username or not password:
            messagebox.showerror(
                "Erreur", "Nom d'utilisateur ou mot de passe incorrect."
            )

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            tk.messagebox.showerror(
                "Erreur",
                "Les champs 'Nom d'utilisateur' ou 'Mot de passe' ne doivent pas être vides.",
            )

        elif self.connexion.check_credentials(username, password):
            tk.messagebox.showerror("Erreur", "Cet utilisateur existe déjà.")
        elif self.connexion.register_user(username, password):
            messagebox.showinfo(
                "Succès", "Inscription réussie!\nVous pouvez maintenant vous connecter."
            )


if __name__ == "__main__":
    connexion = ConnexionBdd()
    app = LoginApp(connexion)
    app.mainloop()
