def calculateNGrams(text,n):
    n_grams= []
    if len(text)<n:
        raise Exception("Integer larger than text, not available N-gram for this")
    else:
        index = 0
        while n+index<= len(text):
            n_grams.append(text[index:n+index])
            index +=1
    
    print(f'this are the {n}-grams',n_grams)
    return (n_grams)


def gettingFrecuency(array):
    words = dict()
    one_of_most_frecuent=array[0]
    for word in array:
        if not word in words:
            words[word] =0
        words[word] +=1
        if words[one_of_most_frecuent] < words[word]:
            one_of_most_frecuent = word

    return one_of_most_frecuent, words



def mostFrequentNgram(text,n):
    array = calculateNGrams(text,n)
    one_of_most_frecuent,words = gettingFrecuency(array)
    most_times = words [one_of_most_frecuent]
    most_frecuent = ''

    for word, times in words.items():
        if words[word] == most_times:
            most_frecuent= word
            break
    print(most_frecuent, f'is the most frecuent {n}-gram')
    return most_frecuent


if __name__ == '__main__':
    mostFrequentNgram('to be or not to be',2)