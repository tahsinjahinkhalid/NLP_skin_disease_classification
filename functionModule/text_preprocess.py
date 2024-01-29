import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def preprocess_text(text):
    """
    Takes a text string input.

    Returns the preprocessed text.

    Involves the following:
    - converts to lower case
    - removes punctuation
    - tokenizes text
    - stop word removal
    - preforms lemmatization
    """
    # convert text to lowercase
    text = text.lower()

    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # tokenize text
    tokens = word_tokenize(text)

    # remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # rerun this step again but add a new word
    tokens = [word for word in tokens if word not in set(
        stopwords.words('english').append('doctor'))]

    # lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return ' '.join(tokens)
