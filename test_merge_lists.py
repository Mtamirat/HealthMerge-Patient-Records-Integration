from merge_lists import ListNode, merge_sorted_lists, linked_list_to_array


def create_list(values):
    if not values:
        return None

    head = ListNode(values[0], 30, "Patient")
    current = head

    for value in values[1:]:
        current.next = ListNode(value, 30, "Patient")
        current = current.next

    return head


# Normal Case 1
def test_merge_normal():
    l1 = create_list([111, 333, 555])
    l2 = create_list([222, 444, 666])

    merged = merge_sorted_lists(l1, l2)

    assert linked_list_to_array(merged) == [111,222,333,444,555,666]


# Normal Case 2
def test_merge_different_sizes():
    l1 = create_list([100,200])
    l2 = create_list([150,250,350,450])

    merged = merge_sorted_lists(l1,l2)

    assert linked_list_to_array(merged) == [100,150,200,250,350,450]


# Normal Case 3
def test_duplicates():
    l1 = create_list([100,200,300])
    l2 = create_list([200,300,400])

    merged = merge_sorted_lists(l1,l2)

    assert linked_list_to_array(merged) == [100,200,200,300,300,400]


# Edge Case 1
def test_both_empty():
    merged = merge_sorted_lists(None,None)

    assert merged is None


# Edge Case 2
def test_first_empty():
    l2 = create_list([100,200])

    merged = merge_sorted_lists(None,l2)

    assert linked_list_to_array(merged) == [100,200]


# Edge Case 3
def test_second_empty():
    l1 = create_list([100,200])

    merged = merge_sorted_lists(l1,None)

    assert linked_list_to_array(merged) == [100,200]