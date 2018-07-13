# --- Define your functions below! ---
def intro():
    print("Hello")

def processInput(answer):
    if answer == "hi":
        saygreeting()
    else:
        saydefault()

def saygreeting():
        print("How are you?")
def saydefault():
        print("That's cool")


# --- Put your main program below! ---

def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        processInput(answer)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
