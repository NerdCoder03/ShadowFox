#THE HANGMAN GAME
from colorslist import colors
import random
hangman_art={0:("-----",
                "  |  ",
                "     ",
                "     ",
                "     "),
             1:("-----",
                "  |  ",
                "  o  ",
                "     ",
                "     "),
             2:("-----",
                "  |  ",
                "  o  ",
                "  |  ",
                "     "),
             3:("-----",
                "  |  ",
                "  o  ",
                " /|  ",
                "     "),
             4:("-----",
                "  |  ",
                "  o  ",
                " /|\\",
                "     "),
             5:("-----",
                "  |  ",
                "  o  ",
                " /|\\",
                " /   "),
             6:("-----",
                "  |  ",
                "  o  ",
                " /|\\",
                " / \\")}
def hang(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print(line)
def give_hint(hint):
    print(" ".join(hint))
def reveal_answer(answer):
    print(" ".join(answer))
def main():
    print("Welcome to the Hangman Game!")
    print("Here's how it works:")
    print("- A secret color name has been chosen.")
    print("- You need to guess it letter by letter.")
    print("- Every wrong guess brings the poor man closer to doom.")
    print("- Guess carefully and save the man!")
    print("Good luck!")
    print("See this thing below ↓ The noose is ready for the man! Be careful!")
    answer=random.choice(colors)
    hint=["_"]*len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running=True
    while is_running:
        hang(wrong_guesses)
        give_hint(hint)
        guess=input("Enter a letter: ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Guess a single letter—nothing else!")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue
        guessed_letters.add(guess)
        if guess in answer:
            print("Great guess! Keep it up!")
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        else:
            wrong_guesses+=1
            print("Oops! Be careful—too many mistakes and the man is doomed!")
        if "_" not in hint:
            hang(wrong_guesses)
            print(f"The correct answer was: {answer}")
            print("CONGRATULATIONS! You have correctly guessed the word.\nThe man is saved!")
            is_running=False
        elif wrong_guesses>=len(hangman_art)-1:
            hang(wrong_guesses)
            print(f"The correct answer was: {answer}")
            print("Alas! You let a humble man die.")
            is_running= False

if __name__=="__main__":
    main()
