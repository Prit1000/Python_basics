# FRACTORIAL NUMBER
def factorial(k):
    if k==0 or k==1:
        return 1
    else:
        return k * factorial(k-1)
    
def factorial_print(k):
    h=factorial(k)
    print(f"The Factorial of {k} is {h}")
factorial_print(6)
'''
The Factorial of 6 is 720
'''

def even_odd(k):
    if k % 2 == 0:
        return "even"
    else:
        return "odd"
    
def print_even_or_odd(k):
    m = even_odd(k)
    print(f"{k} is {m}")
print_even_or_odd(53)
'''
53 is odd
'''
s="Khbjj Hjsoijncc odnjnG"
print(s[::-1])
v="aeiouAEIOU"
print(sum(1 for i in s if i in v))
k=s.lower().replace(" ","")
print(k[::-1])
'''
Gnjndo ccnjiosjH jjbhK
3
gnjndoccnjiosjhjjbhk
'''
