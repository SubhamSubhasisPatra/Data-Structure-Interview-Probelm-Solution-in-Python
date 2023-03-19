from main import LinkedList


def reverse_recursion(head):
    if head is None or head.next is None:
        return
    new_node = reverse_recursion(head.next)
    head.next.next = head
    head.next = None
    return new_node


def reverse_list_recursion(head):
    new_node = None
    while head is not None:
        next_node = head.next
        head.next = new_node
        new_node = head
        head = next_node
    return new_node


def reverse_list(head):
    cur = head
    prev = None
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    head = prev
    return head


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]

    list_object = LinkedList()
    for element in data:
        list_object.add_to_end_of_list(element)

    print(f"Before reverse : {list_object.show_list(list_object.head)}")
    new_head = reverse_list_recursion(list_object.head)
    # print(f"After reverse : {list_object.show_list(new_head)}")