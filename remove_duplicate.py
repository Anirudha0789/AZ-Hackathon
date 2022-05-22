file1 = open('Keyword.txt', 'r', encoding='utf-8')
words = file1.read()

fo1 = open('Keyword_unique.txt', 'a', encoding='utf-8')
fo1.write('\n'.join(dict.fromkeys(words.split())))