import  random

def game():
    print("you are playing the  game....")
    score = random.randint(1, 45)
    with open("hiscore.text") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score {score}")
    if(score>hiscore):
        with open("hiscore.text", "w") as f:
            f.write(str(score))

    return score

game()