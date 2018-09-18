
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node=None):
        self.head_node = node

    def traversal_linked(self):
        # 遍历链表, 这里可以加入一些逻辑
        now_node = self.head_node
        while now_node is not None:
            print (now_node.data)
            now_node = now_node.next

    def seek_node(self, data=None):
        #根据节点data查找节点
        tag_node = self.head_node
        while(tag_node):
            if tag_node.data == data:
                return tag_node
            tag_node = tag_node.next

    def insert_begin(self, new_data):
        # 头节点前插入节点
        new_node = Node(new_data)
        new_node.next = self.head_node
        self.head_node = new_node

    def insert_end(self, new_data):
        # 头节点后插入节点
        new_node = Node(new_data)
        if self.head_node is None:
            self.head_node = new_node
            return
        tag_node = self.head_node
        while(tag_node.next):
            tag_node = tag_node.next
        tag_node.next = new_node

    def insert(self, s_node, data=None):
        # 在指定节点后插入节点
        if data == None:
            return
        new_node = Node(data)
        new_node.next = s_node.next
        s_node.next = new_node

    def remove_node(self, data=None):
        #删除相应的节点
        head_node = self.head_node
        # 判断头节点
        if head_node is None or data is None:
            return

        if head_node.data == data:
            self.head_node = head_node.next
            head = None
            return

        tag_node = head_node
        while(tag_node):
            if tag_node.data == data:
                pre_node.next = tag_node.next
                tag_node = None
                break
            # 记录前一个节点
            pre_node = tag_node
            tag_node = tag_node.next


head = Node("ma")
link = LinkedList(head)
link.insert_begin("xiao")
link.insert_end("zhen")
node = link.seek_node("ma")
link.insert(node, "test")
link.remove_node("zhen")
link.traversal_linked()

