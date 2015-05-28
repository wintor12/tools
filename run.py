import tools
import os
from os.path import join
import numpy as np
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from word2vec_process import Model
from word2vec_train import MySentences

path = 'C:\\Exp\\lda\\google_news'
# path_removed = "C:\\Exp\\lda\\20news\\removed\\"
# old_path ='C:\\Exp\\lda\\nips\\data_words_old'

# if not os.path.exists(old_path):
	# os.rename(path, old_path)
# if not os.path.exists(path):
    # os.makedirs(path)

# print os.listdir('C:\\Exp\\lda\\nips\\data_words_old')
# tools.listFiles(old_path)	
# tools.keepEnglishWords(old_path, path)
# tools.removeLen2Words(old_path, path)



# docs = tools.listFiles(path_removed)
# tools.removeDocs(docs, join(path, 'data'))
# tools.removeDocs(docs, join(path, 'data_trees'))
# tools.removeDocs(docs, join(path, 'data_edges'))


# tools.removeFoldersWithSmallNoDocs(path, 20)
# folders = tools.listFolders(path)
# for folder in folders:
	# tools.removeFilesWithSmallSize(join(path, folder), 2000)

# tools.mergeMultiFoldersToOne(path, 'C:\\Exp\\lda\\googlenews', True)

# model_path = 'C:\\Exp\\lda_acl\\20news_test7\\word2vec_model'
# model_path2 = 'C:\\Exp\\lda_acl\\20news_test7\\GoogleNews-vectors-negative300.bin'
# voc_path = 'C:\\Exp\\lda_acl\\20news_test7\\idAndWord_30_1000'
# matrix_path = 'C:\\Exp\\lda_acl\\20news_test7\\sim_matrix'
# sentences_path = 'C:\\Exp\\lda_acl\\20news_test7\\data_sentences'

# sentences = MySentences(sentences_path)
# model = gensim.models.Word2Vec(sentences, min_count = 10)
# model.save(model_path)

# m = Model(model_path)
# m2 = Model(model_path2, True)
# print m.model.similarity('add', 'agree')
# print m2.model.similarity('add', 'agree')


# process = Model(model_path, voc_path, matrix_path)
# process.saveSimMatrix()


# path_word = "C:\\Exp\\lda_acl\\20news\\data_words"
# path_tree = "C:\\Exp\\lda_acl\\20news\\data_trees"
# path_edge = "C:\\Exp\\lda_acl\\20news\\data_edges"

# files = tools.randomFileNames(path_word, 1000)
# tools.copyFilesFromList(files, path_word, "C:\\Exp\\lda_acl\\20news_1000\\data_words")
# tools.copyFilesFromList(files, path_tree, "C:\\Exp\\lda_acl\\20news_1000\\data_trees")
# tools.copyFilesFromList(files, path_edge, "C:\\Exp\\lda_acl\\20news_1000\\data_edges")

file_path = "C:\\Exp\\lda\\20news_100_1\\eval"
tools.averageRes(file_path)


