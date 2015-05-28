import os
import numpy as np
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



class Model:

	def __init__(self, model_path, binary=False):
		self.model_path = model_path
		if binary is False:
			self.model = gensim.models.Word2Vec.load(model_path)
		else:
			self.model = gensim.models.Word2Vec.load_word2vec_format(model_path, binary=True)
		
	def initother(self, voc_path, matrix_path):
		self.model_path = model_path
		self.voc_path = voc_path
		self.matrix_path = matrix_path
		self.model = gensim.models.Word2Vec.load(model_path)
		if not os.path.exists(matrix_path):
			os.makedirs(matrix_path)

	def getId2Word(self):
		p = open(self.voc_path, 'r')
		content = p.read().rstrip()
		p.close()
		id2word = {}
		word2id = {}
		content = content.split('\n')
		for item in content:
			id = item[:item.index(':')]
			word = item[item.index(':') + 1:]
			id2word[id] = word
			word2id[word] = id
		return id2word, word2id
		
	def saveSimMatrix(self):
		id2word, word2id = self.getId2Word()
		size = len(id2word)
		for i in xrange(size):
			print i
			sim = np.zeros((1, size))
			word1 = id2word[str(i)]	
			for j in xrange(size):
				word2 = id2word[str(j)]
				try:
					sim[0][j] = self.model.similarity(word1, word2)
				except KeyError:
					print 'KeyError: ' + word1 + ' ' + word2
					sim[0][j] = 0
				except:
					print "Unexpected error:", sys.exc_info()[0]
					
			filepath = os.path.join(self.matrix_path, str(i))
			np.savetxt(filepath,sim)
	

#sim = np.zeros((size, size))  memory error



