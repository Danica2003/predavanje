class student:
    def __init__(self, ime, prezime, jmbg): # def-razmak- pa dve donje crte
        self.ime=ime
        self.prezime=prezime
        self.jmbg=jmbg

Danica = student('Danica', 'Antonijevic', 204033002400402)

print(vars(Danica)) # vars () vrednost objekta
