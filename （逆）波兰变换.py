#eval(input())



# 定义结点
class Node(object):
    def __init__(self, number):
        self.number = number
        self.left = None
        self.right = None
#定义树
class Tree(object):
    def __init__(self,root_1):
        self.root = root_1

#定义各个运算符的优先级
operation_dict = {
    '(':1,
    ')':2,
    '+':3,
    '-':4,
    '*':5,
    '/':6,
    }


#前序遍历生成列表，当节点递归至叶子节点时，函数返回None，由于字符串无法与None直接相加，故先以列表形式存储起来
def forward(root_1,fow):
    if(root_1!=None):
        fow.append(root_1.number)
        fow.append(forward(root_1.left,fow))
        fow.append(forward(root_1.right,fow))

#后序遍历    
def backward(root_1,back):
    if(root_1!=None):
        back.append(backward(root_1.left,back))
        back.append(backward(root_1.right,back))
        back.append(root_1.number)

#将列表处理成逆波兰/波兰表达式
def polish_print(equation,PN):
    for i in equation:
        if(i!=None):
                PN=PN+i

#生成二叉树
def transform(equation):
    operation = []
    contents_node =[]
    operations_node = []
    equation = equation.replace(' ','')
    for content in equation:
        #把文字或字母或数字问号等直接输出（其ACII码均大于"/"，但所有运算符ACII码均小于其）
        if(content>"/"):
            content_node=Node(content)
            content_node.left = None
            content_node.right = None
            contents_node.append(content_node)
        else:
            #存储运算符的列表为空时直接输入第一个运算符
            if(len(operation)==0):
                operation.append(content)
                operation_node=Node(content)
                operation_node.left = None
                operation_node.right = None
                operations_node.append(operation_node)
            #若运算符优先级大于栈顶元素，或者其为"(",直接压入该运算符
            elif(operation_dict[content]==1 or operation_dict[content]>operation_dict[operation[len(operation)-1]]):
                operation.append(content)
                operation_node=Node(content)
                operation_node.left = None
                operation_node.right = None
                operations_node.append(operation_node)
            #若运算符小于栈顶元素（除了')'），则依次输出所有比它优先级高的栈内元素，输出完毕后再将其入栈
            elif(content!=')'):
                while(operation_dict[content]<operation_dict[operation[len(operation)-1]]):
                    operation_node=Node(content)
                    operation_node.right=contents_node[len(contents_node)-1]
                    del contents_node[len(contents_node)-1]
                    operation_node.left=contents_node[len(contents_node)-1]
                    del contents_node[len(contents_node)-1]
                    contents_node.append(operation_node)    
                    del operation[len(operation)-1]
                operation.append(content)
            #处理运算符是')'时的情况
            else:
                while(content<operation[len(operation)-1]):
                    operation_node=Node(operation[len(operation)-1])
                    operation_node.right=contents_node[len(contents_node)-1]
                    del contents_node[len(contents_node)-1]
                    operation_node.left=contents_node[len(contents_node)-1]
                    del contents_node[len(contents_node)-1]
                    contents_node.append(operation_node)
                    
                    del operation[len(operation)-1]
                    del operations_node[len(operations_node)-1]
                del operation[len(operation)-1]
                del operations_node[len(operations_node)-1]
    #将运算符栈内剩余元素依次输出
    while(len(operation)!=0):
        operation_node=Node(operation[len(operation)-1])
        operation_node.right=contents_node[len(contents_node)-1]
        del contents_node[len(contents_node)-1]
        operation_node.left=contents_node[len(contents_node)-1]
        del contents_node[len(contents_node)-1]
        contents_node.append(operation_node)  
        del operation[len(operation)-1]
    # 二叉树类的实例化，即确定根节点
    t = Tree(contents_node[len(contents_node)-1])  
    return t




if __name__ == '__main__':
    back = []
    fow = []
    RPN=""
    PN=""
    print("请输入布尔逻辑表达式")
    equation = input()
    tree = transform(equation)
    backward(tree.root,back)
    forward(tree.root,fow)
    for i in back:
        if(i!=None):
            RPN+=i
    for i in fow:
        if(i!=None):
            PN+=i
    print("逆波兰表达式:"+RPN)
    print("波兰表达式:"+PN)
    



