import re

def extractTextBetweenTags(s, tagname):
	r = re.compile('<' + tagname + '>(.*?)</' + tagname + '>', re.DOTALL)
	m = r.findall(s)
	return m