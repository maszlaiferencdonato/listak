def szavak_bekerese():

    szavak = []
    print("Adj meg szavakat, amelyek kis 'a' betűvel kezdődnek!")
    print("Ha nem 'a' betűvel kezdődő szót adsz meg, a program nem menti azt.")
    print("Nyomj ENTER-t, ha befejeznéd a megadást.")

    while True:
        szo = input("Adj meg egy szót: ")
        if szo == "":
            break 
        elif szo.startswith("a"):
            szavak.append(szo)
        else:
            print("A szó nem 'a' betűvel kezdődik")

    print("\nAz összegyűjtött szavak:")
    for szo in szavak:
        print(szo)

szavak_bekerese()

