

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        idx = 0
        currNode = self.head

        while idx < index and currNode is not None:
            currNode = currNode.next
            idx += 1

        return currNode.val if currNode is not None else -1

    def insertHead(self, val: int) -> None:
        if self.head is None:
            n = Node(val, None)
            self.head = self.tail = n
        else:
            n = Node(val, self.head)
            self.head = n

    def insertTail(self, val: int) -> None:
        if self.tail is None:
            n = Node(val, None)
            self.tail = self.head = n
        else:
            currTail = self.tail
            n = Node(val, None)
            self.tail = n
            currTail.next = self.tail

    def remove(self, index: int) -> bool:
        """
        Takes the index of element to remove from linked list.\n
        Example: index = 3\n
        [ 1 -> 2 -> 3 -> (4) -> 5 ]\n
        [ 1 -> 2 -> 3 -> __ -> 5 ] => [ 1 -> 2 -> 3 -> 5 ]
        """

        if index == 0 and self.head is not None:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True
        currIdx = 0
        currItem = self.head

        while currIdx < index - 1 and currItem is not None:
            currIdx += 1
            currItem = currItem.next

        if currItem is None:  # no item before target
            return False
        if currItem.next is None:  # no item at target index
            return False
        else:  # unlink
            currItem.next = currItem.next.next
            if currItem.next is None:  # update tail?
                self.tail = currItem

        return True

    def getValues(self) -> list[int]:
        items = []
        curr = self.head

        while curr is not None:
            items.append(curr.val)
            curr = curr.next
        return items


class Node:
    def __init__(self, val: int, next: Node | None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"[{self.val}]"


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertHead(1)
    ll.insertTail(2)
    ll.insertHead(0)
    toRemove = ll.remove(1)
    vals = ll.getValues()
    print(vals)
