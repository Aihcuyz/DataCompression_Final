class Node(object):
    def __init__(self, parent=None, left=None, right=None, weight=0, symbol='empty'):
        super(Node, self).__init__()
        self._parent = parent
        self._left = left
        self._right = right
        self._weight = weight
        self._symbol = symbol

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def get_left(self):
        return self._left

    def set_left(self, left):
        self._left = left

    def get_right(self):
        return self._right

    def set_right(self, right):
        self._right = right

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol
