class Solution:

    def build(self, preorder: List[int], inorder: List[int], pre_s, pre_e, in_s, in_e) -> TreeNode:
        if pre_s == pre_e:
            return None
        root_node = TreeNode(preorder[pre_s])

        root_idx = inorder.index(root_val)

        l_len = root_idx - in_s
        r_len = in_e - root_idx

        l_pre_s = pre_s + 1
        l_pre_e = pre_s + 1 + l_len

        r_pre_s = pre_s + 1 + l_len
        r_pre_e = pre_e

        l_in_s = in_s
        l_in_e = root_idx

        r_in_s = root_idx + 1
        r_in_e = in_e

        root_node.left  = self.buildTree(l_pre_s, l_pre_e, l_in_s, l_in_e)
        root_node.right = self.buildTree(r_pre_s, r_pre_e, r_in_s, r_in_e)

        return root_node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, inorder, 0, len(), 0, len())

