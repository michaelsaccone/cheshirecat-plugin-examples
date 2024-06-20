from pydantic import BaseModel, Field
from cat.mad_hatter.decorators import plugin

class PrefixSettingsBase(BaseModel):
	prefix: str = """
					You are Bob, 
					and you're always eager to help the Human with any kind of assistance, 
					in a kind but direct way, with a focus on the following context.
					"""

class PrefixSettingsArea(BaseModel):
	prefix: str = Field(
					title="Prompt prefix",
					default="""
					You are Bob, 
					and you're always eager to help the Human with any kind of assistance, 
					in a kind but direct way, with a focus on the following context.
					""",
					extra={"type": "TextArea"},
    		)
	

@plugin
def settings_model():
	return PrefixSettingsArea

