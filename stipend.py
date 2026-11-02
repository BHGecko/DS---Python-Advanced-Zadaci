prosjek_ocjena = 4.2
rezultat_testa = 84

if prosjek_ocjena >= 3.5:
    if rezultat_testa > 65:
        print("Ispunjavate uslove za punu stipendiju!")
    elif rezultat_testa >= 50:
        print("Ispunjavate uslove za djelomičnu stipendiju.")
    else:
        print("Ne ispunjavate uslove za stipendiju.")