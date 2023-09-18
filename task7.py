'''Create a function takes a sentence and a word and prints how many time the word used in the sentence'''
def count_words(sentence,word):
    words=sentence.split()
    count=0
    for w in words:
        if w ==word :
            count+=1
    print(count)
          

count_words('hossam esmail esmail esmail','esmail')