def ask_question():
	question = input("What is your question?\n")
	return question

possible_answers = ['It is certain.', 'it is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.',
                    'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.',
                    "Don't count on it.", "My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]


def 8ball_answer():
        x = random.choice(possible_answers)
        return x
=======
    
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

