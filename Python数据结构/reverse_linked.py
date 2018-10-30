# 反转链表

class Node:
    #节点初始化
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node=None):
        self.head_node = node

    def traversal_linked(self):
        # 便利链表
        tag_node = self.head_node
        while tag_node is not None:
            print (tag_node.data)
            tag_node = tag_node.next

    def reverse_linked(self):
        # 反转链表
        tag_node = self.head_node
        tag_pre_node = None
        tag_next_node = None

        while tag_node is not None:
            tag_next_node = tag_node.next

            if tag_next_node is None:
                self.head_node = tag_node

            tag_node.next = tag_pre_node

            tag_pre_node = tag_node
            tag_node = tag_next_node




node_1 = Node("ma")
node_2 = Node("zhen")
node_3 = Node("l")
node_4 = Node("ccc")
node_1.next = node_2
node_2.next = node_3

link = LinkedList(node_1)
link.traversal_linked()
link.reverse_linked()
link.traversal_linked()
