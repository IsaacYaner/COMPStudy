from flask import render_template, request, redirect, url_for, session, jsonify, abort
from server import app, warehouse, order_manager
from lib.products import ALL_ITEMS, CATEGORIES, CLOTHING, CAMPING
from lib.order import Order, InvalidQuantityError

def fetch_session_cart():
    # Creates a new cart first if the cart never existed
    if 'cart' not in session:
        session['cart'] = order_manager.create_new_order()
    else:
        # Check the current cookie is valid
        try:
            order_manager.get_order(session['cart'])
        except IndexError:
            session['cart'] = order_manager.create_new_order()
    return order_manager.get_order(session['cart'])


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/admin/add_product')
def add_product():
    return render_template('add_product.html', choices=ALL_ITEMS.keys())


@app.route('/create_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        # User wants to create the product
        category = request.form['category']

        args = request.form.to_dict()
        del args['category']  # We don't need to keep track of the category to build it
        builder = ALL_ITEMS[category]
        item = builder(**args)
        warehouse.add_item(item)
    else:
        # Choose a category
        category = request.args.get('category', 'Accessories')

    return render_template('create_product.html', category=category, clothing=CLOTHING, camping=CAMPING)


@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    errors= []
    if request.method == 'POST':
        # Purchase from the search screen
        id = int(request.form['id'])
        qty = int(request.form['qty'])
        try:
            cart = fetch_session_cart()
            cart.add_to_order(id, qty)
        except InvalidQuantityError as e:
            errors.append(str(e))

    if request.args.get('search_str') is not None:
        search_string = request.args['search_str']
        # Search
        select = request.args.get('select', 'all_btn')
        if select == 'cat_btn':
            results = warehouse.search_cat(request.args.get('cat', ''), search_string)
        elif select == 'sub_btn':
            results = warehouse.search_subcat(request.args.get('sub', ''), search_string)
        else:
            results = warehouse.search_all(search_string)

    return render_template('search.html', results=results,
                           choices=[''] + list(CATEGORIES.keys()),
                           sub_choices=[''] + list(ALL_ITEMS.keys()),
                           errors=errors)


@app.route('/shop', methods=['GET', 'POST'])
def shop():
    errors = []
    if request.method == 'POST':
        # Add to cart
        id = int(request.form['id'])
        qty = int(request.form['qty'])
        try:
            cart = fetch_session_cart()
            cart.add_to_order(id, qty)
        except InvalidQuantityError as e:
            errors.append(str(e))

    return render_template('shop.html', items=warehouse.get_all_items(), hidden_traits=['_item_code'], errors=errors)


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    notices = []
    if request.method == 'POST':
        cart = fetch_session_cart()
        if request.form['action'] == 'purchase':
            # Purchase entire cart
            cart.purchase_order(warehouse)
            notices.append(f'Your order ID is {session["cart"]}. You can view your order at {url_for("order", id=session["cart"])}')
            session.pop('cart')  # Deletes the cart ID, the new cart ID will be created when necessary
        elif request.form['action'] == 'update':
            # Update item qty
            try:
                cart.update(int(request.form['id']), int(request.form['qty']))
            except InvalidQuantityError as e:
                notices.append(str(e))
        elif request.form['action'] == 'remove':
            # Remove the item from the cart
            cart.remove(int(request.form['id']))

    return render_template('checkout.html',
                           table=fetch_session_cart().tabulate_order(warehouse),
                           notices=notices)


@app.route('/order/<int:id>')
def order(id):
    try:
        order = order_manager.get_order(id)
        if not order.purchased:
            raise ValueError('Order is not completed to be shown here')
    except (IndexError, ValueError):
        abort(404)
    return render_template('view_order.html',
                           table=order.tabulate_order(warehouse),
                           errors=[])

@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404