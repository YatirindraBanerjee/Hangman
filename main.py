import random
from words import words


def generateSecretWord():
    word = random.choice(words)
    while '-' in word or ' ' in word or len(word) > 7:
        word = random.choice(words)
    return word


def splitWordInLetters(word):
    word_list = []
    for letter in word:
        word_list.append(letter)
    return word_list


def setEmptyList(list, size):
    for i in range(size):
        list.append('-')
    return list


def main():
    secret_word = generateSecretWord().upper()
    secret_word_letter = splitWordInLetters(secret_word)
    user_chosen_letter = []
    user_chosen_letter = setEmptyList(
        user_chosen_letter, len(secret_word_letter))
    chances_to_guess = 7
    user_guessed = 0
    not_game_over = False
    while user_guessed < chances_to_guess and not not_game_over:
        index = 0
        print()
        for i in range(len(user_chosen_letter)):
            print(user_chosen_letter[i], end=" ")
        print("\n")
        user_input = input("Enter your Guess: ").upper()
        if len(user_input) > 1 or len(user_input) == 0:
            print("It's not a valid guess")
        else:
            if user_input in secret_word_letter:
                while index < len(user_chosen_letter):
                    if secret_word_letter[index] == user_input:
                        user_chosen_letter[index] = user_input
                    index += 1
                if user_chosen_letter == secret_word_letter:
                    not_game_over = True
            else:
                user_guessed += 1
                print(
                    f"The letter is not in the word. You have {chances_to_guess-user_guessed} times.")
    if not_game_over == True:
        print("You have won the game")
    else:
        print(f"You have lose the game, and the word was {secret_word}.")


if __name__ == '__main__':
    main()
