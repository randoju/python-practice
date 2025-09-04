#19.   Remove all the punctuation characters from a given string
import re
text = "Hello, World! How's it going?"
result = re.sub(r'[^\w\s]','',text)
print(result)
