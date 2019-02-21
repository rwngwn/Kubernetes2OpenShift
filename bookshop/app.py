from flask import Flask

import requests


app = Flask(__name__)
BOOKS = ['1984', 'foo', 'bar', "ahoj a"]

@app.route("/")
def hello():
    response = "<H1>Books PrgCont FOOOO:</H1><BR>"
    for book in BOOKS:
        try:
            review = requests.get(f'http://bookreview:8080/v1/review/{book}')
            if review.status_code == 200:
                response += f" {book}: {review.text} <BR>"
            else:
                print(f'Cannot get review for {name}, result {review.status_code}')
                response += f" {book} <BR>"
        except:
            print(f'Cannot contact review service')
            response += f" {book} <BR>"
    return response


app.run(host='0.0.0.0', port=8080)
