from cat.mad_hatter.decorators import tool, hook


@hook(priority = 1)  # priorità più alta = sovrappone il resto
def agent_prompt_prefix(prefix, cat):
	settings = cat.mad_hatter.get_plugin().load_settings()
	prefix = settings['prefix']

	return prefix