'''Create a function that takes a sentence and word and remove the word from the sentence'''
def remove_word(x,y):
    words=x.split()
    fillter=[]
    for w in words:
        if w !=y:
            fillter.append(w)
        else:
            continue
    print(fillter)
remove_word('hossam esmail elsayed','elsayed')    