RU = "ru"
EN = "en"
SETTING_LAN = EN

# Источник: https://docs.gpt4all.io/gpt4all_chat.html#server-mode

# No module named openai будет выпадать если запустить код командой: sudo python3 api_gpt.py - из под sudo не запускай!
import openai
import translater_lang

openai.api_base = "http://localhost:4891/v1"
#openai.api_base = "https://api.openai.com/v1"

openai.api_key = "not needed for a local LLM"

# Set up the prompt and other parameters for the API request
# prompt = "Who is Michael Jordan?"

# model = "gpt-3.5-turbo"
#model = "mpt-7b-chat"
model = "gpt4all-j-v1.3-groovy"


# Make the API request
def get_answer_gpt(question, lang=SETTING_LAN):
	answer = ""
	if lang == RU:
		prompt = translater_lang.ru_to_en(question)
	if lang == EN:
		prompt = question
		
	response = openai.Completion.create(
	    model=model,
	    prompt=prompt,
	    max_tokens=50,
	    temperature=0.28,
	    top_p=0.95,
	    n=1,
	    echo=True,
	    stream=False
	)
	
	if lang == RU:
		answer = translater_lang.en_to_ru(response["choices"][0]["text"])
	if lang == EN:
		answer = response["choices"][0]["text"]
		
	return answer

# Print the generated completion
#while True:
#	print(get_answer_gpt(input(">> ")))
