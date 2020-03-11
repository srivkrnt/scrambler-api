from flask import Flask
import random

app = Flask(__name__)

fileName = 'words.txt'
easyWordFile = 'easy_words.txt'


@app.route('/')
def index():
    file = open(fileName)
    words = file.readlines()
    noOfWords = len(words)
    wordIndex = (random.randint(2, noOfWords)//2) * 2
    response = {}
    response['index'] = wordIndex
    response['actual_word'] = words[wordIndex+1]
    response['scrambled_word'] = words[wordIndex]
    response['split_scrambled_word'] = list(''.join(words[wordIndex]).replace(' ','').strip())
    response['noOfWords'] = noOfWords
    return response

@app.route('/all')
def easy_words():
    file = open(easyWordFile)
    words = file.readlines()
    noOfWords = len(words)
    wordIndex = (random.randint(2, noOfWords//2) * 2)
    word = words[wordIndex].strip()
    response = {}
    response['index'] = wordIndex
    response['actual_word'] = word
    word = list(word)
    random.shuffle(word)
    response['split_scrambled_word'] = word
    response['scrambled_word'] = ' '.join(word)
    return response

@app.route('/scramble/<word>')
def scramble(word):
    response = {}
    response['actual_word'] = word
    word = list(word)
    random.shuffle(word)
    response['split_scrambled_word'] = word
    response['scrambled_word'] = ' '.join(word)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')