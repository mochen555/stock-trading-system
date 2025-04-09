from PriorityQueue import MiniPriorityQueue, MaxPriorityQueue
from Trade import Trade
import time
import csv


# order_type=0/1   买/卖
# status= 0/1   未交易/已交易
# status_new='未交易','部分交易','全部交易'
# _type= 0,1,2  股票 0，1，2
class Order:
    def __init__(self, order_id, order_type, quantity, price, _type, owner_id):
        self.order_id = order_id
        self.order_type = order_type
        self.quantity = quantity
        self.status_new = '未交易'
        self.status = 0
        self.price = price
        self.type = _type
        self.time_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.owner = owner_id
        self.actual_price = None

    def get_order_id(self):
        return self.order_id

    def set_order_id(self, order_id):
        self.order_id = order_id
        return self

    # Getter and Setter for order_type
    def get_order_type(self):
        return self.order_type

    def set_order_type(self, order_type):
        self.order_type = order_type
        return self

    # Getter and Setter for quantity
    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        return self

    # Getter and Setter for status
    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
        return self

    # Getter and Setter for price
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
        return self

    # Getter and Setter for type
    def get_type(self):
        return self.type

    def set_type(self, _type):
        self.type = _type
        return self

    # Getter and Setter for owner
    def get_owner(self):
        return self.owner

    def set_actual_price(self, actual_price):
        self.actual_price = actual_price
        return self

    def set_owner(self, owner):
        self.owner = owner
        return self

    def __str__(self):
        return f"""
                order_id:{self.order_id},
                order_type:{self.order_type},
                quantity:{self.quantity},
                status:{self.status},
                price:{round(self.price, 2)},
                type:{self.type},
                time:{self.time_stamp},
                owner:{self.owner}
                actual:{self.actual_price}
                
                    """


class Order_queue:
    def __init__(self):
        self.buy_queue = MaxPriorityQueue()
        self.sell_queue = MiniPriorityQueue()

    def add_order(self, order):
        if order.order_type == 0:
            self.buy_queue.add(order.price, order)
        elif order.order_type == 1:
            self.sell_queue.add(order.price, order)

    def match(self):
        trades = []
        settle_buy_order = []
        settle_sell_order = []
        while not self.buy_queue.isEmpty() and not self.sell_queue.isEmpty():
            buy_order = self.buy_queue.heapArray[1][1]
            sell_order = self.sell_queue.heapArray[1][1]

            if buy_order.get_price() >= sell_order.get_price():
                actual_price = (buy_order.get_price() + sell_order.get_price()) / 2
                if buy_order.get_quantity() >= sell_order.get_quantity():
                    buy_order.status_new = "部分成交"
                    sell_order.status_new = "已成交"
                    remaining_quantity = buy_order.get_quantity() - sell_order.get_quantity()
                    if remaining_quantity > 0:
                        new_buy_order = Order(buy_order.get_order_id() + "*",
                                              buy_order.get_order_type(),
                                              remaining_quantity,
                                              buy_order.get_price(),
                                              buy_order.get_type(),
                                              buy_order.get_owner())
                        new_buy_order.status_new = "部分成交"
                        self.add_order(new_buy_order)
                    settle_buy_order.append(
                        self.buy_queue.delMax().set_status(1).set_actual_price(actual_price).set_quantity(
                            remaining_quantity))
                    settle_sell_order.append(
                        self.sell_queue.delMin().set_status(1).set_actual_price(actual_price).set_quantity(
                            remaining_quantity))
                    trades.append(Trade(buy_order, sell_order, actual_price, buy_order.type, remaining_quantity))
                else:
                    remaining_quantity = sell_order.get_quantity() - buy_order.get_quantity()
                    buy_order.status_new = "已成交"
                    sell_order.status_new = "部分成交"
                    if remaining_quantity > 0:
                        new_sell_order = Order(sell_order.get_order_id() + "*",
                                               sell_order.get_order_type(),
                                               remaining_quantity,
                                               sell_order.get_price(),
                                               sell_order.get_type(),
                                               sell_order.get_owner())
                        new_sell_order.status_new = "部分成交"
                        self.add_order(new_sell_order)
                    settle_buy_order.append(
                        self.buy_queue.delMax().set_status(1).set_actual_price(actual_price).set_quantity(
                            remaining_quantity))
                    settle_sell_order.append(
                        self.sell_queue.delMin().set_status(1).set_actual_price(actual_price).set_quantity(
                            remaining_quantity))
                    trades.append(Trade(buy_order, sell_order, actual_price, buy_order.type, remaining_quantity))
            else:
                break

        return {'trades': trades, 'settle_sell_order': settle_sell_order, 'settle_buy_order': settle_buy_order}

    def cancel_sell_order(self, id):
        for item in self.sell_queue.heapArray:
            if id == item[1].order_id:
                self.sell_queue.heapArray.remove(item)
                self.sell_queue.buildHeap(self.sell_queue.heapArray[1:])
                break

    def cancel_buy_order(self, id):
        for item in self.buy_queue.heapArray[1:]:
            if id == item[1].order_id:
                self.buy_queue.heapArray.remove(item)
                self.buy_queue.buildHeap(self.buy_queue.heapArray[1:])
                break

    def check_first_order(self, order):
        if order == 0:
            return self.buy_queue.heapArray[1]
        elif order == 1:
            return self.sell_queue.heapArray[1]


