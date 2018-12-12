## 从中序遍历以及前序（后序）遍历中还原树

### 思路，通过前后序遍历找到头节点。然后分割中序遍历递归

#### 看起来很棒的代码
```python
class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 如果没有这个子树直接return None
        if not inorder:
            return None
        
        # 找到头节点
        temp = postorder.pop(-1)
        
        # 找到头节点在中序中的问题
        index = inorder.index(temp)
        root = TreeNode(temp)
        
        # 后序遍历先弹出来的是右子树的根
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        
        return root
```

#### 我的很折腾的代码, 起始就是中序遍历的分割没有想清楚，并且还是想通过函数内部新建节点并且添加，没有想到return树节点添加，就很麻烦
```python
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        self.dfs(preorder, inorder, root)
        return root
        
        
    def dfs(self, preorder, inorder, root):
        if len(preorder) == 0:
            return
            
        root_index = inorder.index(root.val)
        
        left_inorder = inorder[:root_index]
        left_preorder = preorder[1:1+len(left_inorder)]
        if len(left_preorder) > 0:
            node = TreeNode(left_preorder[0])
            root.left = node
            self.dfs(left_preorder, left_inorder, root.left)
        
        
        right_inorder = inorder[root_index+1:]
        right_preorder = preorder[1+len(left_inorder):]
        if len(right_preorder) > 0:
            node = TreeNode(right_preorder[0])
            root.right = node
            self.dfs(right_preorder, right_inorder, root.right)
```
