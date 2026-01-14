import random

def play_game():
    print("=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("=" * 40)
    print("\nI'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!\n")
                continue
            
            if guess < secret_number:
                print("Too low! Try a higher number.\n")
            elif guess > secret_number:
                print("Too high! Try a lower number.\n")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {secret_number}!\n")
                return True
                
        except ValueError:
            print("Invalid input! Please enter a number.\n")
    
    print(f"\n😔 Game Over! You've used all {max_attempts} attempts.")
    print(f"The number was {secret_number}.\n")
    return False

def main():
    while True:
        play_game()
        
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye! 👋")
            break
        print("\n")

if __name__ == "__main__":
    main()