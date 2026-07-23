def main():
    n = int(input("whats n: "))
    x = factorial(n)
    print(x)



def factorial(n):
    
    if n == 0:
        return 1
    else:
        return(n * factorial(n-1))
        

main()