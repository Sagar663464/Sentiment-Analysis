from flask import Flask, redirect, url_for, render_template, request
import pickle
from nltk.corpus import stopwords
from nltk import pos_tag, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import regex as re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob, classifiers


app = Flask(__name__)

STOPWORDS = set(stopwords.words('english'))   
def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word not in STOPWORDS])


pattern = '''[-_.,;:'"\/=&@*)(}{?]'''
def remove_punct(text):
    return ' '.join([word for word in text.split() if word in re.sub(pattern=pattern, string=text, repl='')])


lem = WordNetLemmatizer()
def lemmat(text):
    return ' '.join([lem.lemmatize(x) for x in text.split()])


bow = CountVectorizer(stop_words='english', max_features=1000)


@app.route('/')
def welcome_page():

    return render_template('index.html')



@app.route('/coll', methods=['POST', 'GET'])
def collect():
    if request.method == 'POST':

        inp = request.form['txt']
        inp_al = remove_stopwords(inp)
        inp_al = remove_punct(inp_al)
        proc_txt = lemmat(inp_al).lower()

        txt = open('pkl/text_lst.pkl', 'rb')
        text_lst = pickle.load(txt)

        nb = classifiers.NaiveBayesClassifier(text_lst[::20])
        blob = TextBlob(proc_txt, classifier=nb)
        polarity = blob.classify()

        if polarity == 'pos':
            res = 'The text is Positive🙂'
        elif polarity == 'neg':
            res = 'The text is Negative☹️'
        else:
            res = 'The text is Neutral😐'

        return render_template('index.html', text=res, input_txt = inp)



if __name__ == '__main__':
    app.run(debug=True)