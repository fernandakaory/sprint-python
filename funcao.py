import re
continua = "sim"
msgFinal = []

def validaNome(nome):
    erro=""
    if re.search("\d",nome):
        erro = "Nomes não podem conter números"
    return erro
def validaEmail(email):
    erro=""
    if not re.search("@",email):
        erro = "O email precisa conter @"
    return erro

def validaSenha(senha):
    erro=""
    if not re.search("\d{6}",senha) or len(senha) > 6:
        erro = "A senha deve conter 6 números"
    return erro

def recebeNota(nota):
    erro = ""
    if nota>0 and nota <= 3:
        print("Sentimos muito por isso. Por favor, conte-nos o motivo dessa nota.")
        motivo = input()
        print("Obrigado pelo feedback!")
        msgFinal.append(f"Você avaliou nota {nota} para {avaliacao}.\nMotivo: {motivo}")
    elif nota>=3 and nota <=5:
        print("Ficamos felizes com isso. Obrigado pelo feedback!")
        msgFinal.append(f"Você avaliou nota {nota} para {avaliacao}.")
    else:
        erro= "Por favor, digite um número válido"
        return erro
try:
    #área de cadastro e validação 
    print("CADASTRO")
    
    nome = input("Informe seu nome: ")
    erro = validaNome(nome)
    if erro:
        raise ValueError(erro)
    email = input("Informe seu e-mail: ")
    erro = validaEmail(email)
    if erro:
        raise ValueError(erro)
    senha = input("Crie uma senha de 6 dígitos: ")
    erro = validaSenha(senha)
    if erro:
        raise ValueError(erro)

    infoCliente = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    print("\nVocê está no ônibus ST23. Rota Vila Mariana.")
    while continua.lower() == "sim":
        print("\nDigite 1 para avaliar as condições do ônibus.\nDigite 2 para avaliar a rota atual.\nDigite 3 para avaliar sua experiência usando o aplicativo.\nDigite 4 para avaliar a pontualidade do ônibus.\nDigite 5 para entrar em contato com o SAC.")
        escolha = int(input())

# menu de escolhas
        if escolha == 1:
            avaliacao = "Condições do ônibus"
            print("\nEscolha uma nota de 1 a 5 para avaliar as condições do ônibus, sendo 1 péssimas condições e 5 ótimas condições.")
            nota= int(input())
            erro = recebeNota(nota)
            if erro:
                raise ValueError

        if escolha==2:
            avaliacao = "Rota do ônibus"
            print("\nEscolha uma nota de 1 a 5 para avaliar a rota atual do ônibus, sendo 1 péssima rota e 5 ótima rota.")
            nota= int(input())
            erro = recebeNota(nota)
            if erro:
                raise ValueError


        if escolha==3:
            avaliacao = "Experiência usando o aplicativo"
            print("\nEscolha uma nota de 1 a 5 para avaliar sua experiência utilizando o aplicativo, sendo 1 para péssima experiência e 5 para ótima experiência.")
            nota= int(input())
            erro = recebeNota(nota)
            if erro:
                raise ValueError


        if escolha==4:
            avaliacao = "Pontualidade do ônibus"
            print("\nEscolha uma nota de 1 a 5 para avaliar a pontualidade do ônibus, sendo 1 péssima pontualidade e 5 ótima pontualidade.")
            nota= int(input())
            erro = recebeNota(nota)
            if erro:
                raise ValueError


        if escolha==5:
            print("\nInsira a mensagem.")
            sac = input()
            print("Iremos responder o mais rápido possível. Obrigado por utilizar nossos serviços.")
            msgFinal.append(f"Você contatou o SAC.\nMensagem enviada:{sac}")
        
        if escolha<1 or escolha>5:
            erro= "Por favor, digite uma opção válida"
            raise ValueError
        
    #pergunta se quer continuar avaliando
        continua = input("\nVocê deseja fazer uma nova avaliação? ")
        if continua.lower()!="sim" and continua.lower()!="não":
            erro= "Por favor, digite sim ou não"
            raise ValueError
        
    #exibe as mensagens finais
    print("\n*" * 70)
    print("INFORMAÇÕES DO CLIENTE:")
    print(f"Nome: {infoCliente['nome']}")
    print(f"E-mail: {infoCliente['email']}")
    print("*" * 70)
    for i in range(len(msgFinal)):
        print(msgFinal[i])
    print("*" * 70)
    print("\nObrigada por avaliar os serviços da SmarTech.")
except ValueError:
    print(erro)
finally:
    print("Fim da sessão de feedback")
