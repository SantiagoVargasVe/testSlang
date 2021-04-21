
def calculateNGrams(text,n):
    exact_divide = True if len(text)%n==0 else False
    n_grams= []
    if len(text)<n:
        raise Exception("Integer larger than text, not available N-gram for this")
    else:
        index = 0
        while n+index<= len(text):
            if n+index<= len(text):
                n_grams.append(text[index:n+index])
            index +=1
    #print(n_grams)
    return (n_grams)
def mostFrequentNgram(array ,n):
    words = dict()

    for word in array :
        if not word in words:
            words[word] =0
        print(word)
        words[word] +=1
    
    print(words)



if __name__ == '__main__':
    n_gramed_text =calculateNGrams('to be or not to be',2)
    mostFrequentNgram(n_gramed_text,2)