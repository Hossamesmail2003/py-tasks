'''Create a function that takes a sentence and prints how many words in the sentence (do not count the
spaces)'''
def counter_words(sentence):
    words=sentence.split()
    num=len(words)
    
    print(f'number is : {num}')
counter_words('hossam esmail elsayed')    