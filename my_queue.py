class QueueOne:
    """
    Реализация очереди с помощью динамического массива
    """
    def __init__(self):
        self._buf = [None for _ in range(16)]   # список для хранения элементов очереди
        self._head = 0      # индекс, указывающий на первый элемент очереди в self._buf
        self._size = 0      # количество элементов в очереди
        self._cap = 16      # длина списка self._buf (capacity)
        self._mincap = 16   # минимальная длина списка self._buf
        self._offset = -1   # отступ от self._head при итерации по очереди
    
    def enqueue(self, x):
        self._resize_if_needed()
        
        tail = (self._head + self._size) % self._cap
        self._buf[tail] = x
        self._size += 1
    
    def dequeue(self):
        if self._size == 0:
            raise IndexError('Очередь пуста')
        
        ret_val = self._buf[self._head]
        self._head = (self._head + 1) % self._cap
        self._size -= 1
        self._resize_if_needed()
        return ret_val
    
    def peek(self):
        return self._buf[self._head] if self._size else None
    
    def _resize_if_needed(self):
        if self._size == self._cap:
            self._resize(self._cap * 2)
        
        if (self._size < self._cap // 4) and (self._cap // 2 >= self._mincap):
            self._resize(self._cap // 2)
        
    def _resize(self, new_cap):
        new_buf = [None for _ in range(new_cap)]
        for i, elem in enumerate(self):
            new_buf[i] = elem
        self._buf = new_buf
        self._head = 0
        self._cap = new_cap
    
    def __str__(self):
        return f'Queue<[{" ".join(map(str, self))}]>'
    
    def __repr__(self):
        return str(self)
    
    def __next__(self):
        if self._offset == self._size - 1:
            raise StopIteration
        self._offset += 1
        return self._buf[(self._head + self._offset) % self._cap]
    
    def __iter__(self):
        self._offset = -1
        return self
    
    def __len__(self):
        return self._size


class QueueTwo:
    """
    Реализация очереди с помощью односвязного списка
    """
    class ListNode:
        
        def __init__(self, value, next_=None):
            self.value = value
            self.next = next_
    
    def __init__(self):
        self._size = 0          # количество элементов в очереди
        self._head = None       # ссылка на первый элемент ListItem в очереди
        self._tail = None       # ссылка на последний элемент ListItem в очереди
        self._next_node = None  # поле для хранения элемента очереди при итерации
    
    def enqueue(self, x):
        new_item = self.ListNode(x)
        if self._size > 0:
            self._tail.next = new_item
            self._tail = new_item
        else:
            self._head = self._tail = new_item
        self._size += 1
    
    def dequeue(self):
        if self._size == 0:
            raise IndexError('Очередь пуста')
        
        ret_val = self._head.value
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next
        self._size -= 1
        return ret_val
    
    def peek(self):
        return self._head.value if self._size else None
    
    def __str__(self):
        return f'Queue<[{" ".join(map(str, self))}]>'
    
    def __repr__(self):
        return str(self)
    
    def __next__(self):
        if self._next_node:
            ret_val = self._next_node.value
            self._next_node = self._next_node.next
            return ret_val
        else:
            raise StopIteration
    
    def __iter__(self):
        self._next_node = self._head
        return self
    
    def __len__(self):
        return self._size
