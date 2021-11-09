#  Execute para visualizar

# Declarar listas:
numbers=[1,2,3,4,5,6] #Posições 0,1,2,3,4,5, respectivamente
print(numbers)

# Acessar números:
print(numbers[0]) 
print(numbers[-1]) #Acessa o ultimo indice
print(numbers[-2]) #Acessa o penultimo indice

# Tamanho da lista
print(len(numbers))

# Acrescentar ou remover elementos na listas
del(numbers[0])         # Deletar 
print(numbers)

numbers.append(4)       # Adiciona ao final da lista
print(numbers)

numbers.insert(0,125)   # Adiciona no indice 0 o número 125 e "empurra" os outros números pra frente
print(numbers,"\n")

# Troca de dados entre listas
newList = numbers       # Copiar lista toda
print(newList)

newList = numbers[1:4]  # Copiar parte da lista, do índice 1 ao 4
print(newList)

numbers2 = [10,20,30,40,50,60]
numbers3 = [100,200,300,400,500,600]
numbers4 = [1000,2000,3000,4000,5000,6000]

numbers[0], numbers2[1] = numbers3[3], numbers4[5] # numbers recebe de numbers3 ---- numbers2 recebe de numbers4

print (numbers,numbers2,numbers3,numbers4,"\n")

# Organizar lista
numbers.sort() #Menor para o maior
print(numbers)

numbers.reverse() #Maior para o menor
print(numbers)