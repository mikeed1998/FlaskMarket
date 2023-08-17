from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')             # decorator
@app.route('/home')         
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():

    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '214090827', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '214090828', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '214090829', 'price': 150}
    ]

    return render_template('market.html', items=items)


if __name__ == "__main__": 
    app.run(debug=True)


