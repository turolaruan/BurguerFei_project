import os
import datetime

now = datetime.datetime.now()
data = now.strftime("%Y-%m-%d %H:%M")
total = 0
total_cancel = 0

def verificacao_cadastro(): #função que pergunta se ja possui cadastro
    cadastro = input("Já está cadastrado?(Sim/Não)")
    print()
    if cadastro == "Não":
        print("Cadastre-se agora!!")
        cadastrar_novo() # cria seu cadastro ao entrar na função
    elif cadastro == "Sim":
        login() # faz seu login ao entrar na função

def verificar_CPFeSenha(funcao): #função que verifica o CPF e a Senha
    CPF = str(input("Digite o CPF: "))
    Senha = str(input("Digite a senha: "))

    cliente = open("{}.txt".format(CPF),"r")# abre o arquivo para ler

    for linha in cliente.readlines(): #lê as linhas de CPF e Senha e verifica o estão corretos
        if "CPF" in linha:
            if CPF == linha.replace("CPF: ", "").replace("\n", "").replace(" ", ""):
                CPF = "Ok"
        
        if "Senha" in linha:
            if Senha == linha.replace("Senha: ", "").replace("\n", "").replace(" ", ""):
                Senha = "Ok"

    if CPF == "Ok" and Senha == "Ok": # caso o CPF e a Senha estiverem corretos o codigo continua
        print()
        print("Verificacao feita com sucesso!")
        print()
        funcao()
    else: # se o CPF e Senha estiverem errados é chamada a função de verificar o cadastro
        print()
        print("Falha na verificacao!") 
        print()
        verificacao_cadastro()
    cliente.close()# fecha o arquivo

def login(): #função que faz o login
    verificar_CPFeSenha(menu) # verifica o login e entra no menu

def novo_pedido(): #função que cria um novo pedido e chama o menu de pedidos
    menu_pedido()

def skip():
    return

def cancelar_pedido(): #função que cancela o pedido
    print("Digite seu CPF novamente!")
    CPF = int(input("Digite o CPF: "))
    cliente = open("{}.txt".format(CPF),"w")# abre o arquivo para escrever,apagando tudo dentro do arquivo
    print("Pedido cancelado!")
    cliente.close()# fecha o arquivo
    print("Cadastre-se novamente para fazer um novo pedido!")
    print("==================================================")
    verificacao_cadastro()

def inserir_produto(): #função para inserir um novo produto,ela chama o menu de pedidos
    menu_pedido()
    
def valor_total(): #função que mostra o total do pedido
    print("Digite seu CPF novamente!")
    CPF = str(input("Digite o CPF: "))
    cliente = open("{}.txt".format(CPF),"r")# abre o arquivo para ler
    text = cliente.readlines()
    cliente.close()# fecha o arquivo
    text[3] = "Total: R$%.2f\n" % (total - total_cancel)
    cliente = open("{}.txt".format(CPF),"w")#atualiza o valor total do pedido
    for elementos in text:
        cliente.write(elementos)
    cliente.close()# fecha o arquivo
    print("Total a pagar: R$%.2f" % (total - total_cancel)) # imprimi o total do pedido
    print("===========================================")
    menu()

def menu_pedido(): #função que mostra o menu de pedidos e adiciona produtos ao pedido
    global total
    print("==================================================")
    print("                  Menu de Pedidos                  ")
    print("==================================================")
    print("Codigo: 1 ----- X-Salada -------------- R$10,00")
    print("Codigo: 2 ----- X-burger -------------- R$10,00")
    print("Codigo: 3 ----- Cachorro quente ------- R$7,50")
    print("Codigo: 4 ----- Misto quente ---------- R$8,00")
    print("Codigo: 5 ----- Salada de Frutas ------ R$5,50")
    print("Codigo: 6 ----- Refrigerante ---------- R$4,50")
    print("Codigo: 7 ----- Suco Natural ---------- R$6,25")
    print("==================================================")
    print()

    print("Digite seu CPF novamente!")
    CPF = str(input("Digite o CPF: "))
    pedido = int(input("Pedido desejado: "))
    quant = int(input("Quantidade desejada: "))
    cliente = open("{}.txt".format(CPF),"a")# abre o arquivo para adicionar os produtos 

    produtos = {1 :str(quant)+" - "+"X-Salada "+" Preco unitario: "+ " 10.00 "+" Valor: "+" + "+ str(quant*10.00) + " - " + "Codigo: 1",
                2 :str(quant)+" - "+"X-burger "+" Preco unitario: "+" 10.00 "+" Valor: "+" + "+ str(quant*10.00)+ " - " + "Codigo: 2",
                3 :str(quant)+" - "+"Cachorro quente "+" Preco unitario: "+" 7.50 "+" Valor: "+" + "+ str(quant*7.50)+ " - " + "Codigo: 3",
                4 :str(quant)+" - "+"Misto quente "+" Preco unitario: "+" 8.00 "+" Valor: "+" + "+str(quant*8.00)+ " - " + "Codigo: 4",
                5 :str(quant)+" - "+"Salada de Frutas "+" Preco unitario: "+" 5.50 "+" Valor: "+" + "+str(quant*5.50)+ " - " + "Codigo: 5",
                6 :str(quant)+" - "+"Refrigerante "+" Preco unitario: "+" 4.50 "+" Valor: "+" + "+str(quant*4.50)+ " - " + "Codigo: 6",
                7 :str(quant)+" - "+"Suco Natural "+" Preco unitario: "+" 6.25 "+" Valor: "+" + "+str(quant*6.25)+ " - " + "Codigo: 7"}

    p = produtos.values()
    d = list(p)

    pedidos1 = []
    pedidos2 = []
    pedidos3 = []
    pedidos4 = []
    pedidos5 = []
    pedidos6 = []
    pedidos7 = []

    if pedido == 1: #adiciona o X-Salada ao pedido e no arquivo
        pedidos1.append(d[0])
        print("X-Salada adicionado com sucesso!")
        total = total + (quant * 10.00)
        for i in pedidos1:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        outro_prod = input("Deseja adicionar outro produto?(Sim/Não)")
        if outro_prod == "Sim":
            menu_pedido()
        elif outro_prod == "Não":
            menu()

    elif pedido == 2: #adiciona o X-burger ao pedido e no arquivo
        pedidos2.append(d[1])
        print("X-burger adicionado com sucesso!")
        total = total + (quant * 10.00)
        for i in pedidos2:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        outro_prod = input("Deseja adicionar outro produto?(Sim/Não)")
        if outro_prod == "Sim":
            menu_pedido()
        elif outro_prod == "Não":
            menu()

    elif pedido == 3: #adiciona o Cachorro quente ao pedido e no arquivo
        pedidos3.append(d[2])
        print("Cachorro quente adicionado com sucesso!")
        total = total + (quant * 7.50)
        for i in pedidos3:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        outro_prod = input("Deseja adicionar outro produto?(Sim/Não)")
        if outro_prod == "Sim":
            menu_pedido()
        elif outro_prod == "Não":
            menu()
        
    elif pedido == 4: #adiciona o Misto quente ao pedido e no arquivo
        pedidos4.append(d[3])
        print("Misto quente adicionado com sucesso!")
        total = total + (quant * 8.00)
        for i in pedidos4:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        outro_prod = input("Deseja adicionar outro produto?(Sim/Não)")
        if outro_prod == "Sim":
            menu_pedido()
        elif outro_prod == "Não":
            menu()

    elif pedido == 5: #adiciona o Salada de Frutas ao pedido e no arquivo
        pedidos5.append(d[4])
        print("Salada de Frutas adicionado com sucesso!")
        total = total + (quant * 5.50)
        for i in pedidos5:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        outro_prod = input("Deseja adicionar outro produto?(Sim/Não)")
        if outro_prod == "Sim":
            menu_pedido()
        elif outro_prod == "Não":
            menu()
    
    elif pedido == 6: #adiciona o Refrigerante ao pedido e no arquivo
        pedidos6.append(d[5])
        print("Refrigerante adicionado com sucesso!")
        total = total + (quant * 4.50)
        for i in pedidos6:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        outro_prod = input("Deseja adicionar outro produto?(Sim/Não)")
        if outro_prod == "Sim":
            menu_pedido()
        elif outro_prod == "Não":
            menu()
        
    elif pedido == 7: #adiciona o Suco Natural ao pedido e no arquivo
        pedidos7.append(d[6])
        print("Suco Natural adicionado com sucesso!")
        total = total + (quant * 6.25)
        for i in pedidos7:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        outro_prod = input("Deseja adicionar outro produto?(Sim/Não)")
        if outro_prod == "Sim":
            menu_pedido()
        elif outro_prod == "Não":
            menu()

def remover_produto(): #função que cancela os pedidos e também cancela no arquivo
    global total_cancel
    print("Digite seu CPF novamente!")
    CPF = str(input("Digite o CPF: "))
    print()
    print("==================================================")
    print("                  Menu de Pedidos                  ")
    print("==================================================")
    print("Codigo: 1 ----- X-Salada -------------- R$10,00")
    print("Codigo: 2 ----- X-burger -------------- R$10,00")
    print("Codigo: 3 ----- Cachorro quente ------- R$7,50")
    print("Codigo: 4 ----- Misto quente ---------- R$8,00")
    print("Codigo: 5 ----- Salada de Frutas ------ R$5,50")
    print("Codigo: 6 ----- Refrigerante ---------- R$4,50")
    print("Codigo: 7 ----- Suco Natural ---------- R$6,25")
    print("==================================================")
    print()

    pedido_cancelar = int(input("Qual pedido deseja Cancelar: "))
    quantidade_cancelar = int(input("Quantidade que deseja cancelar: "))
    cliente = open("{}.txt".format(CPF),"a")# abre o arquivo para adicionar os produtos cancelados

    produtos_cancel = {1 :str(quantidade_cancelar)+" - "+"X-Salada "+" Preco unitario: "+ " 10.00 "+" Valor: "+" - "+ str(quantidade_cancelar*10.00) + " - " + "Cancelado" + " - " + "Codigo: 1",
                2 :str(quantidade_cancelar)+" - "+"X-burger "+" Preco unitario: "+" 10.00 "+" Valor: "+" - "+ str(quantidade_cancelar*10.00) + " - " + "Cancelado" + " - " + "Codigo: 2",
                3 :str(quantidade_cancelar)+" - "+"Cachorro quente "+" Preco unitario: "+" 7.50 "+" Valor: "+" - "+ str(quantidade_cancelar*7.50) + " - " + "Cancelado" + " - " + "Codigo: 3",
                4 :str(quantidade_cancelar)+" - "+"Misto quente "+" Preco unitario: "+" 8.00 "+" Valor: "+" - "+str(quantidade_cancelar*8.00) + " - " + "Cancelado" + " - " + "Codigo: 4",
                5 :str(quantidade_cancelar)+" - "+"Salada de Frutas "+" Preco unitario: "+" 5.50 "+" Valor: "+" - "+str(quantidade_cancelar*5.50) + " - " + "Cancelado" + " - " + "Codigo: 5",
                6 :str(quantidade_cancelar)+" - "+"Refrigerante "+" Preco unitario: "+" 4.50 "+" Valor: "+" - "+str(quantidade_cancelar*4.50) + " - " + "Cancelado" + " - " + "Codigo: 6",
                7 :str(quantidade_cancelar)+" - "+"Suco Natural "+" Preco unitario: "+" 6.25 "+" Valor: "+" - "+str(quantidade_cancelar*6.25) + " - " + "Cancelado" + " - " + "Codigo: 7"}

    prod = produtos_cancel.values()
    dic = list(prod)

    produtos_cancel1 = []
    produtos_cancel2 = []
    produtos_cancel3 = []
    produtos_cancel4 = []
    produtos_cancel5 = []
    produtos_cancel6 = []
    produtos_cancel7 = []

    if pedido_cancelar == 1: #cancela o X-Salada do pedido e do arquivo
        produtos_cancel1.append(dic[0])
        print("X-Salada cancelado com sucesso!")
        total_cancel = total_cancel + (quantidade_cancelar * 10.00)
        for i in produtos_cancel1:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        cancelar_outro_prod = input("Deseja cancelar outro produto?(Sim/Não)")
        if cancelar_outro_prod == "Sim":
            remover_produto()
        elif cancelar_outro_prod == "Não":
            menu()

    if pedido_cancelar == 2: #cancela o X-burger do pedido e do arquivo
        produtos_cancel2.append(dic[1])
        print("X-burger cancelado com sucesso!")
        total_cancel = total_cancel + (quantidade_cancelar * 10.00)
        for i in produtos_cancel2:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        cancelar_outro_prod = input("Deseja cancelar outro produto?(Sim/Não)")
        if cancelar_outro_prod == "Sim":
            remover_produto()
        elif cancelar_outro_prod == "Não":
            menu()

    if pedido_cancelar == 3: #cancela o Cachorro quente do pedido e do arquivo
        produtos_cancel3.append(dic[2])
        print("Cachorro quente cancelado com sucesso!")
        total_cancel = total_cancel + (quantidade_cancelar * 7.50)
        for i in produtos_cancel3:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        cancelar_outro_prod = input("Deseja cancelar outro produto?(Sim/Não)")
        if cancelar_outro_prod == "Sim":
            remover_produto()
        elif cancelar_outro_prod == "Não":
            menu()

    if pedido_cancelar == 4: #cancela o Misto quente do pedido e do arquivo
        produtos_cancel4.append(dic[3])
        print("Misto quente cancelado com sucesso!")
        total_cancel = total_cancel + (quantidade_cancelar * 8.00)
        for i in produtos_cancel4:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        cancelar_outro_prod = input("Deseja cancelar outro produto?(Sim/Não)")
        if cancelar_outro_prod == "Sim":
            remover_produto()
        elif cancelar_outro_prod == "Não":
            menu()

    if pedido_cancelar == 5: #cancela o Salada de Frutas do pedido e do arquivo
        produtos_cancel5.append(dic[4])
        print("Salada de Frutas cancelado com sucesso!")
        total_cancel = total_cancel + (quantidade_cancelar * 5.50)
        for i in produtos_cancel5:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        cancelar_outro_prod = input("Deseja cancelar outro produto?(Sim/Não)")
        if cancelar_outro_prod == "Sim":
            remover_produto()
        elif cancelar_outro_prod == "Não":
            menu()

    if pedido_cancelar == 6: #cancela o Refrigerante do pedido e do arquivo
        produtos_cancel6.append(dic[5])
        print("Refrigerante cancelado com sucesso!")
        total_cancel = total_cancel + (quantidade_cancelar * 4.50)
        for i in produtos_cancel6:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        cancelar_outro_prod = input("Deseja cancelar outro produto?(Sim/Não)")
        if cancelar_outro_prod == "Sim":
            remover_produto()
        elif cancelar_outro_prod == "Não":
            menu()

    if pedido_cancelar == 7: #cancela o Suco Natural do pedido e do arquivo
        produtos_cancel7.append(dic[6])
        print("Suco Natural cancelado com sucesso!")
        total_cancel = total_cancel + (quantidade_cancelar * 6.25)
        for i in produtos_cancel7:
            cliente.write(i+"\n")
            cliente.close()# fecha o arquivo
        cancelar_outro_prod = input("Deseja cancelar outro produto?(Sim/Não)")
        if cancelar_outro_prod == "Sim":
            remover_produto()
        elif cancelar_outro_prod == "Não":
            menu()

def extrato(): #função que exibe o extrato
    print("Digite seu CPF novamente!")
    CPF = str(input("Digite o CPF: "))
    cliente = open("{}.txt".format(CPF),"r")
    text = cliente.readlines()
    cliente.close()
    text[4] = "Data: %s\n" % str(now.strftime("%Y-%m-%d %H:%M"))#atualiza a data e hora do pedido
    cliente = open("{}.txt".format(CPF),"w")# abre o arquivo para escrever
    for elementos in text:
        cliente.write(elementos)
    cliente.close()# fecha o arquivo
    print()
    print("==================================================")
    print()
    cliente = open("{}.txt".format(CPF),"r")# abre o arquivo para ler
    a = (cliente.read())
    print(a)
    cliente.close()# fecha o arquivo
    print("==================================================")
    print()
    ped = input("Quer fazer um novo pedido?(Sim/Não)") #se a resposta for "Sim" abre o menu,se "Não" fecha o programa
    print()
    if ped == "Sim": 
        menu()
    elif ped == "Não":
        pass

def cadastrar_novo(): #função que cria o cadastro para o cliente
    print()
    Nome = input("Digite seu nome: ") 
    CPF = int(input("Digite o CPF: "))
    Senha = int(input("Digite a senha: "))
    print(os.getcwd())
    cliente = open("{}.txt".format(CPF),"w") # abri o arquivo para escrver dentro dele
    cliente.write("Nome: %s \n" % (Nome)) #escreve o nome no arquivo
    cliente.write("CPF: %s \n" % (CPF)) #escreve o CPF no arquivo
    cliente.write("Senha: %s \n" % (Senha)) #escreve o Senha no arquivo
    cliente.write("Total: R$%.2f\n" % (total - total_cancel)) #escreve o Total no arquivo
    cliente.write("Data: %s\n" % str(now.strftime("%Y-%m-%d %H:%M")))#escreve a data no arquivo
    cliente.write("Itens do pedido: \n")#escreve Itens do pedido no arquivo
    cliente.close() # fecha o arquivo
    if CPF == CPF:
        print("Já existe um pedido nesse CPF!")
        menu()
    else:
        menu()

def menu(): #função que exibe o menu de funcoes
    while True:
        print("==================================================")
        print("                  Menu de Funcoes                  ")
        print("==================================================")
        print("1 - Novo pedido")
        print("2 - Cancelar pedido")
        print("3 - Inserir produto")
        print("4 - Cancela produto")
        print("5 - Valor do pedido")
        print("6 - Extrato do pedido")
        print()
        print("0 - Sair")
        print("===========================================")
        print()
        opcao = int(input("Opção desejada: "))
        if opcao == 1:
            print("Verifique seu login:")
            verificar_CPFeSenha(novo_pedido) #chama a função de verificar o login e entra na função de novo pedido
            break
        elif opcao == 2:
            print("Verifique seu login:")
            verificar_CPFeSenha(cancelar_pedido) #chama a função de verificar o login e entra na função que cancela o pedido
            break
        elif opcao == 3:
            print("Verifique seu login:")
            verificar_CPFeSenha(inserir_produto) #chama a função de verificar o login e entra na função que insere produto no pedido
            break
        elif opcao == 4:
            print("Verifique seu login:")
            verificar_CPFeSenha(remover_produto) #chama a função de verificar o login e entra na função que cancela um produto do pedido
        elif opcao == 5:
            print("Verifique seu login:")
            verificar_CPFeSenha(valor_total) #chama a função de verificar o login e entra na função que exibi o valor total para pagar do pedido
            break
        elif opcao == 6:
            print("Verifique seu login:")
            verificar_CPFeSenha(extrato) #chama a função de verificar o login e entra na função que exibe o extrato do pedido
            break
        elif opcao == 0:
            print("Você saiu!")
            break

def main(): #função que inicia o programa
    print("==================================================")
    print("                  BurgerFEI                  ")
    print("==================================================")
    verificacao_cadastro() #chama função para criar o cadastro ou fazer login
main()