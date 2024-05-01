from classe import calculadora

if __name__ == "__main__":    
    sinal = input("escolha, '/':divisão,'*':multiplicação,'+':adição,'-':subtração")
    valor1 = int(input("por favor insira o primeiro valor:"))
    valor2 = int(input("por favor insira o segundo valor"))
    print(calculadora(sinal,valor1,valor2))

    
