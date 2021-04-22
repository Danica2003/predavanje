class student:
    def __init__(self, ime, prezime, jmbg): # def-razmak- pa dve donje crte
        self.ime=ime
        self.prezime=prezime
        self.jmbg=jmbg


    def imeIPrezime(self):
        return f"{self.ime} {self.prezime}"

Danica = student('Danica', 'Antonijevic', 204033002400402)
dusan = student('Dusan', 'Peric', 532535632392939)

print(dusan.imeIPrezime())