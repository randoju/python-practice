

def words_reverse(s):
    list_words=[]
    s_list=s.split()
    while (len(s_list))>0:
        word = s_list.pop()
        list_words.append(word)
    return ' '.join(list_words)

sentence = "This is GeekCoders"
print(words_reverse(sentence))

#in Python, the pop() method, when used on a list without providing an index, removes and returns the last element by default