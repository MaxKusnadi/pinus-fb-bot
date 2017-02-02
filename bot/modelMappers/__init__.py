import bot.constants.error
import bot.constants.value

def is_input_alphabet(name):
	return name.isalpha()

def is_input_alphanumeric(name):
	return name.isalnum()

def is_name_valid(name):
	if not is_input_alphabet(name):
		raise ValueError(NOT_ALPHABETICAL.format("Name"), name)
	return True

def is_fb_id_valid(name):
	if not is_input_alphanumeric(name):
		raise ValueError(NOT_ALPHANUMERIC.format("FB ID"), name)
	return True

def is_user_args_valid(fb_id, first_name, last_name):
	fb_id_valid = is_fb_id_valid(fb_id)
	is_first_name = (first_name == EMPTY_STRING) or 
					(first_name != EMPTY_STRING and is_name_valid(first_name))
	is_last_name = (last_name == EMPTY_STRING) or
				   (last_name != EMPTY_STRING and is_name_valid(last_name))
	
	return fb_id_valid and is_first_name and is_last_name:
	