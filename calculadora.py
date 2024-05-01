def calculadora(sign,num1,num2):
    operadores = {
      "+": lambda op1, op2: op1 + op2,
      "-": lambda op1, op2: op1 - op2,
      "*": lambda op1, op2: op1 * op2,
      "/": lambda op1, op2: op1 / op2
    }
    return operadores[sign](num1, num2)

