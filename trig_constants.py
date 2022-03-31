# quick program by ron0studios
# prints a quick table of values for trigonometric constants

# GENERATOR
from tabulate import tabulate

headers = ["","0°","30°","45°","60°","90°"]

# \n—\n is just the dividing slash in a fraction
data = [["sin",0,"1\n—\n2","√2\n—\n2","√3\n—\n2",1],
        ["cos",1,"√3\n—\n2","√2\n—\n2","1\n—\n2",0],
        ["tan", 0,"√3\n—\n3","1","√3","∞"]]
 
print(tabulate(data,headers=headers,tablefmt="fancy_grid",numalign="center",stralign="center"))

