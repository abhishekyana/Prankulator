# A file to make the prankulator.py
Text = """print("Enter number into the prankulator and get it calculated")
a = int(input("enter your first number[Currently supports 1 to 100 only]: "))
s = input("enter the operation you want the prankulator to perform(*,+,-,/):")
b = int(input("enter your second number[Currently supports 1 to 100 only]: "))
"""

def mulstr(a,b,s):
	if s=='*':
		return a*b
	if s=='+':
		return a+b
	if s=='-':
		return a-b
	if s=='/':
		return a/b

for s in ['*','+','-','/']:
	for i in range(1, 101):
		for j in range(1, 101):
			text = f"if a=={i} and s=='{s}' and b=={j}:\n\tprint(f'{i}{s}{j}={mulstr(i,j,s)}')\n"
			Text+=text
Text+=f"else:\n\tprint(f'{i},{s},{j}!! Please enter a valid number:')\n"
with open('prankulatormain.py','w') as file:
	file.write(Text)
