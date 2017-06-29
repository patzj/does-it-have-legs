#!/usr/bin/python3


class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return self.data


class BinaryTree:

    def __init__(self, node):
        self.root_node = node
        self.current_node = self.root_node

    def traverse(self):
        q1 = input('%s?(y/n): ' % str(self.current_node))
        if q1 == 'y':
            q2 = input('Is it a %s?(y/n): ' % str(
                self.current_node.left_child
            ))
            if q2 == 'y':
                print('Yay! I got it!')
                q3 = input('Do you want to play again?(y/n): ')
                if q3 == 'y':
                    self.current_node = self.root_node
                    self.traverse()
                else:
                    print('Bye.')
                    # TODO
                    # Serialize
            else:
                if self.current_node.right_child is None:
                    self.temp = input('What is it?: ')
                    new_node = Node(
                        input(
                            'Write a question that the answer is %s: ' %
                            self.temp
                        )
                    )
                    self.current_node.right_child = new_node
                    self.current_node = self.current_node.right_child
                    self.current_node.left_child = Node(self.temp)
                    print('OK! Got it.')
                    q4 = input('Should we play again?(y/n): ')
                    if q4 == 'y':
                        self.current_node = self.root_node
                        self.traverse()
                    else:
                        print('Bye.')
                        # TODO
                        # Serialize
                    self.current_node = self.root_node
                    self.traverse()
                else:
                    self.current_node = self.current_node.right_child
                    self.traverse()
        else:
            if self.current_node.right_child is None:
                self.temp = input('What is it?: ')
                new_node = Node(
                    input(
                        'Write a question that the answer is %s: ' %
                        self.temp
                    )
                )
                self.current_node.right_child = new_node
                self.current_node = self.current_node.right_child
                self.current_node.left_child = Node(self.temp)
                print('OK! Got it.')
                q5 = input('Should we play again?(y/n): ')
                if q5 == 'y':
                    self.current_node = self.root_node
                    self.traverse()
                else:
                    print('Bye.')
                    # TODO
                    # Serialize
            else:
                self.current_node = self.current_node.right_child
                self.traverse()


def main():
    root_node = Node('Does it have legs')
    root_node.left_child = Node('dog')
    binary_tree = BinaryTree(root_node)
    binary_tree.traverse()


if __name__ == '__main__':
    main()
