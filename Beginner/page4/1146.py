while True:
  X = int(input())
  
  if X == 0:
    break
  
  s_out = []
  for i in range(1, X+1):
    s_out.append(str(i))
  
  print(str.join(' ', s_out))