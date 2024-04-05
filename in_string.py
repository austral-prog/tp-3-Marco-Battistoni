def check_vowels():
    nombre = input("ingrese un nombre: ")
    print(nombre)
    in1 = "a" in nombre.lower()
    in2 = "e" in nombre.lower()
    in3 = "i" in nombre.lower()
    in4 = "o" in nombre.lower()
    in5 = "u" in nombre.lower()

    print(f"Contiene a: {in1}")
    print(f"Contiene e: {in2}")
    print(f"Contiene i: {in3}")
    print(f"Contiene o: {in4}")
    print(f"Contiene u: {in5}")
