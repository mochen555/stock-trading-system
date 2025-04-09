import time
import csv
class Trade:
    trade_counter = 0

    def __init__(self, order_buy, order_sell, price, _type, quantity):
        self.trade_id = self.generate_trade_id()
        self.trade_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.buyer_id = order_buy.get_order_id()
        self.seller_id = order_sell.get_order_id()
        self.price = price
        self.type = _type
        self.quantity = quantity

    def generate_trade_id(self):
        Trade.trade_counter += 1
        return f"TRADE_{Trade.trade_counter}"

    def get_trade_id(self):
        return self.trade_id

    def get_trade_time(self):
        return self.trade_time

    def get_buyer_id(self):
        return self.buyer_id

    def get_seller_id(self):
        return self.seller_id

    def __str__(self):
        return (f"Trade ID: {self.trade_id}\n"
                f"Trade Time: {self.trade_time}\n"
                f"Buyer ID: {self.buyer_id}\n"
                f"Seller ID: {self.seller_id}\n"
                f"Price: {self.price}\n"
                f"Type: {self.type}\n"
                f"Quantity: {self.quantity}")