def Fnct(string):
    a = 0
    b = 1

    while b<(len(string)):
        x = int(string[a])
        y = int(string[b])

        z = x + y

    
        if z > 9:
            a += 1
            b += 1
            
        else:
            string = string[:a] + str(z) + string[b+1:]        

    print(string)

number2 = str(1119812)

Fnct(number2)

number1 = str(32581)

Fnct(number1)
