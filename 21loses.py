from random import randint
first= 0
second = 0
turn = randint(1,2)
playing = True
while (playing == True):
  if turn == 1:
    print("first player turn")
    first += randint(1,2)
    print (first)
  else:
          print("second player turn")
    second += randint(1,2)
    print(second)
  if a >= 21:
    print("first player lost!")
    break;
  elif b >= 21:
    print("\nsecond player lost!")
    break;
