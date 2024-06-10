from queue import PriorityQueue
from functools import total_ordering 
import pickle

@total_ordering
class Node:
    def __init__(self, left: 'Node' = None, right: 'Node' = None, frequency: int = None ) -> None:
        self.frequency = frequency if frequency is not None else left.get_frequency() + right.get_frequency() 
        self.right = right
        self.left = left

    def get_frequency(self) -> int:
        return self.frequency or 0

    def __lt__(self, other): 
        return self.frequency < other.frequency 
  
    def __eq__(self, other): 
        return self.frequency == other.frequency 
  
    def __le__(self, other): 
        return self.frequency<= other.frequency 
      
    def __ge__(self, other): 
        return self.frequency>= other.frequency 
          
    def __ne__(self, other): 
        return self.frequency != other.frequency 

class Leaf(Node):
    def __init__(self, character, frequency) -> None:
        super().__init__(frequency=frequency)
        self.character = character

class Huffman:
    def __init__(self, text) -> None:
        self.text = text
        self.frequencies = {}
        self.huffman_codes = {}
        self.fill_frequencies()
        self.root: Node = None

    def fill_frequencies(self):
        for chr in self.text:
            self.frequencies[chr] = self.frequencies.get(chr, 0) + 1

    def encode(self):
        # 2. Build the binary tree from the frequencies.
        queue = PriorityQueue()

        # put all the leaf nodes containing the characters in the queue
        for character, frequency in self.frequencies.items():
            queue.put( Leaf(character, frequency))

        # pull out the bottom two or lowest frequency leaf
        # sum their frequencies and then add the node back into the queue
        while queue.qsize() > 1:
            queue.put(Node(queue.get(), queue.get()))

        self.root = queue.get()

        # 3. Generate the prefix-code table from the tree.
        self.generate_huffman_code(self.root, "")

        # 4. Encode the text using the code table.
        return self.get_encoded_text()

    def generate_huffman_code(self, node: Node, code):
        if isinstance(node, Leaf):
            self.huffman_codes[node.character] = code
            return
        
        self.generate_huffman_code(node.left, code + "0")
        self.generate_huffman_code(node.right, code + "1")

    def get_encoded_text(self):
        result = ""

        for c in self.text:
            result += self.huffman_codes[c]

        return result
    
    def decode(self, code):
        result = ""
        current = self.root

        for chr in code:
            current = current.left if chr == "0" else current.right

            if isinstance(current, Leaf):
                result += current.character
                current = self.root
        
        return result

       
