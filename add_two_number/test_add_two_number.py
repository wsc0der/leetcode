import unittest
from add_two_number import ListNode, Solution


def make_list(nodes):
    first_node = last_node = None
    for i in range(len(nodes)):
        new_node = ListNode(nodes[i])
        if first_node is None:
            first_node = last_node = new_node
        else:
            last_node.next = new_node
            last_node = new_node

    return first_node


def are_equal_lists(l1, l2):
    if l1 == l2:
        return True
    while l1 is not None and l2 is not None:
        if l1.val != l2.val:
            return False
        else:
            l1 = l1.next
            l2 = l2.next
    return l1 is None and l2 is None



class TestSolution(unittest.TestCase):
    def test_case1(self):
        param_list = (([2,4,3], [5,6,4], [7,0,8]),
                      ([0], [0], [0]),
                      ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]))

        s = Solution()
        for l1, l2, l3 in param_list:
            with self.subTest():
                input1 = make_list(l1)
                input2 = make_list(l2)
                answer = make_list(l3)

                r = s.addTwoNumbers(input1, input2)
                self.assertTrue(are_equal_lists(answer, r))
