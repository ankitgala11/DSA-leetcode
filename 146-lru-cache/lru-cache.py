class Node:
    def __init__(self, k, v):
        self.k=k
        self.v=v
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.mp={}
        
        self.head=Node(0, 0)
        self.tail=Node(0, 0)

        self.head.next=self.tail
        self.tail.prev=self.head

    
    def add_after_head(self, node):
        node.next=self.head.next
        node.next.prev=node

        self.head.next=node
        node.prev=self.head



    def del_node(self, node):

        node.prev.next=node.next
        node.next.prev=node.prev



        

    def get(self, key: int) -> int:
        if key in self.mp:
            node=self.mp[key]
            self.del_node(node)
            self.add_after_head(node)
            return node.v

        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.mp:
            node=self.mp[key]
            self.del_node(node)
            self.add_after_head(node)
            node.v=value


        else:
            node=Node(key, value)
            self.mp[key]=node
            if len(self.mp) > self.capacity:
                temp=self.tail.prev
                self.del_node(temp)
                self.mp.pop(temp.k)

                self.add_after_head(node)




            else:
                self.add_after_head(node)



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)