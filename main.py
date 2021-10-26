import random

#Name
name = input("What's your name? ")

# Conversation robot.
def greeting(user_response):
  results = [
    "Great!",
    "Wonderful",
    "YEET!!!"
  ]
  return random.choice(results)

def response_generation(user_input):
  responses = [
    "Wow, very interesting!",
    "You don't say!",
    "Very nice!",
    "Programming is life!",
    "The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.",
    "GENERAL KANOBY!!!!!",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www.youtube.com/watch?v=EaqJgQOVZ9k"
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'

  user_response = input(f"Hello, how are you {name}?\n ")
  
  user_input = input("What do you want to talk about?")
  
  while user_input != quit_character:
    #Ask the user for more input to generate the response.
    user_input = input(response_generation(user_input) + "\n")

if __name__ == "__main__":
  init_chat()

