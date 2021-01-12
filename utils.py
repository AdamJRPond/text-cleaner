import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def clean_text(text):
    # Tokenize and convert to lower case
    tokens = word_tokenize(text)
    tokens = [w.lower() for w in tokens]
    # Remove punctuation and non-alphabetic characters
    table = str.maketrans('', '', string.punctuation)
    filtered = [w.translate(table) for w in tokens if w.isalpha()]
    filtered = [w for w in filtered if w.isalpha()]
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in filtered if not w in stop_words]

    return filtered
