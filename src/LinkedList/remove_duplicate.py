"""
To remove duplicates from an unsorted linked list, we can use a hash table to keep track of the values we have already seen. The algorithm would look something like this:

Create an empty hash table.
Initialize two pointers: current and previous. Set current to the head of the linked list and previous to None.
Traverse the linked list, one node at a time.
For each node, check if its value is already in the hash table. If it is, remove the node by updating the previous node's next pointer to skip over the current node. Otherwise, add the value to the hash table.
If the current node is removed, move the current pointer to the next node without updating the previous pointer. If the current node is not removed, move both pointers to the next node.
Repeat steps 4-5 until the end of the linked list is reached.
Here's an arrow diagram showing the steps of this algorithm:

   +----+     +----+     +----+     +----+     +----+     +----+
   |    |     |    |     |    |     |    |     |    |     |    |
   |    |     |    |     |    |     |    |     |    |     |    |
   |  2 |---->|  1 |---->|  3 |---->|  2 |---->|  4 |---->|  3 |
   |    |     |    |     |    |     |    |     |    |     |    |
   |    |     |    |     |    |     |    |     |    |     |    |
   +----+     +----+     +----+     +----+     +----+     +----+

   +----+     +----+     +----+           +----+     +----+
   |    |     |    |     |    |           |    |     |    |
   |    |     |    |     |    |           |    |     |    |
   |  2 |---->|  1 |---->|  3 |---------> |  4 |---->|None|
   |    |     |    |     |    |           |    |     |    |
   |    |     |    |     |    |           |    |     |    |
   +----+     +----+     +----+           +----+     +----+

In this example, we start with an unsorted linked list containing four nodes with values 2, 1, 3, and 2. After running the algorithm, we end up with a new linked list containing only unique values, in the same order: 2, 1, 3, and 4. The duplicates (the two nodes with value 2) have been removed.

"""

from main import LinkedList


def remove_duplicate(head_pointer):
    cur_node = head_pointer
    dataMap = set()

    while cur_node.next:
        data = cur_node.data
        if data in dataMap:
            cur_node.next = cur_node.next.next
            continue
        dataMap.add(data)
        cur_node = cur_node.next
    return head_pointer


if __name__ == '__main__':
    cur_list = LinkedList()
    elements = [2, 1, 3, 2, 4, 3]

    for element in elements:
        cur_list.add_to_end_of_list(element)

    head = cur_list.head
    cur_list.show_list(head)
    print()
    head = remove_duplicate(head)
    cur_list.show_list(head)
