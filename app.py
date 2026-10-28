from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about/<speaker_name>')
def about(speaker_name):
    return render_template('about.html', speaker=speaker_name)
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        ticket_type = request.form.get('ticket')
        if not name or not email or '@' not in email:
            return render_template('register.html', error="Ошибка: Заполните имя и введите корректный email (с @).")
        prices = {'basic': 1500, 'pro': 3500, 'vip': 7000}
        final_price = prices.get(ticket_type, 0)
        return render_template('success.html',
                               name=name,
                               email=email,
                               ticket=ticket_type,
                               price=final_price)
    return render_template('register.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)
