import random

name = input("What's your name? ")

# Conversation robot.

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

  user_input = input(f"Hello, how are you {name}?\n ")

  while user_input != quit_character:
    #Ask the user for more input to generate the response.
    user_input = input(response_generation(user_input) + "\n")

if __name__ == "__main__":
  init_chat()

#New Change

# This is a basic workflow to help you get started with Actions

name: CI

# Controls when the action will run. 
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2

      - name: Install Python 3
        uses: actions/setup-python@v1
        with:
          python-version: 3.6

      - name: Run tests
        run: python test.py
