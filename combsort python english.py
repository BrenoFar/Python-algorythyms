from random import randrange 
def combsort(num):                 #Defining combsort as a function
    gap = len(num)
    swaps=True
    troca=0
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps=False                    #Turning off just to verify if had the swap
        for i in range(len(num) - gap):
            j = i+gap
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
                swaps=True
                if swaps:
                    troca=troca+1                      #counting the swaps
    print('Houve {0} troca(as)'.format(troca))         #telling to the user how much swaps happened


 
num_list = [75, 16, 55, 19, 48, 14, 2, 61, 22, 100]     #A pre-made list with 10 indexes
#listateste= [127,147,50,149,101] lista desordenada            #MANUALLY TESTING A LIST
#listateste= [101,147,50,149,127] intervalo como 4 V 1 troca   #GAP=4
#listateste= [101,127,50,149,147] intervalo como 3 V 1 troca   #GAP=3
#listateste= [50,127,101,149,147] intervalo como 2 V 1 troca   #GAP=2
#listateste= [50,101,127,147,149] intervalo como 1 V 2 troca   #GAP=1
#listateste= [50,101,127,147,149] lista ordenada

lista = []                                              #Empty list that we add some values
print('Choose one of those options!')
print('1- Pre-made list')
print('2- Define list length and the value')
print('3- Randomized list with X indexes defined by the user')
P1=int(input('\n'))                                    #Here we put one of those options (1, 2 or 3)

if P1 ==1 or P1 ==2 or P1==3:

    if P1==1:
        print('You choosed the Pre-made list.')
        print('Before: ',num_list)                                              #showing the before not sorted
        combsort(num_list)                                                      #calling the combsort now as a function apllying in the pre-made list "num_list"
        print('After: ',num_list)                                               #showing the list after being sorted

    elif P1==2:
        aux = int(input('Define your list length (ex: 1/10/50/30/100) \n'))
        contador = 0                                                          #counter
        while contador < aux:                                                 #will repeat until counter reaches aux value
            value=int(input('Write the {0}° value \n'.format(contador+1)))    #User must write the values (it will repeat until reaches the max in the while function)
            lista.append(value)                                               #adding the var value in the list
            contador = contador + 1                                           #counting one
        print("Before: ", lista)                                              #showing the before not sorted
        combsort(lista)                                                       #calling the combsort now as a function apllying in the empty list "lista"
        print("After:  ", lista)                                              #showing the list after being sorted
        print('\n')
    if P1==3:
        aux = int(input('Define your list length (ex: 1/10/50/30/100) \n'))
        contador = 0                                                                     #counter
        rangeusuario=(int(input('Type up which number can be randomized: \n')))          #The number that the var can randomize ex:1000 it will randomize between 0-1000
        while contador < aux:
            for f in range(1):
                value=randrange(rangeusuario)                                            #calling randrange function to randomize the value and keep it in 'rangeusuario' var
                lista.append(value)                                                      #addin the var value in the list
                contador= contador + 1                                                   #counting one
        print("Before ,",lista)                                                          #showing the before not sorted
        combsort(lista)                                                                  #calling the combsort now as a function applying in the empty list "lista"
        print("After: ",lista)                                                           #showing the list after being sorted
        print('\n')

else:
    print('Valor incorreto! FIM DO ALGORITMO.')                                          #It will not recognize other options and will end the algorythm
