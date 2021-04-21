
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
    print(n_grams)
def mostFrequentNgram(text ,n):
    pass



if __name__ == '__main__':
    calculateNGrams('Slang',5)