class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        tmp_list = []
        while head:
            tmp_list.append(head.val)
            head = head.next
        return tmp_list[::-1]