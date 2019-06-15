def readNotes():
  score1 = -1
  score2 = -1
  
  while (score1 < 0 or score2 < 0):
    s = float(input())

    if s >= 0 and s <= 10:
        if score1 < 0:
            score1 = s
        else:
            score2 = s
    else:
        print('nota invalida')
  
  media = (score1 + score2) / 2
  print('media = ' + '%.2f'%media)

op = 1
while (op != 2):
  if op == 1:
    readNotes()
  
  print('novo calculo (1-sim 2-nao)')
  op = int(input())
