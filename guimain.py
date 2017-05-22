#german vocab learner
#ver 0.5
import tkinter
import pickle
import random

#data structure object
class Data:
    def __init__():
        vocab = []
        tempVocab = []
        done = []
        incorrect = []
        score = 0
        current = []
        position = 0
        phrase = ""
        newVocabList = []
        fVocab = ""

def saveVocab(data):#fixed
    name = save1.get()     
    out_file = open(name + ".dat","wb")
    pickle.dump(data.newVocabList, out_file)
    out_file.close()
    raise_frame(fChoice)
    #clear entry
    save1.delete(0, "end")
def loadVocab(data):#fixed
    try:
        in_file = open(module_entry.get() + ".dat","rb")
        data.vocab = pickle.load(in_file)
        in_file.close()
    except FileNotFoundError:                
        invalid_lbl.configure(text="Incorrect Input")
    else:
        raise_frame(fChoiceLT)
        #clear entry
        module_entry.delete(0, "end")
        invalid_lbl.configure(text="")
def loadVocab2(data):#fixed
    try:
        in_file = open(printI1.get() + ".dat","rb")
        data.vocab = pickle.load(in_file)
        in_file.close()
    except FileNotFoundError:                
        printI2.configure(text="Incorrect Input")
    else:
        printVocab(data)
        #clear entry
        printI1.delete(0, "end")
        printI2.configure(text="")
def testedVocab(data):#fixed
    fTested = tkinter.Frame(window)
    fTested.grid(row=0, column=0, sticky='news')
    tested1 = tkinter.Label(fTested, text="")
    tested1.pack()
    raise_frame(fTested)            
    tested1.configure(text="You got "+str(data.score)+" correct")
    tkinter.Label(fTested, text="Theses are the words you got wrong:").pack(pady=pad_y)
    for i in data.incorrect:
        tkinter.Label(fTested, text=i[0]+" - "+i[1]).pack()
    tkinter.Button(fTested, text="Done", command=lambda:stopTested(fTested)).pack(pady=pad_y)
def stopTested(fTested):#fixed#
    fTested.destroy()
    raise_frame(fChoiceLT)
def initTestVocab(data):
    raise_frame(fTest)
    data.position = 0
    data.tempVocab = [i for i in data.vocab]
    data.done = []
    data.incorrect = []
    data.score = 0
    data.current = []
    testVocab(data)
def testVocab(data):#fixed?
    if data.position < len(data.vocab):
        i = random.choice(data.tempVocab)
        data.current = i
        test1.configure(text="What's " + i[0] + " in English?")        
        data.done.append(i)
        data.tempVocab.remove(i)
    elif data.position >= len(data.vocab):
        i = random.choice(data.done)
        test1.configure(text="What's " + i[1] + " in German?")
        data.current = i       
def checkTestVocab(data):#fixed
    i = data.current
    if data.position < len(data.vocab):
        if test2.get() == i[1]:
            test3.configure(text="Correct")
            data.score += 1
        else:
            test3.configure(text="Incorrect, it's " + i[1])
            if i not in data.incorrect:
                data.incorrect.append(i)
        test2.delete(0, "end")
        data.position += 1
        testVocab(data)
    elif data.position >= len(data.vocab):
        if test2.get() == i[0]:
            test3.configure(text="Correct")
            data.score += 1
        else:
            test3.configure(text="Incorrect, it's " + i[0])
            if i not in data.incorrect:
                data.incorrect.append(i)
        data.done.remove(i)
        test2.delete(0, "end")
        if data.position+1 == 2*len(data.vocab):
            #clear entry
            test2.delete(0, "end")
            test3.configure(text="")
            testedVocab(data)
        else:
            data.position += 1
            testVocab(data)
        
#init vocab learning        
def initLearnVocab(data):
    raise_frame(fLearn)
    data.position = 0
    learnVocab(data)  
def learnVocab(data):    
    if data.position < len(data.vocab):
        i = data.vocab[data.position]
        learn1.configure(text=i[0] + " means <Hiddden>")
        learn2.configure(text="What's " + i[0] + " in English?")
        data.phrase = i[0] + " means " + i[1]
    elif data.position >= len(data.vocab):
        i = data.vocab[data.position - len(data.vocab)]
        learn1.configure(text=i[1] + " means <Hiddden>")
        learn2.configure(text="What's " + i[1] + " in German?")
        data.phrase = i[1] + " means " + i[0]
def showVocab(data):#fixed
    learn1.configure(text=data.phrase)
def checkLearnVocab(data):#fixed
    if data.position < len(data.vocab):
        i = data.vocab[data.position]
        if learn3.get() == i[1]:
            learn3.delete(0, "end")
            learn4.configure(text="")
            learn4.configure(text="Well Done")
            data.position += 1
            learnVocab(data)
        else:
            learn4.configure(text="Incorrect, try again")
            learnVocab(data)
    elif 2*len(data.vocab)-1 > data.position >= len(data.vocab):
        i = data.vocab[data.position - len(data.vocab)]
        if learn3.get() == i[0]:
            learn3.delete(0, "end")
            learn4.configure(text="")
            learn4.configure(text="Well Done")
            data.position += 1
            learnVocab(data)
        else:
            learn4.configure(text="Incorrect, try again")
            learnVocab(data)    
    else:
        #clear entry
        learn3.delete(0, "end")
        learn4.configure(text="")
        raise_frame(fLearnt)
def initNewVocab(data):#fixed
    raise_frame(fNew)
    data.newVocabList = []
def newVocab(data):#fixed
    german = new2.get()
    english = new4.get()
    data.newVocabList.append([german, english])
    #clear entry
    new2.delete(0, "end")
    new4.delete(0, "end")
def addVocab(data):#fixed
    german = add1.get()
    english = add2.get()    
    try:
        in_file = open(add3.get() + ".dat","rb")
        data.newVocabList = pickle.load(in_file)
        in_file.close()
    except FileNotFoundError:                
        add4.configure(text="File Not There")
    else:
        #clear entry
        add1.delete(0, "end")
        add2.delete(0, "end")
        add3.delete(0, "end")
        add4.configure(text="")
        data.newVocabList.append([german, english])
        raise_frame(fSave)
def editVocab(data):#fixed
    try:
        in_file = open(edit1.get() + ".dat","rb")
        data.newVocabList = pickle.load(in_file)
        in_file.close()
    except FileNotFoundError:                
        edit2.configure(text="File Not There")
    else:
        #clear entry, done in add edit vocab
        edit2.configure(text="")
        raise_frame(fChange)
        initEditVocab(data)
def initEditVocab(data):#fixed
    #clearing label
    change2.configure(text="")
    data.fVocab = tkinter.Frame(window)
    data.fVocab.grid(row=0, column=1, sticky='news')
    raise_frame(data.fVocab)
    tkinter.Label(data.fVocab, text="Avaliable Vocab:").pack(padx=pad_x)
    for i in data.newVocabList:
        tkinter.Label(data.fVocab, text=i[0]+" | "+i[1]).pack(padx=pad_x)
def addEditVocab(data):
    for index, i in enumerate(data.newVocabList):
        for index2, i2 in enumerate(i):
            if change1.get() == i2:
                change2.configure(text="")
                data.newVocabList[index][index2] = change3.get()
                #save
                out_file = open(edit1.get() + ".dat","wb")
                pickle.dump(data.newVocabList, out_file)
                out_file.close()
                stopEditVocab(data)
            else:
                change2.configure(text="Vocab Not Found!")
def stopEditVocab(data):
    change1.delete(0, "end")
    change2.configure(text="") 
    change3.delete(0, "end")
    edit1.delete(0, "end")
    change2.configure(text="") 
    data.fVocab.destroy()
    raise_frame(fChoice)
def printVocab(data):
    fPrint =tkinter.Frame(window)
    fPrint.grid(row=0, column=0, sticky='news')
    raise_frame(fPrint)
    for i in data.vocab:
        tkinter.Label(fPrint, text=i[0]+" | "+i[1]).pack()
    tkinter.Button(fPrint, text="Back", command=lambda:stopPrintVocab(fPrint)).pack(pady=pad_y)
def stopPrintVocab(fPrint):
    fPrint.destroy()
    raise_frame(fChoice)

    
def raise_frame(frame):
    frame.tkraise()

#predefined dimensions
pad_x=10
pad_y=20

#defining frames
window = tkinter.Tk()
window.resizable(0,0)
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

#organising frames
for frame in (fHome, fLoad, fChoiceLT, fLearn, fLearnt, fTest, fChoice, fNew, fEdit, fChange, fAdd, fPrintI, fSave, fSize):
    frame.grid(row=0, column=0, sticky='news')

#main object containing data that is passed around
data = Data
#cool window stuff
window.wm_iconbitmap("icon.ico")
window.title("Vocab")
#FRAMES-------------------------------------------
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
module_entry.bind('<Return>', lambda event:loadVocab(data))
tkinter.Button(fLoad, text="Load", command=lambda:loadVocab(data)).pack(pady=pad_y)
invalid_lbl = tkinter.Label(fLoad, text="")
invalid_lbl.pack(pady=pad_y)
tkinter.Button(fLoad, text="Back", command=lambda:raise_frame(fHome)).pack(pady=pad_y)
#choice l/t
tkinter.Label(fChoiceLT, text="Do you want to:").pack()
tkinter.Button(fChoiceLT, text="Learn Vocab", command=lambda:initLearnVocab(data)).pack(pady=pad_y)
tkinter.Button(fChoiceLT, text="Test Vocab", command=lambda:initTestVocab(data)).pack(pady=pad_y)
tkinter.Button(fChoiceLT, text="Back", command=lambda:raise_frame(fHome)).pack(pady=pad_y)
#learn
learn1 = tkinter.Label(fLearn, text="")
learn2 = tkinter.Label(fLearn, text="")
learn3 = tkinter.Entry(fLearn)
learn3.bind('<Return>', lambda event:checkLearnVocab(data))
learn4 = tkinter.Label(fLearn, text="")
learn5 = tkinter.Button(fLearn, text="Check", command=lambda:checkLearnVocab(data))
learn6 = tkinter.Label(fLearn, text="""For reference:
Ä	ALT+0196
ä	ALT+0228
Ö	ALT+0214
ö	ALT+0246
Ü	ALT+0220
ü	ALT+0252""")
learn1.pack()
tkinter.Button(fLearn, text="Show", command=lambda:showVocab(data)).pack()
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
test2.bind('<Return>', lambda event:checkTestVocab(data))
test3 = tkinter.Label(fTest, text="")
test4 = tkinter.Button(fTest, text="Check", command=lambda:checkTestVocab(data))
test5 = tkinter.Label(fTest, text="""For reference -
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
tkinter.Button(fChoice, text="Create New Vocab List", command=lambda:initNewVocab(data)).pack(pady=pad_y)
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
new4.bind('<Return>', lambda event:newVocab(data))
new4.pack(pady=pad_y)
tkinter.Button(fNew, text="Add", command=lambda:newVocab(data)).pack(pady=pad_y)
tkinter.Button(fNew, text="Done", command=lambda:raise_frame(fSave)).pack(pady=pad_y)
tkinter.Button(fNew, text="Back", command=lambda:raise_frame(fChoice)).pack(pady=pad_y)
#edit
tkinter.Label(fEdit, text="From which module do you want to load from:").pack()
edit1 = tkinter.Entry(fEdit)
edit1.bind('<Return>', lambda event:editVocab(data))
edit1.pack(pady=pad_y)
edit2 = tkinter.Label(fEdit, text="")
edit2.pack(pady=pad_y)
tkinter.Button(fEdit, text="Edit", command=lambda:editVocab(data)).pack(pady=pad_y)
tkinter.Button(fEdit, text="Back", command=lambda:raise_frame(fChoice)).pack(pady=pad_y)
#editChange
tkinter.Label(fChange, text="What do you want to change:").pack()
change1 = tkinter.Entry(fChange)
change1.pack(pady=pad_y)
change2 = tkinter.Label(fChange, text="")
change2.pack()
tkinter.Label(fChange, text="to:").pack(pady=pad_y)
change3 = tkinter.Entry(fChange)
change3.bind("<Return>", lambda event:addEditVocab(data))
change3.pack()
tkinter.Button(fChange, text="Done", command=lambda:addEditVocab(data)).pack(pady=pad_y)
tkinter.Button(fChange, text="Back", command=lambda:stopEditVocab(data)).pack(pady=pad_y)
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
add3.bind('<Return>', lambda event:addVocab(data))
add3.pack(pady=pad_y)
add4 = tkinter.Label(fAdd, text="")
add4.pack(pady=pad_y)
tkinter.Button(fAdd, text="Add", command=lambda:addVocab(data)).pack(pady=pad_y)
tkinter.Button(fAdd, text="Back", command=lambda:raise_frame(fChoice)).pack(pady=pad_y)
#printI
tkinter.Label(fPrintI, text="What vocab do you want to load?").pack()
printI1 = tkinter.Entry(fPrintI)
printI1.bind('<Return>', lambda event:loadVocab2(data))
printI1.pack(pady=pad_y)
tkinter.Button(fPrintI, text="Load", command=lambda:loadVocab2(data)).pack(pady=pad_y)
printI2 = tkinter.Label(fPrintI, text="")
printI2.pack(pady=pad_y)
tkinter.Button(fPrintI, text="Back", command=lambda:raise_frame(fChoice)).pack(pady=pad_y)
#print, done in a function
#save
tkinter.Label(fSave, text="Save to Module:").pack()
save1 = tkinter.Entry(fSave)
save1.bind('<Return>', lambda event:saveVocab(data))
save1.pack(pady=pad_y)
tkinter.Button(fSave, text="Done", command=lambda:saveVocab(data)).pack(pady=pad_y)
#size, this sets the size of the window
tkinter.Label(fSize, text="").pack(pady=200, padx=200)

#run
raise_frame(fHome)
window.mainloop()
