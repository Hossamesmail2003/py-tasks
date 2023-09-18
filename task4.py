'''Create a function that takes a sentence and prints the sentence without duplicated words'''
def duple_words(sentence):
    words= sentence.split(' ')
    uniqe_words=[]
    for w in words:
        if w in uniqe_words:
            continue
        else:
            uniqe_words.append(w)
    print(uniqe_words)     
duple_words('hossam hossam esmail elsayed')        