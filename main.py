from order import Order, Order_queue
from random import randint, random


class Progress:
    def __init__(self):
        self.stock_0 = Order_queue()
        self.stock_1 = Order_queue()
        self.stock_2 = Order_queue()
        self.trades = []
        self.settled_buy_order = []
        self.settled_sell_order = []
        self.history = []
        self.all_order=[]
        self.all_sell_order = {}
        self.all_buy_order = {}

    def to_priority_queue(self, order):
        result = None
        if int(order.get_type()) == 0:
            self.stock_0.add_order(order)
            result = self.stock_0.match()
        elif int(order.get_type()) == 1:
            self.stock_1.add_order(order)
            result = self.stock_1.match()
        elif int(order.get_type()) == 2:
            self.stock_2.add_order(order)
            result = self.stock_2.match()
        self.history.append(order)
        return result

    def to_trades(self, result):
        if 'trades' in result and result['trades']:
            self.trades.extend(result['trades'])

    def to_buy_order(self, result):
        if 'settle_buy_order' in result and result['settle_buy_order']:
            self.settled_buy_order.extend(result['settle_buy_order'])

    def to_sell_order(self, result):
        if 'settle_sell_order' in result and result['settle_sell_order']:
            self.settled_sell_order.extend(result['settle_sell_order'])

    def show_all_order(self):

        # 检查 stock_0 的订单队列
        self.check_order_queue(self.stock_0)
        # 检查 stock_1 的订单队列
        self.check_order_queue(self.stock_1)
        # 检查 stock_2 的订单队列
        self.check_order_queue(self.stock_2)

    def check_order_queue(self, order_queue):
        for i in order_queue.buy_queue.heapArray[1:]:
            self.all_order.append(i[1])
        for i in order_queue.sell_queue.heapArray[1:]:
            self.all_order.append(i[1])




def random_order(num):
    result = []
    for i in range(num):
        order = Order(
            str(i),
            randint(0, 1),
            randint(1, 99),
            round(4 * random(), 2),
            randint(0, 2),
            randint(0, 100)
        )
        result.append(order)
    return result


if __name__ == '__main__':
    pc = Progress()
    num = 10
    orders = random_order(num)  
    for order in orders:
        result = pc.to_priority_queue(order)
        pc.to_trades(result)
        pc.to_buy_order(result)
        pc.to_sell_order(result)


    print(f"Number of trades: {len(pc.trades)}")
    for trade in pc.trades:
        print(trade)
    for i in range(len(pc.history)):
        print(pc.history[i].status_new)
