from inflect import Words

def sorting(filename):
  infile = open(filename)
  words = []

  for line in infile:
    temp = line.split()
    for i in temp:
      words.append(i)
  infile.close()

  words.sort()

  outfile = open('Keyword_sorted.txt', 'a', encoding='utf-8')
  for i in words:
    outfile.writelines(i)
    outfile.writelines("\n")
  outfile.close()


sorting('Keyword_unique.txt')