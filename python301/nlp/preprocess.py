import nltk
import string
from nltk.corpus import stopwords


def preprocess(text):
    """
    Tokenize -> Normalize -> Stemming -> Stopping
    :param text: String, sentence
    :return: Returns preprocessed text as a list
    """
    
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = nltk.word_tokenize(text)
    words = [nltk.LancasterStemmer().stem(word) for word in words]
    words = [word for word in words if word not in stopwords.words('english')]
    
    return words


text = 'BBC News provides trusted World and UK news as well as local and regional perspectives, as well as entertainment, business, science, technology and health news.'
print(preprocess(text))
