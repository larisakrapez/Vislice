import model

def izpis_igre(igra):
    tekst = (
        '===============================================================\n\n'
        'Stevilo preostalih poskusov: {stevilo_preostalih_poskusov} \n\n'
        '       {pravilni_del_gesla} \n\n'
        'Neuspeli poskusi: {neuspeli_poskusi} \n\n'
        '==============================================================='
    ).format(
        stevilo_preostalih_poskusov=model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        pravilni_del_gesla=igra.pravilni_del_gesla(),
        neuspeli_poskusi=igra.nepravilni_ugibi()
    )
    return tekst

def izpis_zmage(igra):
    tekst = (
        '\n##### JEEEEJJJJ, zmaga!! Geslo je bilo: {geslo} #####\n\n'
    ).format(
        geslo = igra.pravilni_del_gesla()
    )
    return tekst

def izpis_poraza(igra):
    tekst = (
        '\n##### ŠMENT X___X !!! Geslo je bilo: {geslo}. Več sreče prihodnjič. #####\n\n'
    ).format(
        geslo=igra.geslo
    )
    return tekst

def izpis_napake():
    return '\n##### Ugiba se ena črka naenkrat! #####\n\n'

def izpis_napake_znak():
    return '\n##### Ugib naj ne vsebuje posebnih znakov! #####\n\n'

def zahtevaj_vnos():
    return input('Napiši svojo črko: ')

def pozeni_vmesnik():

    igra = model.nova_igra()

    while True: #neskoncna zanka
        #najprej izpisemo stanje, da vidimo, koliko crka je ipd.
        print(izpis_igre(igra))
        # cakamo na crko od uporabnika
        poskus = zahtevaj_vnos()
        rezultat_ugiba = igra.ugibaj(poskus)
        if rezultat_ugiba == model.VEC_KOT_CRKA:
            print(izpis_napake())
        elif rezultat_ugiba == model.POSEBEN_ZNAK:
            print(izpis_napake_znak())
        if rezultat_ugiba == model.ZMAGA:
            print(izpis_zmage(igra))
            ponovni_zagon = input('Za novo igro vpiši 1.').strip()
            if ponovni_zagon == '1':
                igra = model.nova_igra()
            else:
                break
        elif rezultat_ugiba == model.PORAZ:
            print(izpis_poraza(igra))
            ponovni_zagon = input('Za novo igro vpiši 1. \n').strip()
            if ponovni_zagon == '1':
                igra = model.nova_igra()
            else:
                break


# Zazeni igro:
pozeni_vmesnik()