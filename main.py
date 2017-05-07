#german vocab learner
#ver 0.1
#TODO
#randomise learn vocab
import pickle
import random


def saveVocab(vocabList):
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
def loadVocab():
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
    return vocab
def testVocab(vocab):
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
def learnVocab(vocab):
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
        print("Well done you have learned you're vocab!")

print("""For referance:
Ä	ALT+0196
ä	ALT+0228
Ö	ALT+0214
ö	ALT+0246
Ü	ALT+0220
ü	ALT+0252
""")
while True:
    print("""Welcome to Vocab Learner!
No Vocab Loaded!
Would you like to:
1 - Load Vocab
2 - Add/Edit Vocab
0 - Quit
""")

    choice = input("\n>")

    #load vocab
    if choice == "1":
        vocab = loadVocab()
        while True:
            print("""Do you want to:
1 - Learn Vocab
2 - Test Vocab
0 - Go Back
""")
            choice = input(">")
            #learn
            if choice == "1":
                testVocab(vocab)
            #test
            elif choice == "2":
                learnVocab(vocab)
            #go back
            elif choice == "0":
                break
    #add/edit Vocab
    elif choice == "2":
        print("Do you want to create new vocab or edit existing vocab? (0,1)")
        choice = input(">")
        #new vocab
        if choice == "0":
            vocabList = []
            saveVocab(vocabList)
        #edit vocab
        if choice == "2":
            vocab = loadVocab()
            try:
                tempVocab = [i for i in vocab]
            except:
                print("No Vocab Loaded!\n")
            else:
                for i in vocab:
                    print(i)        
                option = input("Edit or add? (0,1,x)")
                #edit vocab
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
                                    #save
                                    if choice.lower() == "y":
                                        choice = input("What's the name of this vocab set?")
                                        out_file = open(choice + ".dat","wb")
                                        pickle.dump(vocab, out_file)
                                        out_file.close()
                                        print("Vocab Changed!\n")
                #add vocab
                elif option == "1":
                    vocabList = [i for i in vocab]
                    saveVocab(vocabList)
    #quit
    elif choice == "0":
        print("Goodbye")
        break
    #invalid choice
    else:
        print("Invalid Choice")
