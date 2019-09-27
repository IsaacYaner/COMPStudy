#In order to use session in flask you need to set the secret key in your application settings. 
#secret key is a random key used to encrypt your cookies.

from flask import Flask, render_template, request, session, make_response
from server import app,orders
from cart_mgr import Cart, CartManager
from order import Order


def fetch_session_cart():
    # Creates a new cart first if the cart never existed
    if 'cart' not in session:
        print('cart not in session')
        cart = Cart()
        session['cart'] = cart._id
        orders[cart._id] = cart
    else:
        # Check the current cookie is valid
        print('cart in session')
        try:
            return orders[session['cart']]
        except KeyError: 
            print('exception raised: cart not in session')
            cart = Cart()
            session['cart'] = cart._id
            orders[cart._id] = cart
            print(cart._id)
            print("session cookie from ex: " ,session['cart'])
    return orders[session['cart']]


@app.route('/cook')
def say_cookies():
    if not request.cookies.get('food'):
        res = make_response("Setting a cookie")
        res.set_cookie('food', 'bar', max_age=60*60*24*365*2)
    else:
        res = make_response("Value of cookie {} is {}".format('food',request.cookies.get('foo')))
    return res

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # Add to cart
        id = int(request.form['id'])
        qty = int(request.form['qty'])
        cart = fetch_session_cart()
        cart._items.append(Order(id,qty))
        print("no: ", len(cart._items))
        return render_template('home.html', items=cart._items,length=len(cart._items))
    else:
        return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)
 


