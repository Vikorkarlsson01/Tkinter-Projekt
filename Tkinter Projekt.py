import tkinter as tk
import random

class Tarningsspel:
    def __init__(self, rot):
        self.rot = rot
        self.rot.title("Tärningsspel - Först till 50 poäng")
        self.startmeny()

    def startmeny(self):
        self.ryd_fonster()
        tk.Label(self.rot, text="Välj antal spelare (2–5)", font=("Arial", 14)).pack(pady=10)
        for antal in range(2, 6):
            tk.Button(self.rot, text=f"{antal} spelare", command=lambda x=antal: self.starta_spel(x)).pack(pady=5)

    def starta_spel(self, antal_spelare):
        self.antal_spelare = antal_spelare
        self.poang = [0] * antal_spelare
        self.rundpoang = 0
        self.spel_over = False
        self.aktiv_spelare = 0
        self.ryd_fonster()
        self.bygg_gui()
        self.uppdatera_gui()

    def bygg_gui(self):
        self.info = tk.Label(self.rot, font=("Arial", 16))
        self.info.pack(pady=10)

        self.tarning = tk.Label(self.rot, text="🎲", font=("Arial", 40))
        self.tarning.pack()

        self.poang_visning = tk.Label(self.rot, font=("Arial", 14))
        self.poang_visning.pack(pady=10)

        knapp_ruta = tk.Frame(self.rot)
        knapp_ruta.pack()

        tk.Button(knapp_ruta, text="Kasta tärning", command=self.kasta).grid(row=0, column=0, padx=10)
        tk.Button(knapp_ruta, text="Spara poäng", command=self.spara).grid(row=0, column=1, padx=10)
        tk.Button(self.rot, text="Starta om spelet", command=self.startmeny).pack(pady=10)

    def kasta(self):
        if self.spel_over:
            return  # Stoppa om spelet är över

        slag = random.randint(1, 6)

        if slag == 1:
            self.tarning.config(text="⚀")
            self.rundpoang = 0
            self.nasta_spelare()
        elif slag == 2:
            self.tarning.config(text="⚁")
            self.rundpoang += 2
        elif slag == 3:
            self.tarning.config(text="⚂")
            self.rundpoang += 3
        elif slag == 4:
            self.tarning.config(text="⚃")
            self.rundpoang += 4
        elif slag == 5:
            self.tarning.config(text="⚄")
            self.rundpoang += 5
        elif slag == 6:
            self.tarning.config(text="⚅")
            self.rundpoang += 6

        self.uppdatera_gui()

    def spara(self):
        if self.spel_over:
            return  # Stoppa om spelet är över
# vad är self 
        self.poang[self.aktiv_spelare] += self.rundpoang
        if self.poang[self.aktiv_spelare] >= 50:
            # Uppdatera GUI för att visa att spelaren har vunnit
            self.info.config(text=f"🎉 Spelare {self.aktiv_spelare + 1} har vunnit med {self.poang[self.aktiv_spelare]} poäng! 🎉")
            self.inaktivera_knappar()
            self.spel_over = True
        else:
            self.rundpoang = 0
            self.nasta_spelare()
        self.uppdatera_gui()

    def nasta_spelare(self):
        self.aktiv_spelare = (self.aktiv_spelare + 1) % self.antal_spelare
        self.rundpoang = 0
# Kan kalla på fel 
    def uppdatera_gui(self):
        if self.spel_over:
            self.info.config(text="Spelet är slut! Klicka på 'Starta om spelet' för att spela igen.")
        else:
            self.info.config(text=f"Spelare {self.aktiv_spelare + 1}s tur")
        
        alla_poang = "\n".join([f"Spelare {i+1}: {p} poäng" for i, p in enumerate(self.poang)])
        self.poang_visning.config(text=f"{alla_poang}\nRundpoäng: {self.rundpoang}")

    def inaktivera_knappar(self):
        for widget in self.rot.winfo_children():
            if isinstance(widget, tk.Button) and widget['text'] != "Starta om spelet":
                widget.config(state="disabled")

    def ryd_fonster(self):
        for widget in self.rot.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    rot = tk.Tk()
    Tarningsspel(rot)
    rot.mainloop()
