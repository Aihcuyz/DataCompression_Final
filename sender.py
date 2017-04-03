from node import Node

class encoder():
    def __init__(self):
        self._NYT = Node(symbol='NYT')
        self._root = self._NYT
        self._round = 0
        self._pre_encode_length = 0
        self._encoded_length = 0

    def encode(self,symbol):
        first_key = True if self._root == self._NYT else False
        self._round = self._round + 1
        self._pre_encode_length = self._pre_encode_length + 1
        search_input_node = self.search_node(self._root,symbol)

        if search_input_node != None:
            input_node,node_path = search_input_node[0],search_input_node[1]
        else:
            input_node = None
        
        message = 'send symbol: ' + repr(symbol)
        if input_node:
            biggest_node = self.find_biggest_node([self._root],input_node.get_weight())
            
            if biggest_node != input_node and biggest_node != input_node.get_parent(): 
                self.swap_node(biggest_node,input_node)

            input_node.set_weight(input_node.get_weight() + 1)
            self.increment_all_parent_weight(input_node)
            message = message + '(exist) => ' + node_path
        else:
            message = message + '(new symbol) => '
            if first_key:
                node_path = bin(ord(symbol))[2:].zfill(8)
                message = message + node_path + '(first symbol)'
            else:
                nyt = self.search_node(self._root,'NYT')[1]
                node_path = nyt + bin(ord(symbol))[2:].zfill(8)
                message = message + nyt + '(NYT) + ' + node_path + '(encoded symbol)'
                self._encoded_length = self._encoded_length + len(nyt)
            self.insert_node(symbol)
        self._encoded_length = self._encoded_length + len(node_path)
        message = message + '\nCompression Ratio:' + str(float(self._pre_encode_length * 8) / self._encoded_length)
        self.write_encode_log(message)
        return node_path

    def insert_node(self, symbol=''):
        new_NYT_node = Node(parent=self._NYT, symbol='NYT')
        new_symbol_node = Node(parent=self._NYT, weight=1, symbol=symbol)
        self._NYT.set_left(new_NYT_node)
        self._NYT.set_right(new_symbol_node)
        self._NYT.set_weight(1)
        self._NYT.set_symbol('empty')
        self.increment_all_parent_weight(self._NYT)
        if self._NYT.get_parent() == None:
            self._root = self._NYT

        self._NYT = self._NYT.get_left()
        
    def increment_all_parent_weight(self, node):
        while self._root != node:
            node = node.get_parent()
            if self._root != node:
                biggest_node = self.find_biggest_node([self._root],node.get_weight())
                if biggest_node != None and biggest_node != node and biggest_node != node.get_parent():  
                    self.swap_node(biggest_node,node)

            node.set_weight(node.get_weight() + 1)
            

    def swap_node(self, node_a, node_b):
        old_b_parent = node_b.get_parent()

        if node_a.get_parent().get_left() == node_a:
            node_a.get_parent().set_left(node_b)
        else:
            node_a.get_parent().set_right(node_b)

        node_b.set_parent(node_a.get_parent())
        node_a.set_parent(old_b_parent)

        if old_b_parent.get_left() == node_b:
            old_b_parent.set_left(node_a)
        else:
            old_b_parent.set_right(node_a)
            

    def find_biggest_node(self, node_queue, weight):
        while len(node_queue) != 0:
            node = node_queue.pop(0)
            if node.get_weight() == weight and self._root != node:
                return node

            if node.get_right() != None:
                node_queue.append(node.get_right())

            if node.get_left() != None:
                node_queue.append(node.get_left())

        return None
        

    def search_node(self, node, symbol, path=''):
        if node.get_symbol() == symbol:
            return node,path
        else:
            if node._left != None:
                search_left = self.search_node(node.get_left(),symbol,path + '0')
                if search_left != None:
                    return search_left
            if node._right != None:
                search_right = self.search_node(node.get_right(),symbol,path + '1')
                if search_right != None:
                    return search_right
    
    def write_encode_log(self,message):
        file_pointer = open('encode_log.log','a')
        file_pointer.write("=" * 30 + " Round " + str(self._round) + " start " + "=" * 30 + "\n")
        file_pointer.write(message + '\n')
        self.show_all(self._root,file_pointer)
        file_pointer.write("=" * 35 + " end " + "=" * 35 + "\n\n")
        file_pointer.close()

    def show_all(self, node, file_pointer):
        message = "node symbol:" + repr(str(node.get_symbol())) + '(' + str(node.get_weight()) + ')'
        if node.get_left() != None:
            message = message + '\t left symbol:' + repr(node.get_left().get_symbol()) + '(' + str(node.get_left().get_weight()) + ')'
            self.show_all(node.get_left(),file_pointer)
        if node.get_right() != None:
            message = message + '\t right symbol:' + repr(node.get_right().get_symbol()) + '(' + str(node.get_right().get_weight()) + ')'
            self.show_all(node.get_right(),file_pointer)
        file_pointer.write(message + "\n")
