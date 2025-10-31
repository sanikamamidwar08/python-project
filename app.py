from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret123'


# ===== Home =====
@app.route('/')
def index():
    return render_template('index.html')


# ===== Menu =====
@app.route('/menu')
def menu():
    dishes = [
        {"name": "Spaghetti Carbonara", "price": 14.50, "is_vegetarian": False, "image": "carbonara.jpg"},
        {"name": "Mushroom Risotto", "price": 12.00, "is_vegetarian": True, "is_special": True, "image": "risotto.jpg"},
        {"name": "Margherita Pizza", "price": 10.00, "is_vegetarian": True, "image": "pizza.jpg"},
        {"name": "Grilled Steak", "price": 22.00, "is_vegetarian": False, "image": "steak.jpg"},
        {"name": "Paneer Tikka Masala", "price": 15.00, "is_vegetarian": True, "image": "paneer.jpg"},
        {"name": "Chicken Biryani", "price": 16.00, "is_vegetarian": False, "is_special": True, "image": "biryani.jpg"},
        {"name": "Veg Manchurian", "price": 11.00, "is_vegetarian": True, "image": "manchurian.jpg"},
        {"name": "Fish Curry", "price": 18.00, "is_vegetarian": False, "image": "fish.jpg"}
    ]
    return render_template('menu.html', menu_items=dishes)


# ===== Contact =====
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash(f"Thank you {name}, we received your message!")
        return redirect(url_for('contact'))
    return render_template('contact.html')


# ===== Order =====
@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form['name']
        dish = request.form['dish']
        quantity = request.form['quantity']
        flash(f"Order received for {quantity} × {dish} by {name}. Thank you!")
        return redirect(url_for('order'))
    return render_template('order.html')


# ===== About =====
@app.route('/about')
def about():
    return render_template('about.html')





# ===== Specials =====
@app.route('/specials')
def specials():
    specials = [
        {"name": "Chef’s Signature Pasta", "price": 20.00, "desc": "Rich creamy sauce with fresh herbs.", "image": "carbonara.jpg"},
        {"name": "Festive Thali", "price": 18.00, "desc": "A perfect blend of Indian delicacies.", "image": "special2.jpg"}
    ]
    return render_template('specials.html', specials=specials)

# ===== Reservations =====
@app.route('/reservations', methods=['GET', 'POST'])
def reservations():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        guests = request.form['guests']
        flash(f"Reservation confirmed for {guests} guests on {date} at {time}. See you soon, {name}!")
        return redirect(url_for('reservations'))
    return render_template('reservations.html')


if __name__ == "__main__":
    app.run(debug=True)
