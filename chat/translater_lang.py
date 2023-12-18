from translate import Translator

def en_to_ru(en_text):
	translator= Translator(from_lang="English",to_lang="russian")

	ru_text = translator.translate(en_text)

	return ru_text

def ru_to_en(ru_text):
	translator= Translator(from_lang="russian",to_lang="English")

	en_text = translator.translate(ru_text)

	return en_text
