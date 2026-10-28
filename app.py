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
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        ticket_type = request.form.get('ticket')

        # Улучшенная валидация
        errors = []
        if not name or len(name) < 2:
            errors.append("Имя должно содержать минимум 2 символа")
        if not email or '@' not in email or '.' not in email.split('@')[-1]:
            errors.append("Введите корректный email (например, name@example.com)")
        if ticket_type not in ('basic', 'pro', 'vip'):
            errors.append("Выберите тип билета")

        if errors:
            return render_template('register.html', errors=errors,
                                 name=name, email=email, ticket=ticket_type)

        prices = {'basic': 1500, 'pro': 3500, 'vip': 7000}
        final_price = prices.get(ticket_type, 0)

        return render_template('success.html',
                               name=name, email=email,
                               ticket=ticket_type, price=final_price)

    return render_template('register.html', errors=None)

if __name__ == '__main__':
    app.run(debug=True)