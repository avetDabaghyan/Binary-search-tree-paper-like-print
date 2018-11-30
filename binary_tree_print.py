class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if self.queue == []:
            return True
        else:
            return False

    def enqueue(self, new):
        self.queue.insert(0, new)

    def dequeue(self):
        return self.queue.pop()

    # def size(self):
    #     return len(self.queue)

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print "Value already in tree. "

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0
    def _height(self, cur_node, cur_height):
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left,cur_height+1)
        right_height = self._height(cur_node.right,cur_height+1)
        return max(left_height,right_height)


    #Uses breadth-first traversing. Top-down, left-right.
    #Uses a queue 
    def print_tree(self):
        if self.root != None:
            print "breadth-first traversing print: "
            print self.root.data #print first item right away.
            self._print_tree(self.root, q=Queue())
    def _print_tree(self, cur_node, q):
        #Checking left items first, so that next possible traversals happen from the left child.
        if cur_node.left != None:
            print cur_node.left.data
            #Adds the child to the queue only if it actually exists
            q.enqueue(cur_node.left)
        if cur_node.right != None:
            print cur_node.right.data
            #Adds the child to the queue only if it actually exists
            q.enqueue(cur_node.right)
        #Checks if there is another node left to traverse through
        if not(q.isEmpty()):
            next_node = q.dequeue()
            self._print_tree(next_node, q) #Recursion here.
        else:
            print "end print"

    #Uses the same traversing as above.
    #Starts the same way
    def good_print(self):
        if self.root != None:
            print "good print: "
            print str(self.root.data) #print first item right away
            self._good_print(self.root, q=Queue(), text = "", end_node = None)
        else:
            "good print: tree is empty "
            return 0
    #Here, we need 2 more variables.
    #text is for collecting the children on the same level before printing all of them together.
    #end_node is for comparing to see if the function has switched to lower level.
    def _good_print(self, cur_node, q, text, end_node):
        #Check if the function changed level. If it did, prints whatever was collected on the previous level
        #and resets text and end_node for collecting for new level.
        if cur_node == end_node:
            print text
            text = ""
            end_node = None
        if cur_node.left != None:
            text = text + "< " + str(cur_node.left.data) + " "
            q.enqueue(cur_node.left)
            #Looks for the first child of the next level. When it's found, stops looking until level is changed.
            if end_node is None:
                end_node = cur_node.left
        else:
            text = text + "< --- "
        if cur_node.right != None:
            text = text + str(cur_node.right.data) + " >"
            q.enqueue(cur_node.right)
            #Looks for the first child of the next level. When it's found, stops looking until level is changed.
            if end_node is None:
                end_node = cur_node.right
        else:
            text = text + "--- >"
        if not(q.isEmpty()):
            next_node = q.dequeue()
            self._good_print(next_node, q, text, end_node)
        else:
            print "end good print"

#Random tree generator.
def fill_tree(tree, num_elems = 20, min_int = 100, max_int=999):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(min_int,max_int)
        tree.insert(cur_elem)
    return tree


def main():
    tree = Tree()
    tree = fill_tree(tree)
    # tree.insert(5)
    # tree.insert(3)
    # tree.insert(7)
    # tree.insert(0)


    tree.print_tree()
    tree.good_print()
    print "main end"


main()
