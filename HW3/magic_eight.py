def ask_question():
	question = input("What is your question?\n")
	return question
    
if __name__ == "__main__":
	while True:
		question = ask_question()
		if question == "quit":
			break
		if question[-1]!='?':
			print("I’m sorry, I can only answer questions")
		else:
			print(8ball_answer())
			break