import time

def fbis(num):
    result=[0,1]
    for i in range(num-2): #生成從0~(num-2)-1的數字給i
        #result.append(result[i]+result[i+1])
        result.append(result[-1]+result[-2])#抓取倒數1和倒數2的元素
    return result

def main():
    result = fbis(10)
    fobj = open('result.txt','w+')
    for i,num in enumerate(result):
        print("index {0:d} is {1:d}".format(i,num))#多個變數時要加小括號
        fobj.write("%d " % num)
        time.sleep(1)

if __name__=='__main__':
        main()