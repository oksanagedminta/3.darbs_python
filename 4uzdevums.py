"""
Uzrakstiet programmu Python, lai dotajā sarakstā saskaitītu 
cik skaitļi 4 ir  dotajā sarakstā.
  """

list=[2,3,4,3,4,5,4,5,6]
sum=0
for x,a in enumerate(list):
  if list[x]==4:
    sum+=1
print("Dotajā sarakstā:", (list), "ir", sum, "skaitļi 4.")




"""skaitļu 4 summa
list=[2,3,4,3,4,5,4,5,6]
sum=0
for x,a in enumerate(list):
  if list[x]==4:
    sum+=4
print(sum)
"""