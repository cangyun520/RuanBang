# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-7-19.
 * QQ 405367236
"""

# Hash库
import hashlib as hs
# 时间库
import datetime as date
# 区块


class Block():
    # 构造方法，传入数据包括索引、时间戳、数据、上一笔账单的Hash串、可更改的数字
    def __init__(self, index, timestamp, data, preHash, number):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.number = number
        self.preHash = preHash
        self.hash = self.blockHash()

    # 生成Hash串
    def blockHash(self):
        sha = hs.sha256()
        sha.update(str(str(self.index) + str(self.timestamp) + str(self.data) + str(self.preHash) + str(self.number)).encode("utf-8"))
        return sha.hexdigest()


# 创建初始区块
def initBlock():
    rst = Block(0,date.datetime.now(),"first","0",0)
    return rst
# 创建区块链
blockChain = [initBlock()]
preBlock = blockChain[0]
# 测试运行所用时间
starttime = date.datetime.now()
# 生成10个区块
for i in range(0,10):
    # 通过修改数字来生成Hash串
    for j in range(0,10000000000):
        # 由于我懒，时间戳、数据都使用了上一个区块的数据，实际需要交易时的数据
        nextBlock = Block(preBlock.index+1,preBlock.timestamp,preBlock.data,preBlock.hash,j)
        # 这里只测试了前六个字符为0时的数据，成功则加入区块链
        if nextBlock.hash[:5] == "00000":
            blockChain.append(nextBlock)
            preBlock = nextBlock
            break
    print(preBlock.hash)
# 测试运行所用时间
endtime = date.datetime.now()
print((endtime-starttime).seconds)



"""
https://blog.csdn.net/fyq201749/article/details/80973103
"""