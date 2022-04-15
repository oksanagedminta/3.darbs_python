"""
Uzrakstiet Python programmu, lai iegūtu 
starpību starp ievadīto skaitli un 17.
Ja skaitlis ir lielāks par 17, iegūstiet absolūtās starpības 
dubultu.
"""
# !!Nesaprotu uzdevumu!!!

x=int(input("Ievadiet skaitli: "))
if x >17:
    print((x-17)*2)
else: print(17-x)