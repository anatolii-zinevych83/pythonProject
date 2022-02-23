import re

text = """homEwork:
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
text1 = text.lower()
my_list = text1.splitlines(True)

new_list1 = []
new_list1 = [my_list_item.replace('\t', '') for my_list_item in my_list]

new_list2 = [new_list1_item.capitalize() for new_list1_item in new_list1]

replaced_sentence = ' '.join(new_list2)


replaced = re.sub(r'homework:', 'Homework:', replaced_sentence)
replaced = re.sub(r'iz', 'is', replaced)
replaced = re.sub(r'ise', 'ize', replaced)
replaced = re.sub(r'also,', 'Also,', replaced)
replaced = re.sub(r'fix“is”', 'Fix “iz“', replaced)
replaced = re.sub(r'n It', 'n it', replaced)
replaced = re.sub(r'carefull,', 'Carefully,', replaced)
replaced = re.sub(r'i got', 'I got', replaced)


new_sentence_words = re.findall(r'\w*\.', replaced)
new_sentence = ' '.join(new_sentence_words)
new_sentence1 = new_sentence.replace('.', '')

new_text = replaced + new_sentence1
new_text = re.sub(r'87.var', '87. Var', new_text)
print(new_text)

count = 0

for i in range(0, len(new_text)):
    if new_text[i] == " ":
        count += 1
print(count)
