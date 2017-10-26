#coding = utf-8
import random
class Headers():
    def __init__(self,filename):
        self.filename = filename
    def headers(self):
        '''
            获取user_agent的函数
        '''
        uas = []
        with open(self.filename, 'r') as f:
            for header in f.readlines():
                if header:
                    uas.append(header.strip()[1:-1])
        random.shuffle(uas)
        return uas