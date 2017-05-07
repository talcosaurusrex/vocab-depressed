#german vocab learner
#ver 0.1
#TODO
#randomise learn vocab
import pickle
import random


def save(vocabList):
    while True:
        german = input("\nEnter German Word  >")
        english = input("Enter English Word >")
        if (input("Are you sure? (enter/n)")).lower() == "n":
            continue
        vocabList += [[german, english]]
        if (input("Do you want to add more? (enter/n)")).lower() == "n":
            break
    name = input("What's the name of this module? >")
        
    out_file = open(name + ".dat","wb")
    pickle.dump(vocabList, out_file)
    out_file.close()
    print("Vocab Added!\n")

print("""For referance:
Ä	ALT+0196
ä	ALT+0228
Ö	ALT+0214
ö	ALT+0246
Ü	ALT+0220
ü	ALT+0252
""")
while True:
    print("""Welcome to vocab learner!
Would you like to:
1 - Learn Vocab
2 - Test Vocab
3 - Edit Loaded Vocab
4 - Add Vocab
5 - Edit a list
0 - Quit""")
    choice = input("\n>")

    #learn vocab
    if choice == "1":
        try:
            tempVocab = [i for i in vocab]
        except:
            print("No Vocab Loaded!\n")
        else:
            for i in vocab:
                print()
                while True:
                    print(i[0], "means", i[1])
                    print("What's", i[0], "in English?")
                    guess = input(">")
                    if guess == i[1]:
                        break
                    else:
                        print("Incorrect, have another go!")
            for i in vocab:
                print()
                while True:
                    print(i[1], "means", i[0])
                    print("What's", i[1], "in German?")
                    guess = input(">")
                    if guess == i[0]:
                        break
                    else:
                        print("Incorrect, have another go!")
            print("Well done you have learn you're vocab!")

    #test vocab
    elif choice == "2":
        try:
            tempVocab = [i for i in vocab]
        except:
            print("No Vocab Loaded!\n")
        else:
            done = []
            score = 0

            while True:
                try:
                    i = random.choice(tempVocab)
                except:
                    break
                print("What's", i[0], "in English?")
                guess = input(">")
                if guess == i[1]:
                        score += 1
                else:
                        print("Incorrect, it's", i[1])
                done.append(i)
                tempVocab.remove(i)
                
            while True:
                try:
                    i = random.choice(done)
                except:
                    break
                print("What's", i[1], "in German?")
                guess = input(">")
                if guess == i[0]:
                    score += 1
                else:
                    print("Incorrect, it's", i[0])
                done.remove(i)

            print("You got", score, "correct\n")

                
    #load vocab
    elif choice == "3":
        while True:
            choice = input("Which module would you like to load? >")
            try:
                in_file = open(choice + ".dat","rb")
                vocab = pickle.load(in_file)
                in_file.close()
            except FileNotFoundError:                
                print("Incorrect File Name")
            else:
                print("Vocab loaded!\n")
                break
                
                
        
    #add vocab
    elif choice == "4":
        vocabList = []
        save(vocabList)

    #edit a list
    elif choice == "5":
        try:
            tempVocab = [i for i in vocab]
        except:
            print("No Vocab Loaded!\n")
        else:
            for i in vocab:
                print(i)        
            option = input("Edit or add? (0,1,x)")
            if option == "0":
                while True:
                    choice = input("Which vocab do you want to edit? (x to stop)")
                    if choice.lower() == "x":
                        break
                    for index, i in enumerate(vocab):
                        for index2, i2 in enumerate(i):
                            if choice == i2:
                                edit = input("What would you like to change this to?")
                                vocab[index][index2] = edit
                                print(i2, "changed to", edit)
                                choice = input("Are you sure? (y/n)")
                                if choice.lower() == "y":
                                    choice = input("What's the name of this vocab set?")
                                    out_file = open(choice + ".dat","wb")
                                    pickle.dump(vocab, out_file)
                                    out_file.close()
                                    print("Vocab Changed!\n")
            elif option == "1":
                vocabList = [i for i in vocab]
                save(vocabList)
    #quit
    elif choice == "0":
        print("Goodbye")
        break
    #invalid choice
    else:
        print("Invalid Choice")
