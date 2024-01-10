import re
#solicita dados 
nome = input(str("digite seu nome: "))

idade = input("digite sua idade: ")

#cria uma lista de generos
generos = ['Masculino', 'Feminino','Não quero declarar', 'outros']

#cria um loop para certificar das escolhas do usuario
while True:
    print('Selecione seu genero:')
    for i, genero in enumerate(generos, start=1):
        print(f"{i}. {genero}")
        
#solicita a escolha do genero
    escolha = int(input("Digite o numero do genero selecionado: "))
    
#verifica se a escolha é valida
    if 1 <= escolha <= len(generos):
        generos_selecionado = generos[escolha -1]
        print(f"Você selecionou {generos_selecionado}.")
        break
    else:
        print("escolha invalida. por favor, selecione um numero valido")

#solicita o endereço
endereço = input("Endereço: ")

#solicita o numero do endereço
numero_do_endereço =input("Numero: ")

#cria uma lista para declara se tem ou não complemento
lis_complemento = ['sim','não']

#cria um loop para certificar das escolhas do usuario
while True:
    print('Seu endereço tem complemento?')
    for i, complemento in enumerate(lis_complemento, start=1):
        print(f"{i}. {complemento}")
        
    #solicita uma escolha entre sim ou não
    escolha2 = int(input("digite 1 se tiver complemento, se não 2 "))
    if 1 <= escolha2 <= len(lis_complemento):
        complemento_selecionado = lis_complemento[escolha2 - 1]
        
        #caso o endereço precise de complemento 
        if complemento_selecionado == 'sim':
            complemento = input("Digite seu complemento: ")
            print(f"Endereço: {endereço}, {numero_do_endereço}, complemento: {complemento}")
        
        #caso o endereço não precise de um complemento
        else:
            print(f"Endereço: {endereço}, {numero_do_endereço}")
        break
            
    #caso o usuario for desprovido de inteligencia
    else:
        print("Escolha inválida. Por favor, selecione 1 ou 2")
while True:
#solicita um E-mail
    email = input("digite seu email: ")
    valid_email = re.compile(r'^[^\s]+@gmail.com$')
    if valid_email.match(email):
        print("email valido")
        break
    else:
        print("Formato do email invalido, Certifique-se de que não há espaços e que termina com @gmail.com.")
        
#solicita um numéro de telefone
numero_tele = input("Digite seu numero com ddd: ")

#mensagem dizendo que finalizou o cadastro e refornecendo as informações
print("Cadastro comcluido suas informações são:")
print('''Nome: {}
Idade: {}
Endereço: {}{}, complemento: {}
Email: {}
Numero: {}'''.format(nome,
      idade,
      endereço, numero_do_endereço, complemento,
      email,
      numero_tele))