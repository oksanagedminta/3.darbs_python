"""
Uzrakstiet programmu Python, lai aprēķinātu 
trīs ievadīto skaitļu summu.
Ja ievadītās vērtības ir vienādas, atgrieziet summu, trīskāršojot to.
"""
# ?? atgrieziet summu, trīskaršojot to ??
a=int(input(" Ievadiet 1. skaitli: "))
b=int(input(" Ievadiet 2. skaitli: "))
c=int(input(" Ievadiet 3. skaitli: "))
sum=a+b+c
if a==b==c:
    print(sum*3)
else: print(sum)