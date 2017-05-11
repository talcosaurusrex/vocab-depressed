#german vocab learner
#ver 0.270
#TODO
#randomise learn vocab?
#add edit list
import tkinter
import pickle
import random


def saveVocab(event=None):
    vocabList = newVocabList
    name = save1.get()     
    out_file = open(name + ".dat","wb")
    pickle.dump(vocabList, out_file)
    out_file.close()
    raise_frame(fChoice)
    #clear entry
    save1.delete(0, "end")
def loadVocab(event=None):    
    try:
        in_file = open(module_entry.get() + ".dat","rb")
        vocab = pickle.load(in_file)
        in_file.close()
    except FileNotFoundError:                
        invalid_lbl.configure(text="Incorrect Input")
    else:
        global vocab
        raise_frame(fChoiceLT)
        #clear entry
        module_entry.delete(0, "end")
        invalid_lbl.configure(text="")
def loadVocab2(event=None):    
    try:
        in_file = open(printI1.get() + ".dat","rb")
        vocab = pickle.load(in_file)
        in_file.close()
    except FileNotFoundError:                
        printI2.configure(text="Incorrect Input")
    else:
        global vocab
        printVocab()
        #clear entry
        printI1.delete(0, "end")
        printI2.configure(text="")
def testedVocab():
    fTested =tkinter.Frame(window)
    fTested.grid(row=0, column=0, sticky='news')
    tested1 = tkinter.Label(fTested, text="")
    tested1.pack()
    raise_frame(fTested)            
    tested1.configure(text="You got "+str(data[3])+" correct")
    tkinter.Label(fTested, text="Theses are the words you got wrong:").pack(pady=pad_y)
    for i in data[2]:
        tkinter.Label(fTested, text=i[0]+" - "+i[1]).pack()
    tkinter.Button(fTested, text="Done", command=lambda:stopTested(fTested)).pack(pady=pad_y)
def stopTested(fTested):
    fTested.destroy()
    raise_frame(fChoiceLT)
def initTestVocab():
    raise_frame(fTest)
    position = 0
    #temp vocab, done, incorrect,score, current thing
    data = [[i for i in vocab], [], [], 0, []]
    global data
    testVocab(position)
def testVocab(position):
    if position < len(vocab):
        i = random.choice(data[0])
        data[4] = i
        test1.configure(text="What's " + i[0] + " in English?")        
        data[1].append(i)
        data[0].remove(i)
    elif position >= len(vocab):
        i = random.choice(data[1])
        test1.configure(text="What's " + i[1] + " in German?")
        data[4] = i       
    positionG = position
    global positionG
def checkTestVocab(event=None):
    position = positionG
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
            #clear entry
            test2.delete(0, "end")
            test3.configure(text="")
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
        learn1.configure(text=i[0] + " means <Hiddden>")
        learn2.configure(text="What's " + i[0] + " in English?")
        phrase = i[0] + " means " + i[1]
    elif position >= len(vocab):
        i = vocab[len(vocab) - position]
        learn1.configure(text=i[1] + " means <Hiddden>")
        learn2.configure(text="What's " + i[1] + " in German?")
        phrase = i[1] + " means " + i[0]
    positionG = position
    global positionG
    global phrase
def showVocab():
    learn1.configure(text=phrase)
def checkLearnVocab(event=None):
    position = positionG
    if position < len(vocab):
        i = vocab[position]
        if learn3.get() == i[1]:
            learn3.delete(0, "end")
            learn4.configure(text="")
            learnVocab(position+1)
        else:
            learn4.configure(text="Incorrect, try again")
            learnVocab(position)
    elif 2*len(vocab) > position >= len(vocab):
        i = vocab[len(vocab) - position]
        if learn3.get() == i[0]:
            learn3.delete(0, "end")
            learn4.configure(text="")
            learnVocab(position+1)
        else:
            learn4.configure(text="Incorrect, try again")
            learnVocab(position)    
    else:
        #clear entry
        learn3.delete(0, "end")
        learn4.configure(text="")
        raise_frame(fLearnt)
def initNewVocab():
    raise_frame(fNew)
    newVocabList = []
    global newVocabList
def newVocab(event=None):
    german = new2.get()
    english = new4.get()
    newVocabList.append([german, english])
    #clear entry
    new2.delete(0, "end")
    new4.delete(0, "end")
    print([german, english])
def addVocab(event=None):
    german = add1.get()
    english = add2.get()    
    try:
        in_file = open(add3.get() + ".dat","rb")
        newVocabList = pickle.load(in_file)
        in_file.close()
    except FileNotFoundError:                
        add4.configure(text="File Not There")
    else:
        #clear entry
        add3.delete(0, "end")
        add4.configure(text="")
        combined = [german, english]
        newVocabList.append(combined)
        global newVocabList
        raise_frame(fSave)
def editVocab(event=None):
    try:
        in_file = open(edit1.get() + ".dat","rb")
        newVocabList = pickle.load(in_file)
        in_file.close()
    except FileNotFoundError:                
        edit2.configure(text="File Not There")
    else:
        #clear entry, done in add edit vocab
        edit2.configure(text="")
        global newVocabList
        raise_frame(fChange)
        initEditVocab()
def initEditVocab():
    fVocab =tkinter.Frame(window)
    fVocab.grid(row=0, column=1, sticky='news')
    raise_frame(fVocab)
    tkinter.Label(fVocab, text="Avaliable Vocab:").pack(padx=pad_x)
    for i in newVocabList:
        tkinter.Label(fVocab, text=i[0]+" | "+i[1]).pack(padx=pad_x)
    global fVocab
def addEditVocab(event=None):
    for index, i in enumerate(newVocabList):
        for index2, i2 in enumerate(i):
            if change1.get() == i2:
                change2.configure(text="")
                newVocabList[index][index2] = change3.get()
                #save
                out_file = open(edit1.get() + ".dat","wb")
                pickle.dump(newVocabList, out_file)
                out_file.close()
                #clean
                change1.delete(0, "end")
                change3.delete(0, "end")
                edit1.delete(0, "end")
                fVocab.destroy()
                raise_frame(fChoice)
            else:
                change2.configure(text="Vocab Not Found!")    
def printVocab():
    fPrint =tkinter.Frame(window)
    fPrint.grid(row=0, column=0, sticky='news')
    raise_frame(fPrint)    
    for i in vocab:
        tkinter.Label(fPrint, text=i[0]+" | "+i[1]).pack()
    tkinter.Button(fPrint, text="Back", command=lambda:stopPrintVocab(fPrint)).pack(pady=pad_y)
def stopPrintVocab(fPrint):
    fPrint.destroy()
    raise_frame(fChoice)

    
def raise_frame(frame):
    frame.tkraise()

pad_x=10
pad_y=20

window = tkinter.Tk()
fHome =tkinter.Frame(window)
fLoad =tkinter.Frame(window)
fChoiceLT =tkinter.Frame(window)
fLearn =tkinter.Frame(window)
fLearnt =tkinter.Frame(window)
fTest =tkinter.Frame(window)
fChoice =tkinter.Frame(window)
fNew =tkinter.Frame(window)
fEdit =tkinter.Frame(window)
fChange =tkinter.Frame(window)
fAdd =tkinter.Frame(window)
fPrintI =tkinter.Frame(window)
fSave =tkinter.Frame(window)
fSize =tkinter.Frame(window)
#print
#tested


for frame in (fHome, fLoad, fChoiceLT, fLearn, fLearnt, fTest, fChoice, fNew, fEdit, fChange, fAdd, fPrintI, fSave, fSize):
    frame.grid(row=0, column=0, sticky='news')
    
window.wm_iconbitmap("favicon.ico")
window.title("Vocab")# Depressed")
#home
tkinter.Label(fHome, text ="""Welcome to Vocab Learner!
Would you like to:""").pack()
tkinter.Button(fHome, text="Load Vocab", command=lambda:raise_frame(fLoad)).pack(pady=pad_y)
tkinter.Button(fHome, text="Add/Edit Vocab", command=lambda:raise_frame(fChoice)).pack(pady=pad_y)
tkinter.Button(fHome, text="Quit", command=exit).pack(pady=pad_y)
#load
tkinter.Label(fLoad, text="What vocab do you want to load?").pack()
module_entry = tkinter.Entry(fLoad)
module_entry.pack(pady=pad_y)
module_entry.bind('<Return>', loadVocab)
tkinter.Button(fLoad, text="Load", command=loadVocab).pack(pady=pad_y)
invalid_lbl = tkinter.Label(fLoad, text="")
invalid_lbl.pack(pady=pad_y)
tkinter.Button(fLoad, text="Back", command=lambda:raise_frame(fHome)).pack(pady=pad_y)
#choice l/t
tkinter.Label(fChoiceLT, text="Do you want to:").pack()
tkinter.Button(fChoiceLT, text="Learn Vocab", command=initLearnVocab).pack(pady=pad_y)
tkinter.Button(fChoiceLT, text="Test Vocab", command=initTestVocab).pack(pady=pad_y)
tkinter.Button(fChoiceLT, text="Back", command=lambda:raise_frame(fHome)).pack(pady=pad_y)
#learn
learn1 = tkinter.Label(fLearn, text="")
learn2 = tkinter.Label(fLearn, text="")
learn3 = tkinter.Entry(fLearn)
learn3.bind('<Return>', checkLearnVocab)
learn4 = tkinter.Label(fLearn, text="")
learn5 = tkinter.Button(fLearn, text="Check", command=checkLearnVocab)
learn6 = tkinter.Label(fLearn, text="""For referance:
Ä	ALT+0196
ä	ALT+0228
Ö	ALT+0214
ö	ALT+0246
Ü	ALT+0220
ü	ALT+0252""")
learn1.pack()
tkinter.Button(fLearn, text="Show", command=showVocab).pack()
learn2.pack(pady=pad_y)
learn3.pack(pady=pad_y)
learn4.pack(pady=pad_y)
learn5.pack(pady=pad_y)
learn6.pack(pady=pad_y)
tkinter.Button(fLearn, text="Back", command=lambda:raise_frame(fChoiceLT)).pack(pady=pad_y)
#learnt
tkinter.Label(fLearnt, text="""Congratulations!!
You have learnt your vocab!""").pack()
tkinter.Button(fLearnt, text="Done", command=lambda:raise_frame(fChoiceLT)).pack(pady=pad_y)
#test
test1 = tkinter.Label(fTest, text="")
test2 = tkinter.Entry(fTest)
test2.bind('<Return>', checkTestVocab)
test3 = tkinter.Label(fTest, text="")
test4 = tkinter.Button(fTest, text="Check", command=checkTestVocab)
test5 = tkinter.Label(fTest, text="""For referance -
Ä	ALT+0196
ä	ALT+0228
Ö	ALT+0214
ö	ALT+0246
Ü	ALT+0220
ü	ALT+0252""")
test1.pack()
test2.pack(pady=pad_y)
test3.pack(pady=pad_y)
test4.pack(pady=pad_y)
test5.pack(pady=pad_y)
tkinter.Button(fTest, text="Back", command=lambda:raise_frame(fChoiceLT)).pack(pady=pad_y)
#tested, function
#choice
tkinter.Label(fChoice, text="Do you want to:").pack()
tkinter.Button(fChoice, text="Create New Vocab List", command=initNewVocab).pack(pady=pad_y)
tkinter.Button(fChoice, text="Edit Existing Vocab List", command=lambda:raise_frame(fEdit)).pack(pady=pad_y)
tkinter.Button(fChoice, text="Add Words to Existing Vocab List", command=lambda:raise_frame(fAdd)).pack(pady=pad_y)
tkinter.Button(fChoice, text="Print a Vocab List", command=lambda:raise_frame(fPrintI)).pack(pady=pad_y)
tkinter.Button(fChoice, text="Back", command=lambda:raise_frame(fHome)).pack(pady=pad_y)
#new
tkinter.Label(fNew, text="Create New Vocab").pack()
tkinter.Label(fNew, text="Enter German:").pack(pady=pad_y)
new2 = tkinter.Entry(fNew)#entry done
new2.pack(pady=pad_y)
tkinter.Label(fNew, text="Enter English:").pack(pady=pad_y)
new4 = tkinter.Entry(fNew)
new4.bind('<Return>', newVocab)
new4.pack(pady=pad_y)
tkinter.Button(fNew, text="Add", command=newVocab).pack(pady=pad_y)
tkinter.Button(fNew, text="Done", command=lambda:raise_frame(fSave)).pack(pady=pad_y)
tkinter.Button(fNew, text="Back", command=lambda:raise_frame(fChoice)).pack(pady=pad_y)
#edit
tkinter.Label(fEdit, text="From which module do you want to load from:").pack()
edit1 = tkinter.Entry(fEdit)
edit1.bind('<Return>', editVocab)
edit1.pack(pady=pad_y)
edit2 = tkinter.Label(fEdit, text="")
edit2.pack(pady=pad_y)
tkinter.Button(fEdit, text="Edit", command=editVocab).pack(pady=pad_y)
tkinter.Button(fEdit, text="Back", command=lambda:raise_frame(fChoice)).pack(pady=pad_y)
#editChange
tkinter.Label(fChange, text="What do you want to change:").pack()
change1 = tkinter.Entry(fChange)
change1.pack(pady=pad_y)
change2 = tkinter.Label(fChange, text="")
change2.pack()
tkinter.Label(fChange, text="to:").pack(pady=pad_y)
change3 = tkinter.Entry(fChange)
change3.bind("<Return>", addEditVocab)
change3.pack()
tkinter.Button(fChange, text="Done", command=addEditVocab).pack(pady=pad_y)
#add
tkinter.Label(fAdd, text="What vocab do you want to add?").pack()
tkinter.Label(fAdd, text="Enter German:").pack(pady=pad_y)
add1 = tkinter.Entry(fAdd)#entry done
add1.pack(pady=pad_y)
tkinter.Label(fAdd, text="Enter English:").pack(pady=pad_y)
add2 = tkinter.Entry(fAdd)#entry done
add2.pack(pady=pad_y)
tkinter.Label(fAdd, text="From Vocab List:").pack(pady=pad_y)
add3 = tkinter.Entry(fAdd)
add3.bind('<Return>', addVocab)
add3.pack(pady=pad_y)
add4 = tkinter.Label(fAdd, text="")
add4.pack(pady=pad_y)
tkinter.Button(fAdd, text="Add", command=addVocab).pack(pady=pad_y)
tkinter.Button(fAdd, text="Back", command=lambda:raise_frame(fChoice)).pack(pady=pad_y)
#printI
tkinter.Label(fPrintI, text="What vocab do you want to load?").pack()
printI1 = tkinter.Entry(fPrintI)
printI1.bind('<Return>', loadVocab2)
printI1.pack(pady=pad_y)
tkinter.Button(fPrintI, text="Load", command=loadVocab2).pack(pady=pad_y)
printI2 = tkinter.Label(fPrintI, text="")
printI2.pack(pady=pad_y)
tkinter.Button(fPrintI, text="Back", command=lambda:raise_frame(fChoice)).pack(pady=pad_y)
#print, done in a function
#save
tkinter.Label(fSave, text="Save to Module:").pack()
save1 = tkinter.Entry(fSave)
save1.bind('<Return>', saveVocab)
save1.pack(pady=pad_y)
tkinter.Button(fSave, text="Done", command=saveVocab).pack(pady=pad_y)
#size, this sets the size of the window
tkinter.Label(fSize, text="").pack(pady=200, padx=200)


#.bind('<Return>', func)
#run
raise_frame(fHome)
window.mainloop()
print()
while True:
    print("""Welcome to Vocab Learner!
No Vocab Loaded!
Would you like to:
2 - Add/Edit Vocab
""")

    choice = input("\n>")

    #add/edit Vocab
    if choice == "2":
        print("Do you want edit existing vocab? (1)")
        choice = input(">")
        
        #edit vocab
        if choice == "1":
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
                        
