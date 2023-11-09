import re

# função que verifica se o nome tem números ou está vazio
def validaNome(nome):
    erro=""
    if re.search("\d",nome) or nome == '':
        erro = "Campo obrigatório.Por favor, insira um nome válido, sem números."
    return erro

# verifica se o email está na estrutura padrão aceita
def validaEmail(email):
    erro=""
    if not re.search("\w+@\w+\.\w+", email) or email == '':
        erro = "Campo obrigatório. Por favor, insira um e-mail válido."
    return erro

# verifica se a senha possui 6 números
def validaSenha(senha):
    erro=""
    if not re.search("\d{6}",senha) or len(senha) > 6 or senha == '':
        erro = "Campo obrigatório. Por favor, insira uma senha válida de 6 dígitos."
    return erro

# função que pergunta a nota e armazena nas lista para a mensagem final e resumos
def recebeNota(avaliacao, msgFinal, positivos,negativos):
    erro = ""
    print(f"\nEscolha uma nota de 1 a 5 para avaliar {avaliacao}, sendo:\n1 - Péssima\n2 - Ruim\n3 - Mediana\n4 - Boa\n5 - Excelente")
    nota= int(input())
    if nota>0 and nota <= 3:
        print("\nSentimos muito por isso. Por favor, conte-nos o motivo dessa nota.")
        motivo = input()
        while motivo == "":
            print("\nO motivo não pode estar vazio. Por favor, digite novamente:")
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

# função para inserir as avaliações nos documentos txt de resumo
def insereFeedback (email, positivos, negativos, listaSac):
    if positivos != []:
        with open('feedbacks/positivos.txt', 'a',encoding='utf-8 ') as arquivo:
            arquivo.write(email)
            for avaliacao in positivos:
                arquivo.write(avaliacao)
            arquivo.write("\n ")

    if negativos!=[]:
        with open('feedbacks/negativos.txt', 'a',encoding='utf-8 ') as arquivo:
            arquivo.write(email)
            for avaliacao in negativos:
                arquivo.write(avaliacao)
            arquivo.write("\n ")
    if listaSac!=[]:
        with open('feedbacks/sac.txt', 'a',encoding='utf-8 ') as arquivo:
            arquivo.write(email)
            for mensagens in listaSac:
                arquivo.write(mensagens)
            arquivo.write("\n ")
