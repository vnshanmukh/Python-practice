class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	currentNode = linkedList
	while currentNode is not None:
		nextNode = currentNode.next
		while nextNode is not None and nextNode.value == currentNode.value:
			nextNode = nextNode.next
		currentNode.next = nextNode
		currentNode = nextNode
	return linkedList