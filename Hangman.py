# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:51:25 2020

@author: William
"""

import random

words = {"Planets": "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune".split(),
         "Animals": "Dog Cat Owl Crow Parrot Bear Fox Shark Whale Dolphin Fish Panda Rat Badger Llama".split(),
         "Capitals": "Washington London Berlin Tokyo Paris Rome Moscow Beijing Seoul Canberra Jakarta Ottawa Brasilia".split(),
         "Elements": "Hydrogen Helium Carbon Oxygen Nitrogen Silicon Magnesium Calcium Chlorine Iodine Uranium".split(),
         "Scientists": "Newton Einstein Darwin Hawking Maxwell Franklin Crick Curie Mendeleev Feynman".split()}

hangMan = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
. =========''', '''


   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''


   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |

=========''']

def getRandomWord(wordDict):
    # gets random word from word list
    wordKey = random.choice(list(wordDict.keys()))
    
    wordIndex = random.randint(0, len(wordDict[wordKey])-1)
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(hangMan, wrongLetters, secretWord, correctLetters):
    print(hangMan[len(wrongLetters) -1])
    print()
    
    print('Wrong Letters:' , end = " ")
    for l in wrongLetters:
        print(l, end = " ")
    print()
    
    blanks = '_' * len(secretWord)
    
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    for l in blanks:
        print(l, end = " ")
    print()

print("Welcome to Hangman!")
wrongLetters = ""
correctLetters = ""
secretWord, secretSet = getRandomWord(words)
gameOver = False

while True:
    displayBoard(hangMan, wrongLetters, secretWord, correctLetters)
    print('Please guess a letter: ')
    guess = input()
    #guess = guess.lower()
    if guess not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print('This is not a letter! Please make a valid guess: ')
    elif len(guess) != 1:
        print('Please enter a single letter: ')
    elif guess in correctLetters or guess in wrongLetters:
        print('You have already guessed this letter! Please pick another: ')

    if guess in secretWord:
        correctLetters = correctLetters + guess
    
    #Victory conditions
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Congrats dude! The secret word is ' + secretWord + '! You have won!')
            gameOver = True
            break
    else:
        wrongLetters = wrongLetters + guess
    
    #Losing conditions
        if len(wrongLetters) == len(hangMan) - 1:
            displayBoard(hangMan, wrongLetters, secretWord, correctLetters)
            print('HANGMAN!!!!! You have run out of guesses! The secret word is ' + secretWord + '! You have lost!')
            gameOver = True
            break
    

    
    