import tkinter as tk
import random

class Tarningsspel:
    def __init__(self, root):
        self.root = root
        self.root.title("Först till 50 - Tärningsspel")
        self.root.geometry("250x400")
        self.visa_startmeny()

    def visa_startmeny(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Välj antal spelare (2–5)", font=("Helvetica", 14)).pack(pady=10)

        for i in range(2, 6):
            tk.Button(self.root, text=f"{i} spelare", font=("Helvetica", 12),
                      command=lambda x=i: self.starta_spel(x)).pack(pady=5)

    def starta_spel(self, antal_spelare):
        self.antal_spelare = antal_spelare
        self.poang = [0] * self.antal_spelare
        self.rundpoang = 0
        self.aktiv_spelare = 0
        self.spel_over = False
        self.bygg_gui()
        self.uppdatera_gui()

    def bygg_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.player_labels = []
        for i in range(self.antal_spelare):
            label = tk.Label(self.root, text=f"Spelare {i + 1}: 0", font=("Helvetica", 16))
            label.pack()
            self.player_labels.append(label)

        self.round_label = tk.Label(self.root, text="Rundpoäng: 0", font=("Helvetica", 14))
        self.round_label.pack()

        self.dice_label = tk.Label(self.root, text="Tärningskast: -", font=("Helvetica", 14))
        self.dice_label.pack()

        self.status_label = tk.Label(self.root, text="Spelare 1s tur", font=("Helvetica", 14, "bold"))
        self.status_label.pack(pady=10)

        self.roll_button = tk.Button(self.root, text="Kasta Tärning", font=("Helvetica", 12),
                                     bg="lightblue", command=self.kasta)
        self.roll_button.pack(pady=5)

        self.hold_button = tk.Button(self.root, text="Spara Poäng", font=("Helvetica", 12),
                                     bg="lightgreen", command=self.spara)
        self.hold_button.pack(pady=5)

        self.restart_button = tk.Button(self.root, text="Starta om", font=("Helvetica", 12),
                                        bg="orange", command=self.visa_startmeny)
        self.restart_button.pack(pady=10)

        self.restart_label = tk.Label(self.root, text="🎲", font=("Arial", 40)) 
        self.restart_label.pack(pady=10)


    def kasta(self):
        if self.spel_over:
            return

        slag = random.randint(1, 6)
        tarningssymboler = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
        self.dice_label.config(text=f"Tärningskast: {tarningssymboler[slag - 1]} ({slag})")

        if slag == 1:
            self.rundpoang = 0
            self.nasta_spelare()
        else:
            self.rundpoang += slag

        self.uppdatera_gui()

    def spara(self):
        if self.spel_over:
            return

        self.poang[self.aktiv_spelare] += self.rundpoang
        if self.poang[self.aktiv_spelare] >= 50:
            self.status_label.config(text=f"🎉 Spelare {self.aktiv_spelare + 1} vinner! 🎉")
            self.spel_over = True
            self.inaktivera_knappar()
        else:
            self.rundpoang = 0
            self.nasta_spelare()

        self.uppdatera_gui()

    def nasta_spelare(self):
        self.aktiv_spelare = (self.aktiv_spelare + 1) % self.antal_spelare
        self.rundpoang = 0

    def uppdatera_gui(self):
        for i, label in enumerate(self.player_labels):
            label.config(text=f"Spelare {i + 1}: {self.poang[i]}")
        self.round_label.config(text=f"Rundpoäng: {self.rundpoang}")
        if not self.spel_over:
            self.status_label.config(text=f"Spelare {self.aktiv_spelare + 1}s tur")

    def inaktivera_knappar(self):
        self.roll_button.config(state="disabled")
        self.hold_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    spel = Tarningsspel(root)
    root.mainloop()
