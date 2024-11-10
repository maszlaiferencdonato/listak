def mondat_tipusa(mondat):
    if mondat.endswith('.'):
        return "kijelentő mondat"
    elif mondat.endswith('?'):
        return "kérdő mondat"
    elif mondat.endswith('!'):
        return "felkiáltó, felszólító vagy óhajtó mondat"
  
def main():
  
    mondat = input("Adj meg egy mondatot: ")
    tipus = mondat_tipusa(mondat)
    print(f"A megadott mondat {tipus}.")

main()
