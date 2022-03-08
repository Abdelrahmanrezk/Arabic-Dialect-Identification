
from gensim.models import Word2Vec
import numpy as np


def load_word2vec_model(model_path):
    word_to_vec_model = Word2Vec.load(model_path)
    return word_to_vec_model



def ML_text_to_matrix_using_word2vec(word_to_vec_model, text_list, number_of_features, max_len_str):
    '''
    The function used to build our word2vec matrix for the training and testing data.
    Argument:
            List of string each of them is list of words
            the word_to_vec_model model
            number of features you apply to word2vec model
            number of words of greatest string in your reviews
    return:
        embedding matrix that can apply to machine learning algorithms
    '''
    embedding_matrix            = np.zeros((len(text_list), number_of_features*max_len_str)) # largest sentence and 5 fetures
    print("The shape of matrix", embedding_matrix.shape)
#loop over each review
    for index,text in enumerate(text_list):
# list of each reviw which will be appended to embedding matrix
        one_sentence_list       = [] 
        for word in text:
            try:
                word                = word_to_vec_model[word]
                one_sentence_list.extend(word)
            except:
                pass
            
# make padding for small strings
        zero_pad                = np.zeros(number_of_features*max_len_str-len(one_sentence_list))
        zero_pad                = list(zero_pad)
    
# apply the padding
        one_sentence_list.extend(zero_pad)
        embedding_matrix[index] = one_sentence_list
    return embedding_matrix