from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
import pandas as pds
from scipy import sparse

#定义链式结点
class LinkNode(object):
    def __init__(self,data):
        self.attr=data
        self.next=None

#定义链式栈及进出栈操作函数
class Stack(object):
    def __init__(self):
        self.head=None

    def pop(self):
        if self.head:
            HeadNode=self.head
            self.head=HeadNode.next
            return HeadNode.attr

    def push(self,data):
        node=LinkNode(data)
        node.next=self.head
        self.head=node

    def IsEmpty(self):
        if self.head==None:
            return True

#定义链式队列及出入队列操作函数
class Queue(object):
    def __init__(self):
        self.front=None
        self.rear=None

    def EnQueue(self,data):
        node=LinkNode(data)
        RearNode=self.rear
        RearNode.next=node
        self.rear=node

    def DeQueue(self):
        if self.front!=None:
            HeadNode=self.front
            self.front=HeadNode.next
            if self.front==self.rear:
                self.rear=None
            HeadNode.next=None
            return HeadNode.attr

    def IsEmpty(self):
        if self.front==None and self.rear==None:
            return True

#定义树及基本操作
class TreeNode(object):
    def __init__(self,data):
        self.attr=data
        self.left=None
        self.right=None

#按照层次遍历来构造树
def InitTree(data):
    #默认以第一个结点为根节点
    length=len(data)
    node_list=[]
    for i in range(length):
        node_list.append(TreeNode(data[i]))
    for i in range(length//2):
        if (2*i+2) <= length:
            node_list[i].left=node_list[2*i+1]
        if (2*i+3) <= length:
            node_list[i].right=node_list[2*i+2]
    T = Tree(node_list[0])
    return T

#定义二叉树以及常用函数（遍历和线索化）
class Tree(object):
    def __init__(self,root):
        self.root=root

    def ForOrder(self):
        node = self.root
        for_str=""
        s=Stack()
        while s.head!=None or node!=None:
            if node!=None:
                s.push(node)
                for_str=for_str+str(node.attr)
                node=node.left
            else:
                node=s.pop()
                node=node.right
        return for_str

    def InOrder(self):
        node=self.root
        in_str=""
        s=Stack()
        while s.head!=None or node!=None:
            if node!=None:
                s.push(node)
                node=node.left
            else:
                node=s.pop()
                in_str=in_str+str(node.attr)
                node=node.right
        return in_str

    def BackOrder(self):
        node=self.root
        s=Stack()
        back_str=""
        while s.head!=None or node!=None:
            if node!=None:
                s.push(node)
                last_node=node
                node=node.left
            else:
                node=last_node
                #确保右子树存在且未被访问过（易忘记）
                if node.right!=None and node.right!=data:
                    node=node.right
                else:
                    node=s.pop()
                    back_str=back_str+str(node.attr)
                    data=node
                    node=None
        return back_str

    def LevelOrder(self):
        q=Queue()
        node=self.root
        level_str=""
        q.EnQueue(node)
        while not(node==None and q.IsEmpty()):
            p=q.DeQueue()
            level_str=level_str+str(p.attr)
            if p.left:
                q.EnQueue(p.left)
            if p.right:
                q.EnQueue(p.right)
        return level_str

    def 




        

