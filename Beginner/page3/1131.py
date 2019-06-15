inter_victories = 0
gremio_victories = 0
draw = 0

def processGrenals(inter, gremio, draw):
  [I, G] = list(map(int, input().split()))

  if I > G:
    inter += 1
  elif G > I:
    gremio += 1
  else:
    draw += 1
  
  return [inter, gremio, draw]


op = 1;
grenal = 0;

while (op != 2):
  if op == 1:
    grenal += 1
    [inter_victories, gremio_victories, draw] = processGrenals(inter_victories, gremio_victories, draw)
  
  print('Novo grenal (1-sim 2-nao)')
  op = int(input())

print(str(grenal) + ' grenais')
print('Inter:' + str(inter_victories))
print('Gremio:' + str(gremio_victories))
print('Empates:' + str(draw))

if inter_victories == gremio_victories:
  print('Não houve vencedor')
elif inter_victories > gremio_victories:
  print('Inter venceu mais')
else:
  print('Gremio venceu mais')