def loadDataset():
    D = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
    return D


def createC1(D):
    C1 = []
    for t in D:
        for item in t:
            if not {item} in C1:
                C1.append({item})

    C1.sort()
    return list(map(frozenset, C1))  # map 生成了一个迭代器


def scanD(D, Ck, minSup):
    m1 = {}
    for t in D:  # t is each transaction of Dataset
        for item in Ck:  # Ck is Candidate itemset
            if item.issubset(t):
                if item not in m1.keys():
                    m1[item] = 1
                else:
                    m1[item] += 1

    totalItems = float(len(D))

    L = []  # store 频繁数据项集
    N = []  # store non freq itemset
    supportData = {}  # 候选集项Ck的支持度字典 {key: 候选项, value: 支持度}
    for item in m1:
        sup = m1[item] / totalItems
        supportData[item] = sup
        if sup >= minSup:
            L.append(item)
        else:
            N.append(item)

    return L, N, supportData


def aprioriGen(Lk, k, N):
    """
    生成 k+1项集的算法
    L1 => C2，或 L2 => C3, ...
    :param Lk:
    :param k:
    :param N:
    :return:
    """

    Ck = []
    lenLk = len(Lk)
    for i in range(lenLk):
        # 子连接运算
        for j in range(i+1, lenLk):
            # 前k-2个项同时，将两个集合合并
            L1 = list(Lk[i])[:k-2]
            L1.sort()
            L2 = list(Lk[j])[:k-2]
            L2.sort()
            if L1 == L2:
                Ck.append(Lk[i] | Lk[j]) # 加入并集
        # 把子集中有属于非频繁项目集的项目删除
        # 非频繁项集的 超集 肯定是非频繁
        for i in N:
            for j in Ck:
                if set(i).issubset(j):
                    Ck.remove(j)

    return Ck


def apriori(D, minsup=0.5):
    C1 = createC1(D)
    L1,N,supportData = scanD(D, C1, minsup)
    L = [L1]
    k = 2
    while(len(L[k-2]) > 0): # 迭代进行
        Ck = aprioriGen(L[k-2], k, N)
        Lk, Nk, supK = scanD(D, Ck, minsup)
        supportData.update(supK)
        N += Nk
        L.append(Lk)
        k += 1
    return L, N, supportData


if __name__ == '__main__':
    D = loadDataset()
    # C1 = createC1(D)
    # L1, N, supportData = scanD(D, C1, 0.5)
    L, N, supportData = apriori(D)

    print("L:")
    for i in L:
        print(i)

    print("N:")
    for i in N:
        print(i)

    print("supportData:")
    for k in supportData:
        print(k, supportData[k])


