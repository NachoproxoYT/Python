meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }
while True:
    word = input("Escribe una palabra que no entiendas (¡con MAYÚSCULAS!:")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        Definicion = input("Definicion de la palabra: ")
        meme_dict[word] = Definicion
    e = input("Si quieres salir del bucle pon 1. Si quieres seguir pon 2")
    if e == "1":
        break
