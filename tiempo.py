def segundo_a_minuto(segundo):
    return segundos /60

if __name__  == "__main__":
    segundos =150
    minutos = segundo_a_minuto(segundos)
    print(f"{segundos} segundo equivalen a {minutos} minutos.")
