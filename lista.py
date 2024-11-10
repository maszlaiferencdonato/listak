gyumolcs_lista = []

while True:
    gyumolcs = input(str("Adjon meg egy gyümölcsöt"))
    
    if gyumolcs.lower() == "vége":
        break
    elif gyumolcs in gyumolcs_lista:
        print("Ez a gyümölcs már szerepel a listában!")
    else:
        gyumolcs_lista.append(gyumolcs)


print("A megadott gyümölcsök:")
print(" ".join(reversed(gyumolcs_lista)))
