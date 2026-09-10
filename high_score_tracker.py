#Start an intentional infinite loop using while True:.
while True:
#Inside the loop, ask the user to enter a game score next to the flashing cursor.
    score = input("Enter a game score: ").strip().lower()
    if score == "stop":
        print("Game session ended!")
        break
    else: 
        converted_score = int(score)
        if converted_score > 100:
            print("Wow! That’s a new high score!")
        else:
            print("Good try, keep playing!")