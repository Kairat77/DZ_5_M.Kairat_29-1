from decouple import config
import random

def kazino():
  while True:
    money = config("MY_MONEY", cast=int)

    stafka = int(input("сделайте ставку:"))
    chislo = int(input("выберите число от 1 до 30:"))

    vigrish = random.randint(1, 31)
    if vigrish == chislo:
        money += (stafka * 2)
        print(f"вы выиграли = {stafka * 2}$")
    else:
        money -= stafka
        print(f"вы проиграли = {stafka}$")
    print(f"на вашем балансе остались {money}")

    play_again = input("хотите сыграть еще? ")
    if play_again == "да":
      continue
    else:
      break