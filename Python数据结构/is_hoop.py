# 判断链表是否存在环

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self, node=None):
        self.head_node = node

    def is_hoop(self):
        if self.head_node is None:
            return None

        p_slow = self.head_node
        p_fast = p_slow.next

        while p_slow != None and p_fast != None:
            if p_slow is p_fast:
                return True

            p_slow = p_slow.next
            p_fast = p_fast.next
            if p_fast is not None:
                p_fast = p_fast.next

        return None

node_1 = Node("ma")
node_2 = Node("zhen")
node_3 = Node("hao")

node_1.next = node_2
node_2.next = node_3
#node_3.next = node_2

l = LinkedList(node_1)
print(l.is_hoop())
