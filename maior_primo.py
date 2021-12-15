def maior_primo(x):
    primo = 0
    contPrimo = 0
    
    if(x < 2):
        return "Valor digitado incorreto"

    def is_primo(x):
        cont = 1
        while (cont <= x):
            if(x % cont == 0):
                primo = cont
                contPrimo += 1
                print(primo)
            cont += 1
        if(contPrimo <= 2):
            print("é primo",primo)
        
