def sum_of_squares(n:int)->int:
    sum=0
    for i in range(1,n+1):sum+=i*i
    return sum

def main():
    n = 10
    print(f"Sum of squares up to {n}:",sum_of_squares(n))

if __name__=="__main__":main()

def factorial(n):return 1 if n==0 else n*factorial(n-1)

list=[1,2,3,4]

def another_func():
    print("Hello, World!") 
