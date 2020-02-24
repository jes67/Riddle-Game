import random
import json

secret = random.randint(1,30)

guess = 0
attempts = 0

with open("score.txt", "r") as f:
    score_list = json.loads(f.read())
    print("Puntuaciones: " + str(score_list))


while True:
    guess = int(input("Encuentra el numero secreto (entre el 1 y 30): "))
    attempts += 1

    if guess == secret:
        print("Felicidades, has acertado")
        print("Intentos necesitados:  " + str(attempts))
        score_list.append(intentos)
        with open("score.txt", "w") as f:
            f.write(json.dumps(score_list)
            score_list.sort()
            for s in score_list:
                print(s)
        break
    elif guess > secret:
        print("No es correcto... intentalo con uno menor")
    elif guess < secret:
        print("No es correcto, intentandolo con uno mayor")













