while True:

    baselineinput = input("How large shall the pyramids base be, my lord? ")
    print("Very well, " + baselineinput + " it shall be:")

    baseline = int(baselineinput)

    print("")

    for x in range(1, baseline, 2):
       print(" "*((baseline-x)//2), end = "")
       print("*"*x, end = "")
       print(" "*((baseline-x)//2))

    print("")

    happy = input("Art thou happy with thine pyramid, sire?")
    print(happy)

    if happy == "Very much so":
       print("Very well, I shall retire to my chambers then.")
       break
    else:
      print("Very well, we shall rebuild it then.")
      print("")
      continue