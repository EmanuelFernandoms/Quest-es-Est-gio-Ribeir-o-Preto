#------------- QUESTÃO 1

indice = 13
soma = 0
k = 0

while (k < indice):
    k = k + 1
    soma = soma + k

print(soma)

# o valor impresso sera 91
#------------- QUESTÃO 2

numero_informado = int(input("Informe um número: "))

numero_anterior = 0
numero_atual = 1

while numero_atual < numero_informado:
    numero_anterior = numero_atual
    numero_atual = numero_anterior + numero_atual

if numero_atual == numero_informado:
    print(f"O número {numero_informado} se encontra na sequência de Fibonacci")
else:
    print(f"O número {numero_informado} não se encontra na sequência de Fibonacci")

#------------- QUESTÃO 5

string = "tranquilo"
string_invertida = ""

for i in range(len(string)):
    string_invertida = string[i] + string_invertida

print("String invertida:", string_invertida)
