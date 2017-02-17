### T.J. Koepp Python Final Project - Fill in the Blank Quiz ###

### Define Variables for Quiz ###

import sys

answers = ["___1___", "___2___", "___3___", "___4___"]  ### variable for blanks within selected paragraphs ###

easy_quiz = '''___1___ is a clear and powerful object-oriented ___2___ language, comparable to Perl, Ruby, Scheme, or Java. Some of Python's notable features include use of elegant ___3___, making the programs you write easier to read. Python's interactive mode also makes it easy to test short snippets of ___4___.'''  ### Quiz paragraph used if user selects easy as their option. ###
medium_quiz = '''Some programming-language features of Python are, a variety of basic ___1___ types including numbers, strings, lists, and dictionaries. Python supports object-oriented programming with ___2___ and multiple inheritance. The code can be grouped into ___3___ and packages. Additionaly, data types are strongly and dynamically typed. Mixing incompatible types (e.g. attempting to add a string and a number) causes an ___4___ to be raised, so errors are caught sooner.''' ### Quiz paragraph used if user selects medium as their option. ###
hard_quiz = '''Python uses ___1___ typing and a mix of reference counting and a cycle-detecting garbage collector for ___2___ management. An important feature of Python is dynamic ___3___ resolution (late binding), which binds method and ___4___ names during program execution.'''  ### Quiz paragraph used if user selects hard as their option. ###

easy_answers = ["python", "programming", "syntax", "code"] ### Answers for the blanks within the easy paragraph. ###
medium_answers = ["data", "classes", "modules", "exception"] ### Answers for the blanks within the medium paragraph. ###
hard_answers = ["dynamic", "memory", "name", "variable"]    ### Answers for the blanks within the hard paragraph. ###

def choose_difficulty():
    ### This loop will run over and over until the function returns a proper selection. ###
    ### Inputs = User's selected level from their input choice. ###
    ### Outputs = Selected difficulty level paragraphy and answers. ###

    while True:
        choice = raw_input("Please enter a level 'easy', 'medium', 'hard': ")
        choice = choice.lower()
        if choice == "easy":
            print "\nThank you for choosing the easy level. Let's play the game!\n"
            return choice, easy_quiz, easy_answers
        elif choice == "medium":
            print "\nThank you for choosing the medium level. Let's play the game!\n"
            return choice, medium_quiz, medium_answers
        elif choice == "hard":
            print "\nThank you for choosing the easy level. Let's play the game!\n"
            return choice, hard_quiz, hard_answers
        elif choice != "easy" or choice != "medium" or choice != "hard":
            print "\nPlease select a difficulty level based on the three choices given.\n"
        # If choice does not equal easy, medium, or hard, the function will loop around and start at the top

chosen_difficulty, chosen_quiz, chosen_answers = choose_difficulty()

def number_of_turns():
  ### This function prompts the player to select how many turns they would like to guess the correct answer. ###  
  ### Inputs = User input of a positive integer to select number of turns they get. ###
  ### Outputs = Number of turns the player will get when choosing an incorrect answer before they lose the game. ###

  player_prompt = "How many turns would you like?"
  
  player_turns = int(raw_input(player_prompt))
  while player_turns <= 0:
      print "Sorry! Please pick a positive number for your turns!"
      player_turns = int(raw_input(player_prompt))
      
  return player_turns

player_turns = number_of_turns()

def get_answer(answer, my_text, index, my_difficulty, my_answers):
    ### This function takes the user's guess as input and matches it against the correct answer. If the answer is incorrect it notify's the user to try again. If the answer is correct it moves on to the next question. ###
    ### Inputs = Number of chances the user wants for each question, and the guess they make for each question. ###
    ### Outputs = Notification if answer is incorrect. ###

    chances = 0
    guess = ""
    while guess != answer:
        print ""
        print my_text
        blank = answers[index]
        guess = raw_input("\nPlease enter a guess for " + blank + ":")

        if guess.lower() == answer:
            return True
        else: 
            print "\nI'm sorry, that is incorrect! Please try again.\n"
            chances +=1
            if chances >= player_turns:
                return play_again(chances, player_turns, my_difficulty, my_text, my_answers)
   

def play_again(chances, player_turns, my_difficulty, my_text, my_answers):
    ### The function asks the user if they would like to play the game again if they lose and allows them to pass "yes" or "no" as input to play again. If they select yes the game will restart, if they select no the game will end. ###
    ### Inputs = User input to play the game again or not. ###
    ### Outputs = Restarted game if user selects yes. Terminates game if user selects no. ###

    while True:
        play_again_input = ""
        play_again_input = raw_input("Game Over! Would you like to play again? 'yes' or 'no':")
        play_again_input = play_again_input.lower()
        print ""
        if play_again_input == "yes":
            play_game(my_difficulty, my_text, my_answers, player_turns)
        elif play_again_input == "no":
            sys.exit() 
        elif play_again_input != "yes" or play_again != "no":
            print "Please try again:"
                      

def play_game(my_difficulty, my_text, my_answers, player_turns):
    ### This fucntion actually starts the game for the user. ###
    ### Inputs = Selected difficulty, text, answers, and number of turns the user selected in the choose_difficulty() function and number_of_turns() function. ###
    ### Outputs = Notification that the answer is correct if the user types in the correct answer and it also informs the user that they have won the game. ###
    
    for index in range(len(answers)):
        answer = my_answers[index]
        if get_answer(answer, my_text, index, my_difficulty, my_answers) == True:
            my_text = my_text.replace(answers[index], answer.upper())
            print "\nThat is correct!\n"
        
   
    print my_text
    print "\nCongratulations! You have won the game!\n"

play_game(chosen_difficulty, chosen_quiz, chosen_answers, player_turns)
