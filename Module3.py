import re

text = """homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
text1 = text.lower()
print(text1)
my_list = text1.splitlines(True)
print(my_list)

new_list1 = []
new_list1 = [my_list_item.replace('\t', '') for my_list_item in my_list]
print(new_list1)
new_list2 = [my_list_item.split('.') for my_list_item in new_list1]
#print(new_list)
print(new_list2)
replaced = [item.capitalize() for item in new_list2]
print(replaced)


replaced = re.sub(r'homework:', 'Homework:', my_list[1])

replaced = re.sub(r'homework:', 'Homework:', text1)
replaced = re.sub(r'this iz', 'This is', replaced)
replaced = re.sub(r'you need', 'You need', replaced)
replaced = re.sub(r'also,', 'Also,', replaced)
replaced = re.sub(r'it iz', 'It is', replaced)
replaced = re.sub(r'fix', 'Fix ', replaced)
replaced = re.sub(r'n It', 'n it', replaced)
replaced = re.sub(r'last iz', 'Last is', replaced)
replaced = re.sub(r'carefull,', 'Carefully, ', replaced)
replaced = re.sub(r'i got', 'I got', replaced)

new_sentence_words = re.findall(r'\w*\.', replaced)
new_sentence = ' '.join(new_sentence_words)
new_sentence1 = new_sentence.replace('.', '')

new_text = replaced + new_sentence1
new_text = re.sub(r'87.var', '87. Var', new_text)
#print(new_text)

count = 0

for i in range(0, len(new_text)):
    if new_text[i] == " ":
        count += 1
print(count)
