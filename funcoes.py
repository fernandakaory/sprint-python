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

def recebeNota(avaliacao, msgFinal, positivos,negativos):
    erro = ""
    print(f"\nEscolha uma nota de 1 a 5 para avaliar {avaliacao}, sendo:\n1 - Péssima\n2 - Ruim\n3 - Mediana\n4 - Boa\n5- Excelente")
    nota= int(input())
    if nota>0 and nota <= 3:
        print("\nSentimos muito por isso. Por favor, conte-nos o motivo dessa nota.")
        motivo = input()
        print("\nObrigado pelo feedback!")
        msgFinal.append(f"\nVocê avaliou nota {nota} para {avaliacao}.\nMotivo: {motivo}")
        negativos.append(f"\nAvaliou nota {nota} para {avaliacao}.\nMotivo: {motivo}")
    elif nota>=3 and nota <=5:
        print("Ficamos felizes com isso. Obrigado pelo feedback!")
        msgFinal.append(f"\nVocê avaliou nota {nota} para {avaliacao}.")
        positivos.append(f"\nAvaliou nota {nota} para {avaliacao}.")

    else:
        erro= "Por favor, digite um número válido"
        return erro

def insereFeedback (nome, positivos, negativos, listaSac):
    if positivos != []:
        with open('feedbacks/positivos.txt', 'a',encoding='utf-8 ') as arquivo:
            arquivo.write(f'\n{nome}')
            for avaliacao in positivos:
                arquivo.write(avaliacao)
    if negativos!=[]:
        with open('feedbacks/negativos.txt', 'a',encoding='utf-8 ') as arquivo:
            arquivo.write(f'\n{nome}')
            for avaliacao in negativos:
                arquivo.write(avaliacao)
    if listaSac!=[]:
        with open('feedbacks/sac.txt', 'a',encoding='utf-8 ') as arquivo:
            arquivo.write(f'\n{nome}')
            for mensagens in listaSac:
                arquivo.write(mensagens)
