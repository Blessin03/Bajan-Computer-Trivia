# This is a computer quiz with a focus on Barbados

print('Welcome to my computer quiz!')
# Ask the user if they want to play quiz
playing = input('Do you want to play ').lower()
# If the user does not want to play quit the quiz
if playing != 'yes':
 quit()

print("Okay! Let's play 😊")
score = 0 # Initialize the score to 0

# Ask the user a question and check if the answer is correct
answer = input ('What is the capital city of Barbados? ').lower()
if answer == 'bridgetown':
  print('Correct')
  score += 1
else:
  print('Incorrect, the correct answer is bridgetown.')
  
  # Ask the user a question and check if the answer is correct
answer = input ('In which year did Barbados gain independence from British rule? ').lower()
if answer == '1966':
  print('Correct')
  score += 1
else:
  print('Incorrect, the correct answer is 1966.')

# Ask the user a question and check if the answer is correct
answer = input ('Which popular Barbadian singer is known as the "Queen of Pop" and has hits like "Umbrella" and "Diamonds"? ').lower()
if answer == 'rihanna':
  print('Correct')
  score += 1
else:
  print('Incorrect, the correct answer is Rihanna.')
  
  # Ask the user a question and check if the answer is correct
  
answer = input ("Barbados is famous for its white sandy beaches, but can you name one of the most renowned beaches on the island that start's with b? ").lower()
if answer == "browne's beach" or answer ==  "brownes beach":
  print('Correct')
  score += 1
else:
  print("Incorrect, the correct answer is browne's beach")
  
  # Ask the user a question and check if the answer is correct

  
answer = input ("What is the local currency used in Barbados? ").lower()
if answer == "barbadian":
  print('Correct')
  score += 1
else:
  print("Incorrect, the correct answer is barbadian")
  
  # Ask the user a question and check if the answer is correct

  
answer = input ("The Barbados national dish ").lower()
if answer == "cou cou and flying fish":
  print('Correct')
  score += 1
else:
  print("Incorrect, the correct answer is Cou-Cou and Flying Fish ")
  
  # Ask the user a question and check if the answer is correct

  
  answer = input ("Barbados is home to a historic plantation house that is a UNESCO World Heritage Site. What is the name of this plantation house? ").lower()
if answer == "st. nicholas abbey" or  answer == "st.nicholas abbey":
  print('Correct')
  score += 1
else:
  print("Incorrect, the correct answer is St.Nicholas Abbey")

# Calculate and print percentage score
print(f'You got {str((score/7) * 100)} %')

# Print finished message
print("Finished.")

# Wait for user to press Enter to exit
input("Press Enter to exit.")

