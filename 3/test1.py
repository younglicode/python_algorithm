## 检测环路
## 找出环路的单向链表的入口节点
## 通过字典缓存走过的节点，如果重现重复的节点，该节点就是入口节点
## 还有另外一种方法，就是快慢指针法

class ListNode:
    def __init__(self, v) -> None:
        self.val = v
        self.next = None

def create_case(length: int, x: int) -> ListNode:
    if x > length:
        return None
    
    head = ListNode(v=0)
    if x == 0:
        return head
    
    x_node = None

    current_node = head
    for i in range(1, length):
        next_node = ListNode(v=i)
        current_node.next = next_node
        current_node = next_node
        if x == i:
            x_node = current_node

    current_node.next = x_node

    return head

def find_x_node(head: ListNode ) -> (ListNode):
    node_dict = dict()

    while head:
        if node_dict.get(head):
            return head
        else:
            node_dict[head] = True
            print(head.val)
            head = head.next

    return None

if __name__ == "__main__":
    case_node1 = create_case(length=1000, x=455)
    x_node = find_x_node(case_node1)
    if x_node:
        print(x_node.val)

    


        

