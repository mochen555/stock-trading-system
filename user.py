from order_queue import order_queue
class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password

    def order_buy_queue_show(self):
        buy_orders = order_queue.display_buy_order(self.user_id)
        print(f"用户{self.name}的买单队列：")
        for order in buy_orders:
            print(f"id:{order['order_id']},类型:{order['type']},价格:{order['price']},"
                  f"数量:{order['quantity']},时间:{order['time_stamp']}")

    def order_sell_queue_show(self):
        sell_orders = order_queue.display_sell_order(self.user_id)
        print(f"用户{self.name}的卖单队列：")
        for order in sell_orders:
            print(f"id:{order['order_id']},类型:{order['type']},价格:{order['price']},"
                  f"数量:{order['quantity']},时间:{order['time_stamp']}")
