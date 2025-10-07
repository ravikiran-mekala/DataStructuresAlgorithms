def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)