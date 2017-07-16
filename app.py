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
        self.serial = []

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
                    self.save()
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
                        self.save()
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
                    self.save()
            else:
                self.current_node = self.current_node.right_child
                self.traverse()

    def save(self, level=0, current=None):
        if current is None:
            current = self.root_node

        if level < 2:
            self.serial.extend([str(current), str(current.left_child)])
        else:
            # filler = ['-1'] * ((2 ** level) - 2)
            # self.serial.extend(filler)
            self.serial.extend([str(current), str(current.left_child)])

        if current.right_child:
            self.save(level+1, current.right_child)
        else:
            serial = ','.join(self.serial)
            with open('data.csv', 'w') as fout:
                fout.write(serial)

    def bootstrap(self):
        with open('data.csv', 'r') as fin:
            serial = fin.read().split(',')
            for i in range(len(serial)):
                node = Node(serial[i])
                if serial[i] != '-1':
                    if i == 0:
                        self.root_node = node
                        self.current_node = self.root_node
                    else:
                        if self.current_node.left_child is None:
                            self.current_node.left_child = node
                        elif self.current_node.right_child is None:
                            self.current_node.right_child = node
                            self.current_node = self.current_node.right_child
        self.current_node = self.root_node


def main():
    binary_tree = BinaryTree(None)
    binary_tree.bootstrap()
    binary_tree.traverse()


if __name__ == '__main__':
    main()
