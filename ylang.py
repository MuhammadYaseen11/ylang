import sys

variables = {}

# Array class
class Array:
    def __init__(self, values):
        self.values = values
    
    def insert(self, index, value):
        if 0 <= index <= len(self.values):
            self.values.insert(index, value)
        else:
            print(f"[Error] Insert index {index} out of bounds")
    
    def delete(self, index):
        if 0 <= index < len(self.values):
            self.values.pop(index)
        else:
            print(f"[Error] Delete index {index} out of bounds")
    
    def sort(self):
        self.values.sort()
    
    def search(self, value):
        try:
            return self.values.index(value)
        except ValueError:
            return -1
    
    def __str__(self):
        return str(self.values)

# Linked List Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def delete(self, value):
        curr = self.head
        prev = None
        while curr:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next
        print(f"[Error] Value {value} not found to delete")
    
    def traverse(self):
        values = []
        curr = self.head
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values
    
    def __str__(self):
        return "->".join(map(str, self.traverse()))

# Binary Tree Node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Tree class (Insert to maintain BST property)
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)
    
    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result
    
    def __str__(self):
        return str(self.inorder())

def get_value(token):
    try:
        return int(token)
    except ValueError:
        val = variables.get(token)
        if val is not None:
            return val
        else:
            print(f"[Error] Variable '{token}' not defined")
            return None

def interpret(line):
    line = line.strip()
    if not line or line.startswith("#"):  # comment line
        return

    words = line.split()

    if words[0] == "let":
        # let var = value
        if len(words) >= 4 and words[2] == "=":
            val = get_value(words[3])
            if val is not None:
                variables[words[1]] = val
        else:
            print("[Error] Usage: let var = value")

    elif words[0] == "say":
        if len(words) == 1:
            print("[Error] say needs argument")
            return
        if words[1].startswith('"'):
            # print string literal between quotes
            start = line.find('"')
            end = line.rfind('"')
            print(line[start+1:end])
        else:
            var = words[1]
            if var in variables:
                print(variables[var])
            else:
                print(f"[Error] Variable '{var}' not defined")

    elif words[0] == "array":
        # array var = [1,2,3]
        try:
            var_name = words[1]
            start = line.find("[")
            end = line.find("]")
            values = list(map(int, line[start+1:end].split(',')))
            variables[var_name] = Array(values)
            print(f"Created array '{var_name}': {variables[var_name]}")
        except Exception as e:
            print("[Error] Failed array creation:", e)

    elif words[0] == "linkedlist":
        # linkedlist var
        if len(words) == 2:
            variables[words[1]] = LinkedList()
            print(f"Created linkedlist '{words[1]}'")
        else:
            print("[Error] Usage: linkedlist var")

    elif words[0] == "tree":
        # tree var
        if len(words) == 2:
            variables[words[1]] = Tree()
            print(f"Created tree '{words[1]}'")
        else:
            print("[Error] Usage: tree var")

    # method calls like arr.insert(2, 9) or list.insert(10)
    elif "." in words[0]:
        try:
            var_name, method_call = words[0].split(".")
            if var_name not in variables:
                print(f"[Error] Variable '{var_name}' not defined")
                return #
            obj = variables[var_name]
            method_name = method_call[:method_call.find("(")]
            params_str = method_call[method_call.find("(")+1:method_call.find(")")]
            params = []
            if params_str.strip():
                params = list(map(int, params_str.split(',')))

            if hasattr(obj, method_name):
                method = getattr(obj, method_name)
                ret = method(*params)
                # If method returns something (like search), print it
                if ret is not None:
                    print(ret)
                else:
                    print(f"{var_name} after {method_name}: {obj}")
            else:
                print(f"[Error] Method '{method_name}' not supported for {var_name}")

        except Exception as e:
            print("[Error] Method call failed:", e)

    elif words[0] == "repeat":
        # repeat n times command
        try:
            times = int(words[1])
            if words[2] != "times":
                print("[Error] Usage: repeat n times command")
                return
            sub_command = " ".join(words[3:])
            for _ in range(times):
                interpret(sub_command)
        except Exception as e:
            print("[Error] Repeat command error:", e)

    elif words[0] == "add":
        # add x to y
        if len(words) == 4 and words[2] == "to":
            a = get_value(words[1])
            b = get_value(words[3])
            if isinstance(a, int) and isinstance(b, int):
                print(a + b)
            else:
                print("[Error] add requires integers")
        else:
            print("[Error] Usage: add x to y")

    else:
        print(f"[Error] Unknown command: {line}")

def run_file(filename):
    with open(filename) as f:
        for line in f:
            interpret(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ylang.py yourfile.ylang")
    else:
        run_file(sys.argv[1])
