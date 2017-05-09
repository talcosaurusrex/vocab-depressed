#german vocab learner
#ver 0.1
#TODO
#randomise learn vocab
import tkinter
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
    try:
        in_file = open(module_entry.get() + ".dat","rb")
        vocab = pickle.load(in_file)
        in_file.close()
    except FileNotFoundError:                
        invalid_lbl.configure(text="Incorrect Input")
        pass
    else:
        raise_frame(fChoiceLT)
    global vocab
    
def testedVocab():
        raise_frame(fTested)            
        tested1.configure(text="You got "+str(data[3])+" correct")
        #print("Theses are the words you got wrong:")
        #for i in incorrect:
        #    print(i[0], "-", i[1])
        #print()
def initTestVocab():
    raise_frame(fTest)
    position = 0
    #temp vocab, done, incorrect,score, current thing
    done = []
    incorrect = []
    score = 0
    data = [[i for i in vocab], [], [], 0, []]
    global data
    testVocab(position)
def testVocab(position):
    if position < len(vocab):
        print("yay1")
        i = random.choice(data[0])
        data[4] = i
        test1.configure(text="What's " + i[0] + " in English?")        
        data[1].append(i)
        data[0].remove(i)
    elif position >= len(vocab):
        print("yay2")
        i = random.choice(data[1])
        data[4] = i       
    positionG = position
    global positionG
def checkTestVocab(position):
    i = data[4]
    if position < len(vocab):
        if test2.get() == i[1]:
            test3.configure(text="Correct")
            data[3] += 1
        else:
            test3.configure(text="Incorrect, it's " + i[1])
            if i not in data[2]:
                data[2].append(i)
        test2.delete(0, "end")
        testVocab(position+1)
    elif position >= len(vocab):
        if test2.get() == i[0]:
            test3.configure(text="Correct")
            data[3] += 1
        else:
            test3.configure(text="Incorrect, it's " + i[0])
            if i not in data[2]:
                data[2].append(i)
        data[1].remove(i)
        test2.delete(0, "end")
        if position+1 == 2*len(vocab):
            testedVocab()
        else:
            testVocab(position+1)
        
#init vocab learning        
def initLearnVocab():
    raise_frame(fLearn)
    position = 0
    learnVocab(position)  
def learnVocab(position):    
    if position < len(vocab):
        i = vocab[position]
        learn1.configure(text=i[0] + " means " + i[1])
        learn2.configure(text="What's " + i[0] + " in English?")
    elif position >= len(vocab):
        i = vocab[len(vocab) - position]
        learn1.configure(text=i[1] + " means " + i[0])
        learn2.configure(text="What's " + i[1] + " in German?")
    positionG = position
    global positionG
def checkLearnVocab(position):
    if position < len(vocab):
        i = vocab[position]
        if learn3.get() == i[1]:
            learn3.delete(0, "end")
            learnVocab(position+1)
        else:
            learn4.configure(text="Incorrect, try again")
            learnVocab(position+1)
    elif 2*len(vocab) > position >= len(vocab):
        i = vocab[len(vocab) - position]
        if learn3.get() == i[0]:
            learn3.delete(0, "end")
            learnVocab(position+1)
        else:
            learn4.configure(text="Incorrect, try again")
            learnVocab(position+1)    
    else:
        raise_frame(fLearnt)
        


def raise_frame(frame):
    frame.tkraise()

window = tkinter.Tk()
fHome =tkinter.Frame(window)
fLoad =tkinter.Frame(window)
fChoiceLT =tkinter.Frame(window)
fLearn =tkinter.Frame(window)
fLearnt =tkinter.Frame(window)
fTest =tkinter.Frame(window)
fTested =tkinter.Frame(window)
fChoice =tkinter.Frame(window)
fNew =tkinter.Frame(window)
fEdit =tkinter.Frame(window)
fAdd =tkinter.Frame(window)

for frame in (fHome, fLoad, fChoiceLT, fLearn, fLearnt, fTest, fTested, fChoice, fNew, fEdit, fAdd):
    frame.grid(row=0, column=0, sticky='news')
    
#window.geometry("500x500")
window.wm_iconbitmap("favicon.ico")
window.title("Vocab Depressed")
#home
tkinter.Label(fHome, text ="""Welcome to Vocab Learner!
Would you like to:""").pack()
tkinter.Button(fHome, text="Load Vocab", command=lambda:raise_frame(fLoad)).pack(pady=10)
tkinter.Button(fHome, text="Add/Edit Vocab", command=lambda:raise_frame(fChoice)).pack(pady=10)
#load
tkinter.Label(fLoad, text="What vocab do you want to load?").pack()
module_entry = tkinter.Entry(fLoad)
module_entry.pack(pady=10)
tkinter.Button(fLoad, text="Load", command=loadVocab).pack(pady=10)
invalid_lbl = tkinter.Label(fLoad, text="")
invalid_lbl.pack(pady=10)
tkinter.Button(fLoad, text="Back", command=lambda:raise_frame(fHome)).pack(pady=10)
#choice l/t
tkinter.Label(fChoiceLT, text="Do you want to:").pack()
tkinter.Button(fChoiceLT, text="Learn Vocab", command=initLearnVocab).pack(pady=10)
tkinter.Button(fChoiceLT, text="Test Vocab", command=initTestVocab).pack(pady=10)
tkinter.Button(fChoiceLT, text="Back", command=lambda:raise_frame(fHome)).pack(pady=10)
#learn
learn1 = tkinter.Label(fLearn, text="")
learn2 = tkinter.Label(fLearn, text="")
learn3 = tkinter.Entry(fLearn)
learn4 = tkinter.Label(fLearn, text="")
learn5 = tkinter.Button(fLearn, text="Check", command=lambda:checkLearnVocab(positionG))
learn6 = tkinter.Label(fLearn, text="""For referance:
Ä	ALT+0196
ä	ALT+0228
Ö	ALT+0214
ö	ALT+0246
Ü	ALT+0220
ü	ALT+0252""")
learn1.pack()
learn2.pack(pady=10)
learn3.pack(pady=10)
learn4.pack(pady=10)
learn5.pack(pady=10)
learn6.pack(pady=10)
#learnt
tkinter.Label(fLearnt, text="""Congratulations!!
You have learnt your vocab!""").pack()
tkinter.Button(fLearnt, text="Done", command=lambda:raise_frame(fChoiceLT)).pack(pady=10)
#test
test1 = tkinter.Label(fTest, text="")
test2 = tkinter.Entry(fTest)
test3 = tkinter.Label(fTest, text="")
test4 = tkinter.Button(fTest, text="Check", command=lambda:checkTestVocab(positionG))
test5 = tkinter.Label(fTest, text="""For referance:
Ä	ALT+0196
ä	ALT+0228
Ö	ALT+0214
ö	ALT+0246
Ü	ALT+0220
ü	ALT+0252""")
test1.pack()
test2.pack(pady=10)
test3.pack(pady=10)
test4.pack(pady=10)
test5.pack(pady=10)
#tested
tested1 = tkinter.Label(fTested, text="")
tested1.pack()
tkinter.Button(fTested, text="Done", command=lambda:raise_frame(fChoiceLT)).pack(pady=10)
#choice
tkinter.Label(fChoice, text="Do you want to:").pack()
tkinter.Button(fChoice, text="Create New Vocab List", command=lambda:raise_frame(fNew)).pack(pady=10)
tkinter.Button(fChoice, text="Edit Existing Vocab List", command=lambda:raise_frame(fEdit)).pack(pady=10)
tkinter.Button(fChoice, text="Add Words to Existing Vocab List", command=lambda:raise_frame(fNew)).pack(pady=10, padx=10)
tkinter.Button(fChoice, text="Back", command=lambda:raise_frame(fHome)).pack(pady=10)
#new
#edit
#add

#run
raise_frame(fHome)
window.mainloop()
print()
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
                learnVocab(vocab)
            #test
            elif choice == "2":
                testVocab(vocab)
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
