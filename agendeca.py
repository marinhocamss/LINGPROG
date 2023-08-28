print("************************AgendECA**************************")
print("****************Agenda telefonica de ECA******************\n")

agenda = {"nomes": [], "telefones": []}

def inserir():
    nome = input("Digite o nome do contato: ")
    agenda["nomes"].append(nome)
    telefone = int(input("Digite o número do tefelofe: "))
    agenda["telefones"].append(telefone)

def editar():
    nome_para_editar = input('Qual contato vc quer editar? ')
    if nome_para_editar in agenda["nomes"]:
        indice = agenda["nomes"].index(nome_para_editar)

        novo_nome = input('Digite o novo nome do contato:')
        agenda["nomes"][indice] = novo_nome

        novo_telefone = int(input('Digite o novo número de telefone:'))
        agenda["telefones"][indice] = novo_telefone

        print('Contato editado com sucesso!')
    
    else:
        print('Contato não encontrado!')

def remover():
    nome_para_remover = input('Qual contato deseja remover? ')
    if nome_para_remover in agenda["nomes"]:
        indice = agenda["nomes"].index(nome_para_remover)

        del agenda["nomes"][indice]
        del agenda["telefones"][indice]

        print('Contato removido com sucesso!')

    else:
        print('Contato não encontrado!')

def mostrar():
    if len(agenda["nomes"]) == 0:
        print('A agenda está vazia!')
    else:
        print('Contatos da agenda: \n')
        for i in range(len(agenda["nomes"])):
            print(f'Nome: {agenda["nomes"][i]}, Telefone {agenda["telefones"][i]}')

def sair():
    pass

saida = True 

while saida:

    print("\nOpções:")
    print("i - Inserir contato")
    print("e - Editar contato")
    print("r - Remover contato")
    print("m - Mostrar contatos")
    print("s - Sair")

    escolha = input("O que deseja fazer? ")
    if escolha == 'i':
        inserir()

    if escolha == 'e':
        editar()

    if escolha == 'r':
        remover()

    if escolha =='m':
        mostrar()

    if escolha == 's':
        print('XAUUUUUU')
        break        
