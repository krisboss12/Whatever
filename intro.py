print("""This is Madlibs you'll need to input different nouns and verbs, think of words as random as possible""")


pluaral_noun = raw_input("Please input a plural noun:")
noun1 = raw_input("Please input a noun")
noun2 = raw_input("Please input a noun")
song = raw_input("Please input the name of a song")
verb = raw_input("Please input a verb")
madlibs = ("""Learning to drive is a tricky process. There are a few rules you need to follow
1. Keep two %s on the steering wheel at all times.
2. Step on the %s to speed up and the %s to slow down
3. Your parents would just LOVE it if you play %s on the radio
4. Make sure to honk the hork when you see %s on the street sign.""")

print(madlibs %(pluaral_noun,noun1,noun2,song,verb))