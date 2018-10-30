# 查找倒数第k个节点
# 剑指offer 22

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node=None):
        self.head_node = node

    def insert_tail(self, new_node):
        if self.head_node == None:
            self.head_node = new_node
            return
        tag_node = self.head_node
        while tag_node.next:
            tag_node = tag_node.next
        tag_node.next = new_node

    def __len__(self):
        # 返回链表的长度
        len = 0
        tag_node = self.head_node
        while tag_node:
            tag_node = tag_node.next
            len = len + 1
        return len

    def find_tail_k(self, tail_k:int):
        # 返回倒数第k个元素
        #begin_pos = len(self) - tail_k + 1 #上边这种也可以
        begin_pos = self.__len__() - tail_k + 1
        if self.head_node == None or begin_pos <= 0 or tail_k <= 0:
            return None

        tag_node = self.head_node
        while True:
            begin_pos = begin_pos - 1
            if not begin_pos:
                return tag_node
            tag_node = tag_node.next

node_1 = Node("ma")
node_2 = Node("zhen")
node_3 = Node("shi")

l1 = LinkedList(node_1)
l1.insert_tail(node_2)
l1.insert_tail(node_3)
print (len(l1))
print (l1.find_tail_k(2).data)

