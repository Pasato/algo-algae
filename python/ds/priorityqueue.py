class PriorityQueue:
    def __init__(self, priorityComparator):
        self.__ar = [] # key corresponds to the priority
    def is_empty():
        return len(self.__ar) == 0
    def insert_with_priority(elem, priority):
        self.__ar.append((elem, priority)) 
        return self 
    def pull_highest_priority():
        return self.__ar.sort(priorityComparator)

