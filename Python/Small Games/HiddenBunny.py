# Hidden Bunny Game
print("Choose the Hat by the numbers:\n1 2 3")
from random import randint

HAT = "🎩"
BUNNY = "🐇"
BUNNY_FACE = "🐰"

BIG_SWAP = "🔄"
SWAP = "↔️"

middle = 1
hats = [HAT] * 3
hiddenBunny = randint(0,2)

def printHats():
  print(" ".join(hats))

def isNear(n1, n2):
  return n1+1 == n2 or n1-1 == n2

print("Find the hidden bunny!")

printHats()
print(("   "*hiddenBunny)+BUNNY)
hats[hiddenBunny] = BUNNY_FACE
print()
printHats()
hats[hiddenBunny] = HAT

swaps = randint(3, 10)

for i in range(swaps):
  swap = randint(0, 2)
  while swap == hiddenBunny:
    swap = randint(0, 2)
  if isNear(swap, hiddenBunny):
    fmt = ""
    s = -1
    if swap+1==hiddenBunny:
      s = swap
    else:
      s = hiddenBunny
    for hat in range(len(hats)):
      fmt += hats[hat]
      if hat != len(hats)-1:
        if hat==s:
          fmt += SWAP
        else:
          fmt += " "
    print(fmt)
  else:
    hats[middle] = BIG_SWAP
    printHats()
    hats[middle] = HAT
  hiddenBunny = swap


where = int(input("Where is the bunny?"))-1
if where==hiddenBunny:
  print("Yay! ur right, found the bunny👍")
else:
  print("Nah! dat bunny wasn't there🫤")

hats[hiddenBunny]=BUNNY
printHats()
