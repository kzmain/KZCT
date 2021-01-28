class Solution:
    rst = []
    max = 0

    def recursive(self, node: ListNode, curr_pivot):
        try:
            self.recursive(node.next, curr_pivot + 1)
            self.rst[self.max - curr_pivot] = node.val
        except Exception:
            self.rst = [0] * curr_pivot
            self.max = curr_pivot - 1
            return

    def reversePrint(self, head: ListNode) -> List[int]:
        self.recursive(head, 0)
        return self.rst