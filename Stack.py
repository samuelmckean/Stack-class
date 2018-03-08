class Stack:
    def __init__(self, lst=[]):
        self.__lst = lst

    # constructor for Stack class    
    def Stack(self, startingList):
        self.__init__(startingList)
        
    # returns True if the stack is empty
    def isEmpty(self):
        if self.__lst == []:
            return True
        else:
            return False

    # returns the top element of the stack without removing it
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__lst[len(lst) - 1]
        
    # adds another element to the top of the stack
    def push(self, value):
        self.__lst.append(value)

    # removes and returns the top element of the stack
    def pop(self):
        return self.__lst.pop()

    # returns the number of element in the stack
    def getSize(self):
        return len(self.__lst)
