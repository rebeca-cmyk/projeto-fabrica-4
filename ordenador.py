nome1 = input(" nome1 do boi: ")
pesoboi1 = float(input("peso do boi: "))
nome2 = input("nome2 do boi: ")
pesoboi2 = float(input("peso do boi: "))
nome3 = input("nome3 do boi: ")
pesoboi3 = float(input("peso do boi: "))

if pesoboi1 > pesoboi2 and pesoboi1 > pesoboi3:
    if pesoboi > pesoboi3:
        print(f"{nome1}, {nome2}, {nome3}")
    else:
        print(f"{nome1}, {nome3}, {nome2}")
elif pesoboi2 > pesoboi1 and pesoboi2 > pesoboi3:
    if pesoboi1 > pesoboi3: 
        print(f"{nome2}, {nome1}, {nome3}")
    else:
        print(f"{nome2}, {nome3}, {nome1}")
else: 
    if pesoboi1 > pesoboi2:
        print(f"{nome3}, {nome1}, {nome2}")
    else:
        print(f"{nome3}, {nome2}, {nome1}")

