from os import system,name
def calculator(): #criar uma função
    
    while True: # while = loop
        system('cls') if(name == 'nt') else system('clear')
        print("Selecione a operação desejada:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair da Calculadora")
        choice = input("Informe sua escolha (1/2/3/4/5): ") #Variavel para armazenar resultado do menu
        

        if choice == "5": # se o choice for 5 ele ira quebrar o loo
            break
        elif choice == "1" or choice == "2" or choice == "3" or choice == "4":
            num1 = int(input("Informe o primeiro número: "))
            num2 = int(input("Informe o segundo número: "))

            if choice == "1":
                resultadoSoma = num1 + num2
                print(f"O resultado da soma {num1} + {num2} = {resultadoSoma}")
            elif choice == "2":
                resultadoSub = num1 - num2
                print(f"O resultado da Subtração {num1} - {num2} = {resultadoSub}")
            elif choice == "3":
                resultadoMult = num1 * num2
                print(f"O resultado da Multiplicação {num1} * {num2} = {resultadoMult}")
            elif choice == "4":
                resultadoDivi = num1 / num2
                print(f"O resultado da Divisão {num1} / {num2} = {resultadoDivi}")
        else:
            print("Escolha inválida, tente novamente")
            


        input("Aperte Enter para continuar")
        system('cls') if(name == 'nt') else system('clear')

    system('cls') if(name == 'nt') else system('clear')
#termino da função

#chamada da função
calculator() 
