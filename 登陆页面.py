import time
from main import Progress
from order import Order
from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import csv

owner = ""
order_id = 1
app = Flask(__name__)
app.secret_key = 'your_secret_key'
progress = Progress()


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        df = pd.read_csv("users.csv", encoding="gbk")
        users = []
        passwords = []
        for row in df.iterrows():
            usernameNew = row[1]['用户名']
            passwordNew = row[1]['用户密码']
            users.append(usernameNew)
            passwords.append(passwordNew)
        if username in users:
            if passwords[users.index(username)] == password:
                global owner
                owner = username
                return redirect(url_for('mainPage'))
            else:
                flash('密码错误！', 'danger')
        else:
            flash('无效用户名或密码！', 'danger')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        df = pd.read_csv("users.csv", encoding="gbk")
        users = []
        for row in df.iterrows():
            usernameOld = row[1]['用户名']
            users.append(usernameOld)
        if username in users:
            flash('用户已经存在了！', 'danger')
        else:
            with open("users.csv", 'a+', encoding='gbk', newline="") as f:
                csv_write = csv.writer(f)
                data_row = [f"{username}", f"{password}"]
                csv_write.writerow(data_row)
            flash('注册成功，您现在可以登录了！', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/mainPage')
def mainPage():
    return render_template('mainPage.html')


@app.route('/page1', methods=['GET', 'POST'])
def page1():
    global owner
    global order_id
    if request.method == 'POST':
        stock_price = request.form['stock_price']
        stock_price = float(stock_price)
        print(stock_price)
        buy_sell = request.form['buy_sell']
        if buy_sell == '买':
            buy_sell = 0
        else:
            buy_sell = 1
        stock_quantity = request.form['stock_quantity']
        stock_quantity = int(stock_quantity)
        stock_type = request.form['stock_type']
        stock_type = int(stock_type)
        order = Order(str(order_id), buy_sell, stock_quantity, stock_price, stock_type, owner)
        progress.to_priority_queue(order)
        order_id += 1
        flash('成功添加订单', 'success')

    return render_template('page1.html')


@app.route('/page2', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        stock_id = request.form['stock_id']
        stock_id = str(stock_id)
        found = False
        if progress.history == []:
            flash('当前无历史订单', 'danger')
            return render_template('page2.html')
        for stock in progress.history:
            if stock.order_id == stock_id:
                found = True
                if stock.type == 0:
                    if stock.order_type == 0:
                        progress.stock_0.cancel_buy_order(stock_id)
                    else:
                        progress.stock_0.cancel_sell_order(stock_id)
                    flash('成功删除订单', 'success')
                    return render_template('page2.html')
                elif stock.type == 1:
                    if stock.order_type == 0:
                        progress.stock_1.cancel_buy_order(stock_id)
                    else:
                        progress.stock_1.cancel_sell_order(stock_id)
                    flash('成功删除订单', 'success')
                    return render_template('page2.html')
                elif stock_id == 2:
                    if stock.order_type == 0:
                        progress.stock_2.cancel_buy_order(stock_id)
                    else:
                        progress.stock_2.cancel_sell_order(stock_id)
                    flash('成功删除订单', 'success')
                    return render_template('page2.html')
        if not found:
            flash('未找到订单', 'danger')

    return render_template('page2.html')


@app.route('/page3')
def page3():
    return render_template('page3.html')


@app.route('/page4')
def page4():
    return render_template('page4.html')


@app.route('/target_page1')
def target_page1():
    orders = []
    for order in progress.history:
        order_id = int(order.order_id)
        if order.order_type == 0:
            order_type = '买'
        else:
            order_type = '卖'
        dictNew = {'order_id': order_id, 'order_type': order_type, 'order_status': order.status_new,
                   'transaction_quantity': order.quantity,
                   'transaction_price': order.price}
        orders.append(dictNew)
    return render_template('target_page1.html', orders=orders)


@app.route('/target_page2')
def target_page2():
    return render_template('target_page2.html')


@app.route('/view_stock/<int:stock_id>')
def view_stock(stock_id):
    stock_orders = {0: [], 1: [], 2: []}
    progress.show_all_order()
    for stock in progress.all_order:
        if stock.type == 0:
            if stock.order_type == 0:
                order_type = '买'
            else:
                order_type = '卖'
            stock_orders[0].append(
                {'order_id': stock.order_id, 'order_type': order_type, 'order_status': stock.status_new,
                 'transaction_quantity': stock.quantity, 'transaction_price': stock.price})
        elif stock.type == 1:
            if stock.order_type == 0:
                order_type = '买'
            else:
                order_type = '卖'
            stock_orders[1].append(
                {'order_id': stock.order_id, 'order_type': order_type, 'order_status': stock.status_new,
                 'transaction_quantity': stock.quantity, 'transaction_price': stock.price})
        elif stock.type == 2:
            if stock.order_type == 0:
                order_type = '买'
            else:
                order_type = '卖'
            stock_orders[2].append(
                {'order_id': stock.order_id, 'order_type': order_type, 'order_status': stock.status_new,
                 'transaction_quantity': stock.quantity, 'transaction_price': stock.price})
    stock_info = stock_orders.get(stock_id, None)
    progress.all_order = []
    if stock_info is None:
        return "Stock not found", 404

    return render_template('view_stock.html', stock_id=stock_id, orders=stock_info)


if __name__ == '__main__':
    app.run()
