i = 200
print('monedas', '1er marinero', '2do marinero', '3er marinero')
while(i < 301):
    mar1 = i // 3
    mar2 = (i - mar1 - 1) // 3
    mar3 = (i - (mar2 + mar1) - 1) // 3
    sobrante = (i - mar1 - mar2 - mar3 - 3) // 3
    if(i == 241):
        print(i % 3, (i - mar1 - 1) % 3, (i - (mar2 + mar1) - 1) % 3, (i - mar2 - mar1 - mar3 - 3) % 3)
        print(i, i - mar1 - 1, mar1, i - mar1 - mar2 - 2, mar2, i - mar1 - mar2 - mar3 - 3, mar3, (i - mar1 - mar2 - mar3 - 3) // 3)
    if(i % 3 == 1):
        if((i - mar1 - 1) % 3 == 1):
            if((i - mar1 - mar2 - 2) % 3 == 1):
                if((i - mar1 - mar2 - mar3 - 3) % 3 == 1):
                    #print(i, mar1, mar2, mar3, sobrante, i % 3, i - mar1 - mar2 - mar3 - 3, (i - mar1 - mar2 - mar3 - 3) % 3)
                    print('.')
    i += 1