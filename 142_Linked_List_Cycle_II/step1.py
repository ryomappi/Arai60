# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur_node = head
        visited_nodes = []

        while cur_node and cur_node.next:
            for i in range(len(visited_nodes)):
                if cur_node == visited_nodes[i]:
                    return cur_node
            visited_nodes.append(cur_node)
            cur_node = cur_node.next

        return None
