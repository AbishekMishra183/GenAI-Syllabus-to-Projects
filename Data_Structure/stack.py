class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, item):
        if self.top == self.size - 1:
            print("Stack Overflow!")
        else:
            self.top += 1
            self.stack[self.top] = item
            print(f"{item} is pushed into stack")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow!")
        else:
            removed = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f"{removed} is popped from stack")

    def display(self):
        if self.top == -1:
            print("Stack is Empty!")
        else:
            print("The elements in the stack are:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

    def peek(self):
        if self.top == -1:
            print("Stack is Empty!")
        else:
            print(f"Top element is: {self.stack[self.top]}")


def main():
    size = int(input("Enter the size of the stack: "))
    s = Stack(size)

    while True:
        print("\n1.Push\n2.Pop\n3.Display\n4.Peek\n5.Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter element to push: ")
            s.push(item)

        elif choice == 2:
            s.pop()

        elif choice == 3:
            s.display()

        elif choice == 4:
            s.peek()

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

main()

        
