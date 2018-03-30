"""
>>> t = AVLTree()
>>> t.append(50); t.root.value
50
>>> t.append(40); t.root.value, t.root.left.value, t.to_list()
(50, 40, [40, 50])
>>> t.append(30); t.root.value, t.root.left.value, t.root.right.value, t.to_list()
(40, 30, 50, [30, 40, 50])
>>> t.append(20); t.root.value, t.root.left.value, t.root.right.value, t.to_list()
(40, 30, 50, [20, 30, 40, 50])
>>> t.append(10); t.root.value, t.root.left.value, t.root.right.value, t.to_list()
(40, 20, 50, [10, 20, 30, 40, 50])
>>> 20 in t
True
>>> 21 in t
False
>>> #t.append(9); t.root.value, t.root.left.value, t.root.right.value, t.to_list()
(20, 10, 40, [9, 10, 20, 30, 40, 50])
>>> #t.remove(9)
>>> t.append(29); t.root.value, t.root.left.value, t.root.right.value, t.to_list()
(30, 20, 40, [10, 20, 29, 30, 40, 50])
>>> #t.to_list()
[9, 10, 20, 29, 30, 40, 50]
"""
import enum

class Rotation(enum.Enum):
    LEFT = 0
    RIGHT = 1


class AVLTree:

    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def append(self, value):
        new_node = Node(value)
        if self._root is None:
            self._root = new_node
        else:
            self._root = self._append_node(self._root, new_node)

    def _append_node(self, parent, node):

        if node.value < parent.value:
            if parent._left is None:
                parent._left = node
            else:
                parent._left = self._append_node(parent._left, node)
                parent.update_balance()
        else:
            if parent._right is None:
                parent._right = node
            else:
                parent._right = self._append_node(parent._right, node)
                parent.update_balance()

        if parent.balance <= -2 or 2 <= parent.balance:  # Need to rotate
            parent = self._rotate(parent)

        parent.update_balance()
        return parent

    def _rotate(self, subroot):
        if 0 < subroot.balance:
            if 0 < subroot._left.balance: # single left rotation
                subroot = self._left_rotation(subroot)
            elif subroot._left.balance < 0:  # double right rotation
                subroot._left = self._right_rotation(subroot._left)
                subroot = self._left_rotation(subroot)
        else:
            if subroot._right.balance < 0: # single right rotation
                subroot = self._right_rotation(subroot)
            elif 0 < subroot._right.balance:  # double left rotation
                subroot._right = self._left_rotation(subroot._right)
                subroot = self._right_rotation(subroot)
        return subroot

    def _left_rotation(self, node):
        pivot = node._left
        assert pivot is not None, "Node : {}".format(node.value)
        node._left = pivot._right
        pivot._right = node
        return pivot

    def _right_rotation(self, node):
        pivot = node._right
        assert pivot is not None, "Node : {}".format(node.value)
        node._right = pivot._left
        pivot._left = node
        return pivot

    def remove(self, value):
        pass

    def _remove_node(self, parent, value):
        if parent.value == value:
            n, p, pl, pr = self._find_large_node(parent)
            parent._value = n.value
            p._left = pl
            p._right = pr
            parent.update_balance()
        # else:

        # pass

    def __contains__(self, value):
        return self._find_node(value) is not None

    def _find_node(self, x):
        node = self._root
        while node is not None:
            if node.value == x:
                return node
            elif x < node.value:
                node = node.left
            elif node.value < x:
                node = node.right
        return None

    def _find_large_node(self, node):
        if node.right is not None:
            n, *p = _find_large_node(node.right.right)
            if n is not None:
                return n, *p
            n, *p = _find_large_node(node.right.left)
            if n is not None:
                return n, *p
            return node.right, node, node.left, None
        if node.left is not None:
            n, *p = _find_large_node(node.left.right)
            if n is not None:
                return n, *p
            n, *p = _find_large_node(node.left.left)
            if n is not None:
                return n, *p
            return node.left, node, None, node.right

        return None, None, None, None


    def to_list(self):
        nodes = self._root.in_order()
        return [n.value for n in nodes]


class Node:

    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def value(self):
        return self._value

    def height(self):
        lh, rh = self.get_heights()
        return max(lh, rh) + 1

    def get_heights(self):
        lh = self._left.height() if self._left else 0
        rh = self._right.height() if self._right else 0
        return lh, rh

    def update_balance(self):
        lh, rh = self.get_heights()
        self._balance = lh - rh

    def in_order(self):
        l = self._left.in_order() if self._left else []
        r = self._right.in_order() if self._right else []
        return l + [self] + r


if __name__ == "__main__":
    import doctest
    doctest.testmod()
