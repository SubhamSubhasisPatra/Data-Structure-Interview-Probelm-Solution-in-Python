"""

 [data , pointter] -> [data , pointer] -> None

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end_of_list(self, data):
        """
        :keyword data : the data to be stored in the list
        """

        # create a node
        # assign the node
        # While assigning check if the there a linked list is there or not
        # if we have assign to it's next else assing to the begining

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        # take the head
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = new_node

    def show_list(self):
        cur_node = self.head
        while cur_node:
            print(f"{cur_node.data}", end='->')
            cur_node = cur_node.next


ll_obj = LinkedList()
ll_obj.add_to_end_of_list(1)
ll_obj.add_to_end_of_list(2)
ll_obj.add_to_end_of_list(3)
ll_obj.show_list()
