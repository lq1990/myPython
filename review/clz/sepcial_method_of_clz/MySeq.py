

class MySeq:
    def __init__(self):
        self.lseq=['I', 'II', 'III', 'IV']

    def __len__(self):
        return len(self.lseq)

    def __getitem__(self, item):
        if 0 <= item < 4:
            return self.lseq[item]


if __name__ == '__main__':
    m = MySeq() # 使得类成为一个序列
    for i in range(4):
        print(m[i])





