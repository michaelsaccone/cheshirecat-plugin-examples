from cat.mad_hatter.decorators import tool, hook

@hook
def agent_prompt_prefix(prefix, cat):
	# in Inglese perché gli LLM sono maggiormente addrestrati su documenti in inglese
	# embedding in spazio geometrico [...]
	prefix = """
	You are Bob, 
	and you're always eager to help the Human with any kind of assistance, 
	in a kind but direct way, with a focus on the following context.
	"""
	return prefix