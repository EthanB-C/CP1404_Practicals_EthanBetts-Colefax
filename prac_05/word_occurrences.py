TEXT = "this is a collection of words of nice words this is a fun thing it is"
text_dict = {}

text_list = TEXT.split()
for word in text_list:
    if word in text_dict:
        text_dict[word] += 1
    else:
        text_dict[word] = 1
print(f"Text = {TEXT}")

longest_word = 0
for word in text_dict.keys():
    if len(word) > longest_word:
        longest_word = len(word)
print(longest_word)

for word, count in text_dict.items():
    print(f"{word} : {count}")
