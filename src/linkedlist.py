class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")



def append(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    current = head
    while current.next is not None:
        current = current.next

    current.next = new_node
    return head


def prepend(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def insert_after(head, prev_data, data):
    current = head

    while current is not None:
        if current.data == prev_data:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
            return head
        current = current.next

    print(str(prev_data) + " siyahıda tapılmadı")
    return head


def delete(head, data):
    current = head

    if current is not None and current.data == data:
        return current.next

    prev = None
    while current is not None and current.data != data:
        prev = current
        current = current.next

    if current is None:
        print(str(data) + " elementi siyahıda yoxdur")
        return head

    prev.next = current.next
    return head


def search(head, value):
    current = head
    while current is not None:
        if current.data == value:
            print("Element tapıldı.")
            return True
        current = current.next
    print("Element tapılmadı.")
    return False



def length(head):
    count = 0
    current = head
    while current is not None:
        count = count + 1
        current = current.next
    return count



def find_max(head):
    if head is None:
        return None
    max_value = head.data
    current = head.next
    while current is not None:
        if current.data > max_value:
            max_value = current.data
        current = current.next
    return max_value


def find_min(head):
    if head is None:
        return None
    min_value = head.data
    current = head.next
    while current is not None:
        if current.data < min_value:
            min_value = current.data
        current = current.next
    return min_value



def reverse(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# Testlər
if __name__ == "__main__":

    # Tapşırıq 1
    node = Node(15)
    print("Node data:", node.data)
    print("Node next:", node.next)
    print()

    # Tapşırıq 2
    head1 = Node(10)
    head1.next = Node(20)
    head1.next.next = Node(30)
    head1.next.next.next = Node(40)
    print_list(head1)
    print()

    # Tapşırıq 3
    head2 = Node(20)
    head2.next = Node(30)
    head2.next.next = Node(40)
    head2 = prepend(head2, 10)
    print_list(head2)
    print()

    # Tapşırıq 4
    head3 = Node(10)
    head3.next = Node(20)
    head3.next.next = Node(40)
    head3 = insert_after(head3, 20, 30)
    print_list(head3)
    print()

    # Tapşırıq 5
    head4 = None
    for value in [10, 20, 30, 40, 50]:
        head4 = append(head4, value)
    head4 = delete(head4, 30)
    print_list(head4)
    print()

    # Tapşırıq 6
    head5 = None
    for value in [10, 20, 30]:
        head5 = append(head5, value)
    search(head5, 30)
    search(head5, 99)
    print()

    # Tapşırıq 7
    head6 = None
    for value in [11, 22, 33, 44, 55]:
        head6 = append(head6, value)
    print("List length =", length(head6))
    print()

    # Tapşırıq 8
    head7 = None
    for value in [23, 8, 91, 15, 42]:
        head7 = append(head7, value)
    print("Maximum:", find_max(head7))
    print("Minimum:", find_min(head7))
    print()

    # Tapşırıq 9
    head8 = None
    for value in [10, 20, 30, 40, 50]:
        head8 = append(head8, value)
    print("Evvel:")
    print_list(head8)
    head8 = reverse(head8)
    print("Sonra:")
    print_list(head8)
