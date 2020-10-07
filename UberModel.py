import random
BidenWins = 0
TrumpWins = 0

for lp in range(100):
  TrumpEV = 163
  BidenEV = 183
  ARIZONA = random.randint(-3, 2)
  COLORADO = random.randint(-5, 1)
  FLORIDA = random.randint(-2, 3)
  GEORGIA = random.randint(-1, 6)
  IOWA = random.randint(-1, 12)
  MAINE = random.randint(-5, 1)
  MAINE2 = random.randint(-1, 3)
  MICHIGAN = random.randint(-3, 1)
  MINNESOTA = random.randint(-5, 1)
  NEBRASKA2 = random.randint(-1, 2)
  NEVADA = random.randint(-4, 2)
  NEW_HAMPSHIRE = random.randint(-3, 1)
  NEW_MEXICO = random.randint(-6, 1)
  NORTH_CAROLINA = random.randint(-2, 3)
  OHIO = random.randint(-3, 12)
  PENNSYLVANIA = random.randint(-2, 2) 
  VIRGINIA = random.randint(-8, 1)
  WISCONSIN = random.randint(-1, 1)

  if (ARIZONA > 0):
    print("Trump Won Arizona!")
    TrumpEV = TrumpEV + 11
  else:
    print("Biden won Arizona!")
    BidenEV = BidenEV + 11
  #if (ARIZONA == 0):
  # print("Arizona is a tossup")


  if (COLORADO > 0):
    print("Trump Won Colorado!")
    TrumpEV = TrumpEV + 9
  else:
    print("Biden won Colorado!")
    BidenEV = BidenEV + 9


  if (FLORIDA > 0):
    print("Trump Won Florida!")
    TrumpEV = TrumpEV + 29
  else:
    print("Biden won Florida!")
    BidenEV = BidenEV + 29


  if (GEORGIA > 0):
    print("Trump Won Georgia")
    TrumpEV = TrumpEV + 16
  else:
    print("Biden won Georgia!")
    BidenEV = BidenEV + 16


  if (IOWA > 0):
    print("Trump Won Iowa!")
    TrumpEV = TrumpEV + 6
  else:
    print("Biden won Iowa!")
    BidenEV = BidenEV + 6


  if (MAINE > 0):
    print("Trump Won Maine!")
    TrumpEV = TrumpEV + 2
  else:
    print("Biden won Maine!")
    BidenEV = BidenEV + 2


  if (MAINE2 > 0):
    print("Trump Won Maine's 2nd District!")
    TrumpEV = TrumpEV + 1
  else:
    print("Biden won Maine's 2nd District!")
    BidenEV = BidenEV + 1


  if (MICHIGAN > 0):
    print("Trump Won Michigan!")
    TrumpEV = TrumpEV + 16
  else:
    print("Biden won Michigan!")
    BidenEV = BidenEV + 16


  if (MINNESOTA > 0):
    print("Trump Won Minnesota!")
    TrumpEV = TrumpEV + 10
  else:
    print("Biden won Minnesota!")
    BidenEV = BidenEV + 10


  if (NEBRASKA2 > 0):
    print("Trump Won Nebraska's 2nd District!")
    TrumpEV = TrumpEV + 1
  else:
    print("Biden won Nebraska's 2nd District!")
    BidenEV = BidenEV + 1


  if (NEVADA > 0):
    print("Trump Won Nevada!")
    TrumpEV = TrumpEV + 6
  else:
    print("Biden won Nevada!")
    BidenEV = BidenEV + 6


  if (NEW_HAMPSHIRE > 0):
    print("Trump Won New Hampshire!")
    TrumpEV = TrumpEV + 4
  else:
    print("Biden won New Hampshire!")
    BidenEV = BidenEV + 4


  if (NEW_MEXICO > 0):
    print("Trump Won New Mexico!")
    TrumpEV = TrumpEV + 5
  else:
    print("Biden won New Mexico!")
    BidenEV = BidenEV + 5


  if (NORTH_CAROLINA > 0):
    print("Trump Won North Carolina!")
    TrumpEV = TrumpEV + 15
  else:
    print("Biden won North Carolina!")
    BidenEV = BidenEV + 15


  if (OHIO > 0):
    print("Trump Won Ohio!")
    TrumpEV = TrumpEV + 18 
  else:
    print("Biden won Ohio!")
    BidenEV = BidenEV + 18


  if (PENNSYLVANIA > 0):
    print("Trump Won Pennsylvania!")
    TrumpEV = TrumpEV + 20
  else:
    print("Biden won Pennsylvania!")
    BidenEV = BidenEV + 20


  if (VIRGINIA > 0):
    print("Trump Won Virginia!")
    TrumpEV = TrumpEV + 13
  else:
    print("Biden won Virginia!")
    BidenEV = BidenEV + 13


  if (WISCONSIN > 0):
    print("Trump Won Wisconsin!")
    TrumpEV = TrumpEV + 10 
  else:
    print("Biden won Wisconsin!")
    BidenEV = BidenEV + 10

  if TrumpEV >= 270:
    print("Trump won the election!")
    print ("Trump: " + str(TrumpEV) + " Biden: " + str(BidenEV))
    TrumpWins = TrumpWins + 1

  if BidenEV >= 270:
    print("Biden won the election!")
    print ("Biden: " + str(BidenEV) + " Trump: " + str(TrumpEV))
    BidenWins = BidenWins + 1

print ("")
print("")
print("")
print("")
print ("Trump wins " + str(TrumpWins) + "% of the time.")
print ("Biden wins " + str(BidenWins) + "% of the time.")
