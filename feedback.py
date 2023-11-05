import os
import json
from funcoes import *

continua = "sim"
msgFinal = []
avaliados = []
positivos = []
negativos = []
listaSac = []

try:
    cadastro = input("Você já possui cadastro? (Digite 'sim' ou 'não') ").lower()

    if cadastro == "não":
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

        #verifica se o email já foi cadastrado
        if os.path.exists(f'usuarios/{email}.json'):
            erro = "Email já cadastrado."
            raise FileNotFoundError
        else:
            with open(f'usuarios/{email}.json', 'w', encoding='utf-8') as arquivo:
                json.dump(infoCliente,arquivo)

    elif cadastro=="sim":
        #verifica as informações do cadastro
        email = input("Informe seu e-mail: ")
        erro = validaEmail(email)
        if erro:
            raise ValueError(erro)
        
        if os.path.exists(f'usuarios/{email}.json'):
            with open(f'usuarios/{email}.json', 'r', encoding='utf-8') as arquivo:
                infocadastro = json.loads(arquivo.read())
                senha = input("Digite sua senha de 6 dígitos: ")
                erro = validaSenha(senha)
                if erro:
                    raise ValueError(erro)
                if email == infocadastro['email'] and senha == infocadastro['senha']:
                    print(f"Acesso permitido! Bem-vindo(a), {infocadastro['nome']}")
                else:
                    erro = "Senha incorreta"
                    raise ValueError
        else:
            erro = "E-mail incorreto"
            raise FileNotFoundError  
    else:
        erro= "Por favor, digite sim ou não."
        raise ValueError
    

    print("\nVocê está no ônibus ST23. Rota Vila Mariana.")
    while continua.lower() == "sim":
        print("\nDigite 1 para avaliar as condições do ônibus.\nDigite 2 para avaliar a rota atual.\nDigite 3 para avaliar sua experiência usando o aplicativo.\nDigite 4 para avaliar a pontualidade do ônibus.\nDigite 5 para entrar em contato com o SAC.")
        escolha = input()

# menu de escolhas
        if escolha not in avaliados:
            if escolha == "1":
                erro = recebeNota("condição do ônibus",msgFinal,positivos,negativos)
                if erro:
                    raise ValueError

            elif escolha == "2":
                erro = recebeNota("rota atual",msgFinal,positivos,negativos)
                if erro:
                    raise ValueError

            elif escolha == "3":
                erro = recebeNota("experiência usando o aplicativo",msgFinal,positivos,negativos)
                if erro:
                    raise ValueError

            elif escolha == "4":
                erro = recebeNota("pontualidade do ônibus",msgFinal,positivos,negativos)
                if erro:
                    raise ValueError

            elif escolha == "5":
                print("\nInsira a mensagem.")
                sac = input()
                print("\nIremos responder o mais rápido possível. Obrigado por utilizar nossos serviços.")
                msgFinal.append(f"\nVocê contatou o SAC.\nMensagem enviada:{sac}")
                listaSac.append(f"\nContatou o SAC.\nMensagem enviada:{sac}")
            
            else:
                erro= "Por favor, digite uma opção válida."
                raise ValueError
            
            avaliados.append(escolha)
        else:
            print("\nVocê já avaliou este tópico.")
        
    #pergunta se quer continuar avaliando
        continua = input("\nVocê deseja fazer uma nova avaliação? (Digite 'sim' ou 'não') ")
        if continua.lower()!="sim" and continua.lower()!="não":
            erro= "Por favor, digite sim ou não."
            raise ValueError
        
    #exibe as mensagens finais
    with open(f'usuarios/{email}.json', 'r', encoding='utf-8') as arquivo:
        infocadastro = json.loads(arquivo.read())
    print("*" * 70)
    print("INFORMAÇÕES DO CLIENTE:")
    print(f"Nome: {infocadastro['nome']}")
    print(f"E-mail: {infocadastro['email']}")
    print("*" * 70)
    for i in range(len(msgFinal)):
        print(msgFinal[i])
    print("*" * 70)
    print("\nObrigada por avaliar os serviços da SmarTech.")

    #insera avaliações nos documentos de resumo de feedback
    insereFeedback(infocadastro['nome'],positivos,negativos,listaSac)
    

except ValueError:
    print(f"\n{erro}")
except FileNotFoundError:
    print(f"\n{erro}")
except FileExistsError:
    print(f"\n{erro}")

finally:
    print("Fim da sessão de feedback")
