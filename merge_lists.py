class ListNode:
    def __init__(self, ssn, age, full_name):
        self.ssn = ssn
        self.age = age
        self.full_name = full_name
        self.next = None


def merge_sorted_lists(list1, list2):
    dummy = ListNode(0, 0, "")
    current = dummy

    while list1 and list2:
        if list1.ssn <= list2.ssn:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1

    if list2:
        current.next = list2

    return dummy.next


def linked_list_to_array(head):
    result = []

    while head:
        result.append(head.ssn)
        head = head.next

    return result