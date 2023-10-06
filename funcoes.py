import re

def validaNome(nome):
    erro=""
    if re.search("\d",nome) or nome == '':
        erro = "Campo obrigatório. Por favor, insira um nome válido, sem números."
    return erro

def validaEmail(email):
    erro=""
    if not re.search("\w+@\w+\.\w+", email) or email == '':
        erro = "Campo obrigatório. Por favor, insira um e-mail válido."
    return erro

def validaSenha(senha):
    erro=""
    if not re.search("\d{6}",senha) or len(senha) > 6 or senha == '':
        erro = "Campo obrigatório. Por favor, insira uma senha válida de 6 dígitos."
    return erro

def recebeNota(avaliacao, msgFinal):
    erro = ""
    print(f"\nEscolha uma nota de 1 a 5 para avaliar {avaliacao}, sendo:\n1 - Péssima\n2 - Ruim\n3 - Mediana\n4 - Boa\n5- Excelente")
    nota= int(input())
    if nota>0 and nota <= 3:
        print("\nSentimos muito por isso. Por favor, conte-nos o motivo dessa nota.")
        motivo = input()
        print("\nObrigado pelo feedback!")
        msgFinal.append(f"\nVocê avaliou nota {nota} para {avaliacao}.\nMotivo: {motivo}")
    elif nota>=3 and nota <=5:
        print("Ficamos felizes com isso. Obrigado pelo feedback!")
        msgFinal.append(f"\nVocê avaliou nota {nota} para {avaliacao}.")
    else:
        erro= "Por favor, digite um número válido"
        return erro