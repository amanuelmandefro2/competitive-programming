class BrowserHistorNode:
    def __init__(self, url):
        self.url = url
        self.prev = self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = BrowserHistorNode(homepage)
        self.curr = self.head
    def visit(self, url: str) -> None:
        new_node = BrowserHistorNode(url)
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url    
        

    def forward(self, steps: int) -> str:
        while self.curr.next and steps:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)