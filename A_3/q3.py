words = input("enter a comma-separated sequence of words ")
word_list = [word.strip() for word in words.split(",")]
word_list.sort()
print(",".join(word_list))
