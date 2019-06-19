from Urna import *
print("Bem vindo!\nIniciar urna?(S ou N)")
while True:
    Ligar = input(">").upper()
    if Ligar == "S":
        ligar = True
        print("Iniciando sistema\n")
        break
    elif Ligar == "N":
        ligar = False
        print("Fechando sistema")
        break
    else:
        print("\nDigite apenas S ou N!")
pessoas=0
prefeito=0
desligar = False
if ligar == True:
    while True:
        print("\nCadastrar Títulos e Candidatos")
        print("1 - Cadastrar Título\n2 - Remover Título\n3 - Carregar Títulos\n4 - Cadastrar Candidato\n5 - Remover Candidato\n9 - Iniciar Votação\n10 - Desligar")
        
        try:
            escolha = int(input(">"))
        except ValueError:
            print("\nDigite apenas números!")
        
        if escolha == 1:
            print("\nDigite o número do título\nOBS: o número do título deve ser composto por 4 digitos!")
            aux = input(">")
            a = addTitulo(aux)
            if a == True:
                pessoas += 1
        
        elif escolha == 2:
            print("\nDigite o número do título a ser removido")
            aux = input(">")
            a = removerTitulo(aux)
            if a == True:
                pessoas -= 1
        
        elif escolha == 3:
            print("\nCarregando títulos")
            addTituloAut()
            pessoas += 500
        
        elif escolha == 4:
            print("\nDigite as informações do candidato")
            print("Número\nOBS: apenas 2 digitos)")
            numero = input(">")
            a = checkNumero(numero)
            if a == False:
                print("Nome")
                nome = input(">")
                b = checkNome(nome)
                if b == False:
                    addCandidato(numero, nome)
                    prefeito += 1
        
        elif escolha == 5:
            print("\nDigite o número do candidato a ser removido")
            numero = input(">")
            a = checkCandidato(numero)
            if a == True:
                print(removerCandidato(numero))
            else:
                print(a)
                    
        elif escolha == 9:
            if pessoas > 0:
                if prefeito > 0:
                    print("\nEncerrando cadastramento\n")
                    break
                else:
                    print("\nNão existem candidatos!\n")
            else:
                print("\nNão existem títulos cadastrados!\n")
        
        elif escolha == 10:
            desligar = True
            print("\nDesligando\n")
            break
        
        else:
            print("\nDigite apenas números válidos!\n")

if ligar == True and desligar == False:
    while True:
        print("\nVotação")
        print("1 - Votar\n2 - Gerar Votos\n3 - Resetar Votação\n4 - Resultado(Encerra Votação)\n5 - Sair(Apaga Todos os Registros)")
        
        try:
            escolha = int(input(">"))
        except ValueError:
            print("\nDigite apenas números!")
        
        if escolha == 1:
            print("\nDigite o número do seu título")
            titulo = input(">")
            a = checkTitulo(titulo)
            if a == True:
                b = votou(titulo)
                if b == False:
                    print("\nDigite o número do candidato")
                    numero = input(">")
                    c = checkCandidato(numero)
                    if c == True:
                        votar(titulo, numero)
                        print("\nVoto realizado com sucesso!")
                    else:
                        print(c)
        
        elif escolha == 2:
            print("\nGerando Votos Aleatórios")
            votarAut()
            
        elif escolha == 3:
            print("\nResetando votação!")
            resetVoatacao()
            print("\nVotos Resetados!")
        
        elif escolha == 4:
            print("\nEncerrando Votação\nCalculando Votos\n")
            encerrarVotacao()
            resetVoatacao()
            break
        
        elif escolha == 5:
            print("\nDesligando\n")
            break
    
H = input("Pressione Enter")
