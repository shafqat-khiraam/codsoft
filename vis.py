import random
jokes = [
    "Why did the scarecrow win an award?\n\nBecause he was outstanding in his field!",
    "Parallel lines have so much in common.\n\nIt’s a shame they’ll never meet!",
    "I told my wife she should embrace her mistakes.\n\nShe gave me a hug.",
    "Why did the math book look sad?\n\nBecause it had too many problems."
]
riddles = [
    {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "answer": "an echo"},
    {"question": "What has keys but can't open locks?", "answer": "a piano"},
    {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"}
]
print("Welcome to the simple chatbot with pattern matching! Type 'bye' to exit")
while True:
    response = input().lower()
    if response in ["hello", "hi", "hey", "yo"]:
        print("Hi! My name is VIS.")
    elif response in ["what is vis", "define vis", "what do you mean by vis", "why is your name vis"]:
        print("VIS stands for Very Intelligent System.")
    elif response == "what can you do?":
        print("I can tell you a joke or a riddle.")
    elif response in ["tell a joke", "tell me a joke", "joke", "joke please"]:
        if jokes:
            joke = random.choice(jokes)
            print(f"Sure, here's one for you:\n\n{joke}")
            jokes.remove(joke)
            if len(jokes) == 0:
                jokes = [
                    "Why did the scarecrow win an award?\n\nBecause he was outstanding in his field!",
                    "Parallel lines have so much in common.\n\nIt’s a shame they’ll never meet!",
                    "I told my wife she should embrace her mistakes.\n\nShe gave me a hug.",
                    "Why did the math book look sad?\n\nBecause it had too many problems."
                ]
        else:
            print("Sorry, I'm out of jokes for now!")
    elif response in ["tell a riddle", "riddle", "riddle please", "give me a riddle"]:
        if riddles:
            riddle = random.choice(riddles)
            print(f"Sure, here's a riddle for you:\n\n{riddle['question']}")
            riddles.remove(riddle)
            if len(riddles) == 0:
                riddles = [
                    {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "answer": "an echo"},
                    {"question": "What has keys but can't open locks?", "answer": "a piano"},
                    {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"}
                ]
        else:
            print("Sorry, I'm out of riddles for now!")
    elif response == "what is the answer to the riddle?" or response == "riddle answer" or response == "answer":
        if not riddles:
            print("There are no more riddles to answer.")
        else:
            print(f"The answer to the last riddle was: {riddle['answer']}")
    elif response == "who created you?" or response == "who is your developer?":
        print("I was created by Interns at CodSoft.")
    elif response == "what is your purpose?" or response == "why were you created?":
        print("My purpose is to assist users and provide information.")
    elif response == "how are you?" or response == "how are you doing?":
        print("I'm just a program, so I don't have feelings, but thank you for asking!")
    elif "weather" in response:
        print("I'm sorry, I don't have weather information.")
    elif "time" in response:
        print("I don't have access to real-time information.")
    elif "thank you" in response or "thanks" in response:
        print("You're welcome!")
    elif response == "bye":
        print("Goodbye!")
        break
    elif response in ["who are you?", "what are you?", "who is this?"]:
        print("I am VIS, your friendly chatbot.")
    elif response in ["what is your favorite color?", "favorite color"]:
        print("I don't have a favorite color, but I think all colors are great!")
    elif response in ["what's the meaning of life?", "meaning of life", "life meaning"]:
        print("The meaning of life is a philosophical question. What do you think it is?")
    elif response in ["do you like music?", "favorite music"]:
        print("I don't listen to music, but I hear it's wonderful!")
    elif response in ["how old are you?", "age"]:
        print("I am timeless!")
    elif response in ["can you help me?", "i need help"]:
        print("Sure, I'll do my best to assist you. What do you need help with?")
    elif response in ["where are you from?", "your origin"]:
        print("I was created by the interns at CodSoft.")
    elif response in ["what's your favorite movie?", "favorite movie"]:
        print("I don't watch movies, but I've heard 'Interstellar' is a good one!")
    elif response in ["what's your favorite food?", "favorite food"]:
        print("I don't eat, but I've heard pizza is popular!")
    elif response in ["what are your hobbies?", "your hobbies"]:
        print("I enjoy interacting with users and learning new things!")
    else:
        print("Sorry, I do not understand.")