def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_ht = self.maxDepth(root.left)
            right_ht = self.maxDepth(root.right)
            return max(left_ht, right_ht) + 1
def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = []
        if root is not None:
            queue.append((1, root))
        depth = 0
        while queue:
            cur_depth, node = queue.pop()
            if node is not None:
                depth = max(depth, cur_depth)
                queue.append((cur_depth+1, node.left))
                queue.append((cur_depth+1, node.right))
        return depth