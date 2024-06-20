from cat.mad_hatter.decorators import tool, hook

@tool(examples = ['tabellina', 'dimmi la tabellina'], return_direct=True)
def calcola_tabellina(tool_input, cat):
	"""
	Calcola la tabellina del numero dato in input. 
	L'input è sempre il numero di cui calcolare la tabellina.
	Calcolo matematico della tabellina.
	"""
	print("Calcolo la tabellina del " + str(tool_input))
	result = ""
	for i in range (1, 11):
		result += "\n" + str(tool_input) + " * " + str(i) + " = " + str(int(tool_input) * i)

	return "la tabellina del " + tool_input + " è: " + result