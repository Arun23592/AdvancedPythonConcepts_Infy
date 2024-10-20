def find_largest_word(sentence):
    words = sentence.split()
    largest_word = max(words, key=len)
    return largest_word

sentence = "Welcome to cognizant interviewprocess"
largest_word = find_largest_word(sentence)
print("The largest word is :", largest_word)