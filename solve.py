import numpy as np
import queue
import prettytable as pt


class A_star:
    def __init__(self, start_data, end_data):
        self.start_data = start_data
        self.end_data = end_data
        self.opened = queue.Queue()
        self.closed = {}
        self.result_node = None

    def find_zero(self, n):
        tmp_x, tmp_y = np.where(n == 0)
        return tmp_x[0], tmp_y[0]

    def swap(self, num_data, direction):
        x, y = self.find_zero(num_data)
        n = np.copy(num_data)
        if direction == 'left':
            if y == 0:
                return n
            n[x][y] = n[x][y - 1]
            n[x][y - 1] = 0
            return n
        if direction == 'right':
            if y == 2:
                return n
            n[x][y] = n[x][y + 1]
            n[x][y + 1] = 0
            return n
        if direction == 'up':
            if x == 0:
                return n
            n[x][y] = n[x - 1][y]
            n[x - 1][y] = 0
            return n
        if direction == 'down':
            if x == 2:
                return n
            else:
                n[x][y] = n[x + 1][y]
                n[x + 1][y] = 0
                return n

    def cal_wcost(self, n):
        con = 0
        for i in range(3):
            for j in range(3):
                tmp_num = n[i][j]
                compare_num = self.end_data[i][j]
                if tmp_num != 0:
                    con += tmp_num != compare_num
        return con

    def data_to_int(self, n):
        value = 0
        for i in n:
            for j in i:
                value = value * 10 + j
        return value

    def sort_by_floss(self):
        tmp_open = self.opened.queue.copy()
        length = len(tmp_open)
        for i in range(length):
            for j in range(length):
                if tmp_open[i].f_loss < tmp_open[j].f_loss:
                    tmp = tmp_open[i]
                    tmp_open[i] = tmp_open[j]
                    tmp_open[j] = tmp
                if tmp_open[i].f_loss == tmp_open[j].f_loss:
                    if tmp_open[i].step > tmp_open[j].step:
                        tmp = tmp_open[i]
                        tmp_open[i] = tmp_open[j]
                        tmp_open[j] = tmp
        self.opened.queue = tmp_open

    def refresh_open(self, now_node):
        tmp_open = self.opened.queue.copy()
        for i in range(len(tmp_open)):
            data = tmp_open[i]
            now_data = now_node.data
            if (data == now_data).all():
                data_f_loss = tmp_open[i].f_loss
                now_data_f_loss = now_node.f_loss
                if data_f_loss <= now_data_f_loss:
                    return False
                else:
                    tmp_open[i] = now_node
                    self.opened.queue = tmp_open
                    return True
        tmp_open.append(now_node)
        self.opened.queue = tmp_open
        return True

    def method_a_function(self):
        con = 0
        while len(self.opened.queue) != 0:
            node_u = self.opened.get()
            if (node_u.data == self.end_data).all():
                print(f'总共耗费{con}轮')
                self.result_node = node_u
                return
            self.closed[self.data_to_int(node_u.data)] = 1
            for action in ['left', 'right', 'up', 'down']:
                child_node = Node(self.swap(node_u.data, action), node_u.step + 1, node_u, self)
                index = self.data_to_int(child_node.data)
                if index not in self.closed:
                    self.refresh_open(child_node)
            self.sort_by_floss()
            con += 1

    def output_result(self):
        all_node = [self.result_node]
        for i in range(self.result_node.step):
            father_node = self.result_node.parent
            all_node.append(father_node)
            self.result_node = father_node
        return reversed(all_node)

    def solve(self):
        start_node = Node(self.start_data, 0, None, self)
        self.opened.put(start_node)
        self.method_a_function()
        node_list = list(self.output_result())
        tb = pt.PrettyTable()
        tb.field_names = ['step', 'data', 'f_loss']
        for node in node_list:
            num = node.data
            tb.add_row([node.step, num, node.f_loss])
            if node != node_list[-1]:
                tb.add_row(['---', '--------', '---'])
        return tb


class Node:
    f_loss = -1
    step = 0
    parent = None

    def __init__(self, data, step, parent, a_star_instance):
        self.data = data
        self.step = step
        self.parent = parent
        self.f_loss = a_star_instance.cal_wcost(data) + step


start_data = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
end_data = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

a_star = A_star(start_data, end_data)
result_table = a_star.solve()
print(result_table)
