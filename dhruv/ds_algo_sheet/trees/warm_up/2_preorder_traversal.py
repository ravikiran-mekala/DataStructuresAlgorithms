import os
import importlib.util

_base_dir = os.path.dirname(__file__)
_file_path = os.path.join(_base_dir, "1_binary_tree_node.py")

_spec = importlib.util.spec_from_file_location("tree_node_mod", _file_path)
_tree_node_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_tree_node_mod)


def preorder_traversal(root):
    if not root:
        return

    print(root.val)
    preorder_traversal(root.left)
    preorder_traversal(root.right)
