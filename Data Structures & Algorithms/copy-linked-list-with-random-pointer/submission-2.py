class Solution:
    visited = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        if head in self.visited:
            return self.visited.get(head)

        node = Node(head.val, None, None)
        self.visited[head] =  node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node