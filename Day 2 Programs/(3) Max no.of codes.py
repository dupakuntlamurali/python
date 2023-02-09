def maxWords(sentences):
    max_words=0
    for sentence in sentences:
        words=sentence.split()
        max_words=max(max_words,len(words))
    return max_words

sentences=["A sentence is a lis of words."]
print("The maximum number of words in a single sentence is", maxWords(sentences))
