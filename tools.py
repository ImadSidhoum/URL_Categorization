from nltk.stem.snowball import SnowballStemmer
from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop
from spacy.lang.en.stop_words import STOP_WORDS as en_stop
import json, re, tldextract, itertools
from urllib.parse import urlparse
from setuptools.namespaces import flatten
import numpy as np
# An example on Stemming
stemmer = SnowballStemmer(language='french')
# Getting the stopwords list
final_stopwords_list = list(fr_stop) + list(en_stop)
# we can extend the stopwords list with some word related to URLs
final_stopwords_list += ['html','htm'] # .... to be added after

class LabelEncoder(object):
    """Label encoder for tag labels."""
    def __init__(self, class_to_index={}):
        self.class_to_index = class_to_index
        self.index_to_class = {v: k for k, v in self.class_to_index.items()}
        self.classes = list(self.class_to_index.keys())
        

    def __len__(self):
        return len(self.class_to_index)

    def __str__(self):
        return f"<LabelEncoder(num_classes={len(self)})>"

    def fit(self, y):
        classes = np.unique(list(itertools.chain.from_iterable(y)))
        for i, class_ in enumerate(classes):
            self.class_to_index[class_] = i
        self.index_to_class = {v: k for k, v in self.class_to_index.items()}
        self.classes = list(self.class_to_index.keys())
        return self

    def encode(self, y):
        y_one_hot = np.zeros((len(y), len(self.class_to_index)), dtype=int)
        for i, item in enumerate(y):
            for class_ in item:
                y_one_hot[i][self.class_to_index[class_]] = 1
        return y_one_hot

    def decode(self, y):
        classes = []
        for i, item in enumerate(y):
            indices = np.where(item == 1)[0]
            classes.append([self.index_to_class[index] for index in indices])
        return classes

    def save(self, fp):
        with open(fp, "w") as fp:
            contents = {"class_to_index": self.class_to_index}
            json.dump(contents, fp, indent=4, sort_keys=False)

    def load(self, fp):
        with open(fp, "r") as fp:
          self.class_to_index = json.load(fp=fp)["class_to_index"]
        self.index_to_class = {v: k for k, v in self.class_to_index.items()}
        self.classes = list(self.class_to_index.keys())
def splitAtUpperCase(s):
  """
    split the word s by uppercase letter
  """
  for i in range(len(s)-1)[::-1]:
      if s[i].isupper() and s[i+1].islower():
          s = s[:i]+' '+s[i:]
      if s[i].isupper() and s[i-1].islower():
          s = s[:i]+' '+s[i:]
  return s.split()

# an example of splitting by uppercase letters
splitAtUpperCase('FastANDFurious')
def removal_condition(token ,stopwords) :
  """
    *Returns a boolean indicate if the token satisfy all the conditions or not*
    Parameters
    ----------
    token : str
        a word.
    stopwords : list of str
        a list of words that we want to remove.

    check_existence:bool 
        a boolean indicate if we want to check if the word exist in the dictionnary or not
    Returns
    -------
    bool
        the token satisfy all the conditions or not.
  """
  cond =  any(c.isdigit() for c in token) or len(token) <=2 or token in stopwords or len(token) >= 20 
  return not(cond)

def preprocess_url (url ,stopwords_list=final_stopwords_list) :
  """
    *Process the url to make it ready to be used by the model*
    Parameters
    ----------
    url : str
        the url of a page.
    stopwords_list : list of str
        a list of words that we want to remove.
    Returns
    -------
    str
        processed url
  """

  # getting the domain name using tldextract library
  domain_name = tldextract.extract(url)[1]
  full_path = urlparse(url).path
  # getting the query if it exists otherwise it's empty
  query = urlparse(url).query
  # split of (path + query )
  splited_tokens = re.split('[- _ % : , / \. \+ = ]', full_path +' '+query)
  tokens = []
  # spliting by digits
  for token in splited_tokens : 
      tokens += re.split('\d+' , token)
  # spliting by uppercase letters
  tokens = list(flatten([splitAtUpperCase(s) for s in tokens]))
  # stemming , lowercasing , stopwords removal , and removing tokens with numbers 
  tokens = [ stemmer.stem(token.lower()) for token in tokens if removal_condition(token.lower() , stopwords_list) ]
  tokens = [token for token in tokens if removal_condition(token , stopwords_list)]
  # return unique elements
  # [domain_name] +
  final_sentence = list(dict.fromkeys([domain_name] + tokens))
  return " ".join(final_sentence)