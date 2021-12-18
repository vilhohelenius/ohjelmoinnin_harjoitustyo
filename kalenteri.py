kuukaudet = {'Tammikuu': 31,
            'Helmikuu': 28,
            'Maaliskuu': 31,
            'Huhtikuu': 30,
            'Toukokuu': 31,
            'Kesäkuu': 30,
            'Heinäkuu': 31,
            'Elokuu': 31,
            'Syyskuu': 30,
            'Lokakuu' : 31,
            'Marraskuu': 30,
            'Joulukuu': 31}

kuut = [i for i in kuukaudet.keys()]

viikko = ['Ma', 'Ti', 'Ke', 'To', 'Pe', 'La', 'Su']

import datetime

with open('muistio.txt') as tiedosto:
        for rivi in tiedosto:
            if str(datetime.date.today().strftime('%d.%m.%Y')) in rivi:
                print()
                print(rivi)

def lisaa_muistutus():
    lisaa = input('Haluatko lisätä muistutuksen? (k tai e) ')
    if lisaa == 'k':
        paiva = input('Anna päivä jolle haluat luoda muistutuksen (muoto: 1.1.2022): ')
        muistutus = str(input('Muistutus: '))
        with open('muistio.txt', 'a') as tiedosto:
            tiedosto.write(paiva + ' ' + muistutus + '\n')
    elif lisaa == 'e':
        return None

def kaikki_muist() -> bool:
    kaikki = input('Haluatko nähdä kaikki muistutukset?(k tai e) ')
    if kaikki == 'k':
        return True
    else:
        return False

def karkausvuosi(vuosi: int) -> bool:
    if vuosi % 4 == 0:
        if vuosi % 400 == 0:
            return True
        elif vuosi % 100 == 0:
            return False
        else:
            return True
    else:
        return False

space =''
space = space.rjust(2, ' ')

def kalenteri(kuukausi: int, vuosi: int):
    if karkausvuosi(vuosi) == True:
        kuukaudet['Helmikuu'] = 29
    ukuukausi = kuut[kuukausi-1]
    paivia = kuukaudet[ukuukausi]
    alku = datetime.date(vuosi, kuukausi, 1)
    ekapaiva = alku.isoweekday()
    print()
    print(ukuukausi, vuosi)
    print(' '.join(['{0:<2}'.format(w) for w in viikko]))
    for i in range(paivia + ekapaiva - 1):    
        if i <= ekapaiva-2:
            print(space, end =' ')
        else:
            print('{:02d}'.format(i-ekapaiva+2), end =' ')
            if (i+1) % 7 == 0:
                print()
    print()
    if kaikki_muist() == True:
        with open('muistio.txt') as tiedosto:
            for rivi in tiedosto:
                print(rivi)
    print()
    lisaa_muistutus()
    print()
    
def tarkistus():
    luo_kalenteri = True
    while luo_kalenteri:
        vuosi_tark = False
        while vuosi_tark == False:
            vuosi_input = input('Anna vuosi (tyhjä lopettaa): ')
            if vuosi_input == '':
                luo_kalenteri = False
                return None
            else:
                vuosi = int(vuosi_input)
                if 1 > vuosi > 9999:
                    print("Syötä vuosiluku väliltä 1-9999")
                else:
                    vuosi_tark = True        
        kuu_tark = False
        while kuu_tark == False:
            kuu_input = input('Anna kuukausi (tyhjä näyttää koko vuoden): ')
            if kuu_input == '':
                for i in range(1,13):
                    kalenteri(i, vuosi)
                tarkistus()
            else:
                if kuu_input[0] == '0':
                    kuu_input = kuu_input[1:]                
                kuukausi = int(kuu_input)
                if 1 > kuukausi > 12:
                    print("Syötä kuukausi väliltä 1-12")
                else:
                    kuu_tark = True 
        if vuosi_tark == True and kuu_tark == True:
            kalenteri(kuukausi, vuosi)

if __name__ == '__main__':
    tarkistus()




