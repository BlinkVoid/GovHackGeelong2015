from stormwatermonitor.helpers import fish

def checkspill(type):
	if type == "oil":
		return """A""" + fish.text() + """has ingested some oil! Oil and other organic hydrocarbons are toxic to lots of species  and build up through the food chain."""
	
	elif type == "detergent":
		return "A" + fish.text() + """ has got some detergent on its skin! Detergents can damage gills and the mucus layer that protects fish from infection. Some detergents also contain high levels of phosphorus nutrients, that encourage algal blooms. """

	elif type == "duck":
		return """Your rubber duckie has floated out to sea. Eventually it will break down into smaller pieces, small enough for birds, fish and seals to eat. Plastic doesn't provide any nutrition and can kill animals.It can break down further into tiny particles called 'microplastics'."""

def spill(type):
	result = "<div id='info'>"
	result += checkspill(type)
	result += "</div>"
	return result