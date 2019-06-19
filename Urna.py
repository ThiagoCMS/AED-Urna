from RedBlackTree import *
from Candidato import *
from random import randint
import re
eleitores = RedBlackTree()
titulosUsados = BinaryTree()
candidatos = {}

def addTitulo(numero):
    if numero.isdigit():
        if len(numero) == 4:
            numero = int(numero)
            if eleitores.search(numero) == None:
                eleitores.insert(numero)
                print("Título adicionado com sucesso!")
                return True
            else: 
                print("Título já cadastrado!")
                return False
        else:
            print("O título deve ser composto de 4 digitos numéricos!")
            return False
    else:
        print("O título deve conter apenas números!")
        return False

def removerTitulo(numero):
    if numero.isdigit():
        numero = int(numero)
        temp = eleitores.search(numero)
        if temp != None:
            eleitores.deleteNode(numero)
            print("Título removido com sucesso!")
            return True
        else:
            print("O título %s não está cadastrdo!"%numero)
            return False
    else:
        print("Os títulos são compostos por 4 digitos numéricos!")
        return False
        
def addTituloAut():
    for i in range(501):
        if eleitores.search(i+1) == None:
            eleitores.insert(i+1)
        
def checkTitulo(numero):
    if numero.isdigit():
        if len(numero) == 4:
            numero = int(numero)
            if eleitores.search(numero) != None:
                return True
            else:
                return "O título %s não está cadastrado!"%str(numero).zfill(4)
        else:
            return "Os títulos cadastrados são compostos por 4 digitos numéricos!"
    else:
        return "Os títulos são compostos apenas por números!"
    
def votou(numero):
    numero = int(numero)
    if titulosUsados.search(numero) == None:
        return False
    else:
        return True

def votar(titulo, numero):
    candidatos[numero].addVoto()
    titulosUsados.insert(int(titulo))
    return "Voto realizado com sucesso!"

def votarAut():
    eleitores.percorrer(eleitores.getRoot())
    x = list(eleitores.enviar())
    b = list(candidatos.keys())
    eleitores.limpar()
    for i in x:
        if titulosUsados.search(i.getData()) == None:
            titulosUsados.insert(i.getData())
            candidatos[b[randint(0,len(b)-1)]].addVoto()

def checkCandidato(numero):
    if numero.isdigit():
        if int(numero) < 100 and int(numero) > 0:
            if numero in candidatos:
                return True
            else:
                return "Não existe candidato com o número %s!"%numero
        else:
            return "Os números dos candidatos são maiores que 0 e menores que 100!"
    else:
        return "Os números dos candidatos são compostos apenas por números!"
    
def checkNumero(numero):
    erro = False
    try:
        temp = int(numero)
        if temp <= 0 or temp >= 100:
            erro = True
            print("O número do candidato pode ser apenas números maiores que 0 e menores que 100!")
    except ValueError:
        erro = True
        print("O número do candidato deve conter apenas números!")
    if erro == False and numero in candidatos:
        erro = True
        print("Número %s já cadastrado!"%numero)
    return erro
    
def checkNome(nome):
    erro = False
    letra = False
    for i in nome:
        if i != " ":
            letra = True
            break
    if letra == False or nome == "":
        erro = True
        print("O nome do candidato deve ser informado!")
    if erro == False:
        for i in nome:
            if re.match("^[!@#$%&*()_=+¹²³£¢¬§{}´`~^:;.>,</?°|\ªº'0-9 ]*$", i):
                erro = True
                print("O nome do candidato deve conter apenas letras!")
                break
    return erro
    
def addCandidato(numero, nome):
    candidatos[numero] = Candidato(numero, nome)

def verCandidato(numero):
    x, y, z = candidatos[numero].getDados()
    print("\nNome: %s, numero: %s"%(y, x))

def resetVoatacao():
    titulosUsados = BinaryTree()

def removerCandidato(numero):
    if numero in candidatos:
        del candidatos[numero]
        return "Candidato %s excluído com sucesso"%numero
    else:
        return "Não existe candidato com o número %s"%numero

def encerrarVotacao():
    t = sorted(candidatos.keys())
    result = []
    defi = []
    for i in t:
        x, y, z = candidatos[i].getDados()
        a = (z, (x, y))
        result.append(a)
    for i in range(len(result)):
        aux = result[0]
        for j in range(i, len(result)):
            if result[j][0] > aux[0]:
                aux = result[j]
        defi.append(aux)
        result.remove(aux)
    print("Posição        Nº Votos        Nº        Nome")
    for i in range(len(defi)):
        print("%iº             %s               %s        %s"%(i+1, defi[i][0], defi[i][1][0], defi[i][1][1]))
    
