from random import randint
a = 0
b = 0
turn = randint(1,2)
playing = True
while (playing == True):
  if turn == 1:
    a += randint(1,2)
    print (a)
  else:
    b += randint(1,2)
    print(b)
  if a >= 21:
    print("first player lost!")
    break;
  elif b >= 21:
    print("\n\nsecond player lost!")
    break;
