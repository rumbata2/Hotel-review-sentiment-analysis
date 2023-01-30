import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

NON_ENGLISH_SYMBOLS = "À|Á|Â|Ã|Ä|Å|Æ|Ç|È|É|Ê|Ë|Ì|Í|Î|Ï|Ð|Ñ|Ò|Ó|Ô|Õ|Ö|×|Ø|Ù|Ú|Û|Ü|Ý|Þ|ß|à|á|â|ã|ä|å|æ|ç|è|é|ê|ë|ì|í|î|ï|ð|ñ|ò|ó|ô|õ|ö|÷|ø|ù|ú|û|ü|ý|þ|ÿ"

SPANISH_KEYWORDS = " ante | bajo | cabe | con | contra | de | desde | durante | en | hacia | hasta | mediante | para | por | sobre | tras | ver | y | pero | o | ni | que | todavia | aun "
ITALIAN_KEYWORDS = " di | da | con | su | tra | fra | anche | inoltre | nemmeno | neanche | neppure | se | poiche | siccome | visto "
FRENCH_KEYWORDS = " alors | que | comme | donc | ensuite | et | lorsque | mais | ni | ou | bien | puis | si | chez | je | de | sur | dans | devant | le | la "
GERMAN_KEYWORDS = " der | das | dem | des | bis | durch | entlang | fuer | gegen | ohne | um | und | oder | bzw | bzw. | beziehungsweise | denn | aber | sondern | allein | doch | jedoch "
PORTUGUESE_KEYWORDS = " e | ou | mas | porque | quando | se | de | antes | acima | perante | apos | depois | como | diante | perante | em | sobre | perto | para | por "

KEYWORDS_BY_LANGUAGE = [SPANISH_KEYWORDS,
                        ITALIAN_KEYWORDS,
                        FRENCH_KEYWORDS,
                        GERMAN_KEYWORDS,
                        PORTUGUESE_KEYWORDS]

def in_english(review_text):
    """
    Returns True if a review (string) is written in english, False otherwise
    """
    
    if re.search(NON_ENGLISH_SYMBOLS, review_text):
        return False

    for lang in KEYWORDS_BY_LANGUAGE:
        if re.search(lang, review_text):
            return False

    return True
    
def clean_text(text):
    """
    Processes a single review text to a point where we can extract features from it
    """

    text = text.lower()
    text = re.sub(r'[%.,?0-9\"\'!\-\(\):]', '', text)
    text = re.sub(r' st | nd | rd | th ', ' ', text)
    text = re.sub(r' \| ', ' ', text)
    
    text = text.split()
    text = [word for word in text if word not in stopwords.words("english")]

    lemmatizer = WordNetLemmatizer()
    text = list(map(lemmatizer.lemmatize, text))

    return text

def split_matrix_data(X, y, delim_pct):
    """
    X: (n, m) matrix
    y: array of size n

    Splits the data into a training set and a validation set
    """

    length = len(X)
    delim_length = int(delim_pct * length)

    X_train = X[: delim_length]
    y_train = y[: delim_length]
    X_test = X[delim_length :]
    y_test = y[delim_length :]

    return X_train, y_train, X_test, y_test

