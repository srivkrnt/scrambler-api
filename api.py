from flask import Flask
import random

app = Flask(__name__)

noOfWords = 11800
fileName = 'words.txt'

@app.route('/')
def index():
    file = open(fileName)
    words = file.readlines()

    wordIndex = (random.randint(2, noOfWords)//2) * 2
    response = {}
    response['index'] = wordIndex
    response['actual_word'] = words[wordIndex+1]
    response['scrambled_word'] = words[wordIndex]
    response['split_scrambled_word'] = list(''.join(words[wordIndex]).replace(' ','').strip())
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