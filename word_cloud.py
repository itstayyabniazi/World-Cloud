# Python 3

# Be sure you have followed the instructions to download the 98-0.txt,
# the text of A Tale of Two Cities, by Charles Dickens

import collections

file=open('I:\# BEE-60\Sem-3\DSA\Assingment-1\98-0.txt', encoding="utf8")

content = file.read()
lowered_content = content.lower()
words_into_list = lowered_content.split()

# print(lowered_content)
# print(words_into_list)

# if you want to use stopwords, here's an example of how to do this
stopwords = set(line.strip() for line in open('I:\# BEE-60\Sem-3\DSA\Assingment-1\stopwords'))

# Instantiate a dictionary, and for every word in the file, add to 
# the dictionary if it doesn't exist. If it does, increase the count.

# Hint: To eliminate duplicates, remember to split by punctuation, 
# and use case demiliters. The functions lower() and split() will be useful!


def without_using_stopword():
    # create your data structure here.  F
    wordcount={}
    for word in words_into_list:
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace("\"","")
        word = word.replace("“","")
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount

def using_stopword():
    # create your data structure here.  F
    wordcount={}
    for word in words_into_list:
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace("\"","")
        word = word.replace("“","")
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    return wordcount

print("Welcome!\n-> Chose any one option <-\n1.Wordcloud without Stop Word.\n2.Worldcloud using Stop Word.")
choice = int(input("=>"))
if choice == 1:
    wording = without_using_stopword()
elif choice == 2:
    wording = using_stopword()
else:
    print("Invalid Choice!")

# after building your wordcount, you can then sort it and return the first
# n words.  If you want, collections.Counter may be useful.
# print(wordcount)
for word, count in wording.items():
    print(word, ": ", count, end='\t')

print("\n-> Most Common word used are:")
d = collections.Counter(wording)

# print(d.most_common(10))
for word, count in d.most_common(10):
    print(word, ": ", count)