def reverse(str):
    list=[]
    for i in range(len(str)-1,-1,-1): #从len(str)-1到-1 步长为-1
        list.append(str[i])
    return ''.join(list) #返回通过指定字符连接序列中元素后生成的新字符串

x=reverse('I am unstoppable')
print(x)

