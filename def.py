def daLiJePlatioRacun(ime, jePlatioRacun):
          #1 PARAMETAR IME   #2 TRUE DRUGI PARAMETAR

    if jePlatioRacun==True: #jePlatio
        print('korisnik' ,ime, 'je platio racun')
    else:
        print('korisnik', ime, 'nije platio racun')

daLiJePlatioRacun('Vuk',True)
daLiJePlatioRacun('Ana', False)
