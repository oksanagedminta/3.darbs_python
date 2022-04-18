"""
Uzrakstiet programmu Python, lai aprēķinātu 
trīs ievadīto skaitļu summu.
Ja ievadītās vērtības ir vienādas, atgrieziet summu, trīskāršojot to.
"""
# Nr.1 ar FUNKCIJU def
def plus(x,y,z):
    plus=x+y+z
    if x==y==z:
        return plus*3
meginu=plus(2,2,2)
print(meginu)

# Nr.2
a=int(input(" Ievadiet 1. skaitli: "))
b=int(input(" Ievadiet 2. skaitli: "))
c=int(input(" Ievadiet 3. skaitli: "))
sum=a+b+c
if a==b==c:
    print(sum*3)
else: print(sum)