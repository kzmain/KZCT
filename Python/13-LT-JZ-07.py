class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root_val = preorder[0]
        root_nde = TreeNode(root_val)
        root_idx = inorder.index(root_val)

        l_pr = preorder[1:root_idx + 1]
        l_in = inorder[0:root_idx]

        r_pr = preorder[root_idx + 1:]
        r_in = inorder[root_idx + 1:]
        root_nde.left = self.buildTree(l_pr, l_in)
        root_nde.right = self.buildTree(r_pr, r_in)

        return root_nde