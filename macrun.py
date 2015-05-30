import xmltools
from os.path import isfile, join, isdir

file_path = '/Users/tongwang/Desktop/exp/lda/ap.txt'
folder_path = '/Users/tongwang/Desktop/exp/lda/ap/'
p = open(file_path, 'r')
s = p.read()
p.close()

texts = xmltools.extractTextBetweenTags(s, 'TEXT')
titles = xmltools.extractTextBetweenTags(s, 'DOCNO')

for i in xrange(len(texts)):
	p = open(join(folder_path, titles[i]),'w')
	p.write(texts[i])
	p.close()
