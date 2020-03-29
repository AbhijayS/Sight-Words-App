import tkinter
from math import *

index = 0
group_size = 5
curr_group = 0
reps = 5
words = ["a","and","away","big","blue","can","come","down","find","for","funny","go","help","here","I","in","is","it","jump","little","look","make","me","my","not","one","play","red","run","said","see","the","three","to","two","up","we","where","yellow","you"]
word = words[index]
wordmap = {}

for i in range(len(words)):
    wordmap[words[i]] = 0

def correct(event):
    global index
    global word
    global curr_group
    global group_size
    global reps

    wordmap[word] = min(wordmap[word]+1, reps)

    # group has finished reps
    if (hasFinishedReps()):
        nextWord(event)
    else:
        # go to next word in the current group
        index = curr_group*group_size + ((index+1) % group_size)
        word = words[index]
        wordVar.set(word)
    print(wordmap)
    

def incorrect(event):
    global index
    global word
    global curr_group
    global group_size
    global reps

    # go to next word in the current group
    index = curr_group*group_size + ((index+1) % group_size)
    word = words[index]
    wordVar.set(word)
    print(wordmap)

def previousWord(event):
    global index
    global word
    global curr_group
    global group_size
    global reps

    index = (index-1) % len(words)

    if (index == len(words)-1):
        curr_group = ceil(len(words)/group_size)-1
    elif (index%group_size == group_size-1):
        curr_group -= 1

    word = words[index]
    wordVar.set(word)

def nextWord(event):
    global index
    global word
    global curr_group
    global group_size
    global reps

    index = (index+1) % len(words)

    if (index == 0):
        curr_group = 0
    elif (index % group_size == 0):
        curr_group += 1
    
    word = words[index]
    wordVar.set(word)

def hasFinishedReps():
    global index
    global word
    global curr_group
    global group_size
    global reps

    i = curr_group*group_size
    while (i < min(curr_group*group_size + group_size, len(words))):
        if (wordmap[words[i]] != reps):
            return False
        i+=1
    return True

root = tkinter.Tk()
root.state('zoomed')

wordVar = tkinter.StringVar(root, value=word)
wordLabel = tkinter.Label(root, textvariable=wordVar)
wordLabel.config(font=("Sans serif", 500))
wordLabel.pack()

root.bind("<Left>", incorrect)
root.bind("<Right>", correct)
root.bind("<Up>", previousWord)
root.bind("<Down>", nextWord)

root.mainloop()