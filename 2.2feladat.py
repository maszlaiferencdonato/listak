def szavak_bekerese():
    szavak = []
    print("Sdj meg szavakat, amelyek 'a' vagy 'A' betűvel kezdődnek!")
    print("Ha nem 'a' vagy 'A' betűvel kezdődő szót adsz meg, a program nem menti azt.")
    print("Nyomj ENTER-t, ha befejeznéd a megadást.")

    while True:
        szo = input("Adj meg egy szót: ")
        if szo == "":
            break 
        elif szo.startswith("a") or szo.startswith("A"):
            szavak.append(szo)
        else:
            print("A szó nem 'a' vagy 'A' betűvel kezdődik.")

    print("\nAz összegyűjtött szavak:")
    for szo in szavak:
        print(szo)

szavak_bekerese()
