class SnapshotArray:

    def __init__(self, length: int):
        self.data = [0] * length 
        self.snapshotChanges = [[] for i in range(length)]
        self.snapId = 0
        

    def set(self, index: int, val: int) -> None:
        self.data[index] = val
        changes = self.snapshotChanges[index]
        if len(changes) > 0 and changes[-1][0] == self.snapId:
            changes[-1][1] = val
        else:
            self.snapshotChanges[index].append([self.snapId, val])
        

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1
        

    def get(self, index: int, snap_id: int) -> int:
        changes = self.snapshotChanges[index]

        insert_index = bisect.bisect(changes, snap_id, key=lambda c : c[0])

        if insert_index == 0:
            return 0
        
        return changes[insert_index - 1][1]


        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)