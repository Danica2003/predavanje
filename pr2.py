def cenaPotrStruje(kolicina, cenaKWH):
    return kolicina*cenaKWH         # vraca informacije return

kolicinaStruje=int(input('Unesi kolicinu struje '))
cenaKilowata=int(input('Unesi kolicinu struje '))
cena_potr_struje= cenaPotrStruje(kolicinaStruje, cenaKilowata)

print(cena_potr_struje)

