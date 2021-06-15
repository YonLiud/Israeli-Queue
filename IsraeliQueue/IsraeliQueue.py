class IsraeliQueue(list):
    def enqueue(self, a):
        for i in range(len(self)):
            if type(self[i][0]) == type(a):
                self[i].append(a)
                break
        else:
            self.append([a])
    def dequeue(self):
        return self.pop(0)