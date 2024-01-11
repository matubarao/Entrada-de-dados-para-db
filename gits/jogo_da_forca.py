import random
lista = ["Abacaxi","Bola","Cachorro","Dentista","Elefante","Foguete","Girassol","Hamburguer","Igreja","Jacaré","Kanguru","Laranja","Macaco","Navio","Ovelha","Piano","Quadrado","Rato","Sapato","Tigre"]
palavra = random.choice(lista)
palavra = palavra.lower()
nmr_tenta = 5
letras_erradas = []
letras_certas = []
advinha = "_" * len(palavra)
def mostra_forca():
    print(f"letras restantes: {nmr_tenta}")
    print("palavra:"+"".join(advinha))
    print("letras errada:"+" ".join(letras_erradas))

while nmr_tenta > 0:
    mostra_forca()
    palpite=input("digite uma letra: ").lower()
    if len(palpite) != 1 or not palpite.isalpha():
        print("tente apenas 1 letra.")
        continue
    if palpite in letras_erradas or palpite in letras_certas:
        print("voce ja tentou essa letra.")
        continue
    if palpite in palavra:
        letras_certas.append(palpite)
        for i in range(len(palavra)):
            if palavra [i] == palpite:
                 advinha = advinha[:i] + palpite + advinha[i+1:]
    else:
        letras_erradas.append(palpite)
        nmr_tenta -= 1 
    if advinha==palavra:
        mostra_forca()
        print('WOAU')
        break
if nmr_tenta==0:
    mostra_forca()
    print(f"você é um fracassado a palavra era '{palavra}''.")  