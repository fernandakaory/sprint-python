import re
continua = "sim"
msgFinal = []
avaliados = []

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

def recebeNota(avaliacao):
    erro = ""
    # print(f"\nEscolha uma nota de 1 a 5 para avaliar {avaliacao}, sendo 1 péssimas condições e 5 ótimas condições.")
    print(f"\nEscolha uma nota de 1 a 5 para avaliar {avaliacao}, sendo:\n1 - Péssima\n2 - Ruim\n3 - Mediana\n4 - Boa\n5- Excelente")
    nota= int(input())
    if nota>0 and nota <= 3:
        print("\nSentimos muito por isso. Por favor, conte-nos o motivo dessa nota.")
        motivo = input()
        print("\nObrigado pelo feedback!")
        msgFinal.append(f"Você avaliou nota {nota} para {avaliacao}.\nMotivo: {motivo}\n")
    elif nota>=3 and nota <=5:
        print("Ficamos felizes com isso. Obrigado pelo feedback!")
        msgFinal.append(f"Você avaliou nota {nota} para {avaliacao}.\n")
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
        if escolha not in avaliados:
            if escolha == 1:
                erro = recebeNota("condição do ônibus")
                if erro:
                    raise ValueError

            elif escolha==2:
                erro = recebeNota("rota atual")
                if erro:
                    raise ValueError

            elif escolha==3:
                erro = recebeNota("experiência usando o aplicativo")
                if erro:
                    raise ValueError

            elif escolha==4:
                erro = recebeNota("pontualidade do ônibus")
                if erro:
                    raise ValueError

            elif escolha==5:
                print("\nInsira a mensagem.")
                sac = input()
                print("\nIremos responder o mais rápido possível. Obrigado por utilizar nossos serviços.")
                msgFinal.append(f"Você contatou o SAC.\nMensagem enviada:{sac}\n")
            
            else:
                erro= "Por favor, digite uma opção válida."
                raise ValueError
            avaliados.append(escolha)
        else:
            print("Você já avaliou este tópico.")
        
    #pergunta se quer continuar avaliando
        continua = input("\nVocê deseja fazer uma nova avaliação? (Digite 'sim' ou 'não') ")
        if continua.lower()!="sim" and continua.lower()!="não":
            erro= "Por favor, digite sim ou não."
            raise ValueError
        
    #exibe as mensagens finais
    print("*" * 70)
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
