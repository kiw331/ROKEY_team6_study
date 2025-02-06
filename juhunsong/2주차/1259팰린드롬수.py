while True:
  a=str(input())
  if a=="0":
    break

  l=len(a)
  x=0
  if len(a)==1:
    print('yes')
    continue
  for i in range(l):
    if a[i] != a[-(i+1)]:
      print('no')
      break
    else:
      x+=2
      if x==l or (x+1)==l:
        print('yes')
        break
