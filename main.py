from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return '''
                <h1>To jest moja strona</h1>
                <img src='https://media.giphy.com/media/3o7TKz9bX9v6hZ8ZIY/giphy.gif' alt='GIF'>
                <h2> <a href='/password/10'> Kliknij tutaj, aby zobaczyć hasło </a> </h2>
                <h2> <a href='/second'> Kliknij tutaj, aby zobaczyć losowy dzień tygodnia </a> </h2>
                '''

@app.route('/second')
def second():
    lista = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']

    return f'''<h1> {random.choice(lista)} </h1>
                <h2> <a href='/'> Kliknij tutaj, aby zobaczyć stronę główną </a> </h2>
                <h2> <a href='/password/10'> Kliknij tutaj, aby zobaczyć hasło </a> </h2>
                '''

@app.route('/password/<int:size>')
def password(size):
    symbols = 'abcdefghijklmnouprstwyz'
    haslo = ''
    for i in range(size):
        haslo += random.choice(symbols)

    return f'''<h1> {haslo} </h1>
                <h2> <a href='/'> Kliknij tutaj, aby zobaczyć stronę główną </a> </h2>
                <h2> <a href='/second'> Kliknij tutaj, aby zobaczyć losowy dzień tygodnia </a> </h2>
                '''

@app.route('/slownik')
def slownik():
    slownik = {
        'red' : 'czerwony',
        'blue' : 'niebieski',
        'green' : 'zielony',
        'yellow' : 'żółty'
    }
    return f'''<ul>
                <li> {'red'} : {slownik['red']} </li>
                <li> {'blue'} : {slownik['blue']}</li>
                <li> {'green'}: {slownik['green']}</li>
                <li> {'yellow'} : {slownik['yellow']}</li>
                </ul>
                
                '''

@app.route('/students')
def students():
    studenty = {
        'Jan' : 'Kowalski',
        'Anna' : 'Nowak',
        'Piotr' : 'Kowalski',
        'Ewa' : 'Nowak'
    }
    return render_template('index.html', studenty=studenty)


app.run(debug=True)
