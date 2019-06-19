#THIAGO CESAR DE MIRANDA SILVA
class Node:
    def __init__(self, data = None, father = None, leftSon = None, rightSon = None):
        self._data = data
        self._father = father
        self._leftSon = leftSon
        self._rightSon = rightSon
    
    def getData(self):
        return self._data
    
    def setData(self, newData):
        self._data = newData
    
    def getFather(self):
        return self._father
    
    def setFather(self, newFather):
        self._father = newFather
    
    def getLeftSon(self):
        return self._leftSon
    
    def setLeftSon(self, newLeftSon):
        self._leftSon = newLeftSon
    
    def getRightSon(self):
        return self._rightSon
    
    def setRightSon(self, newRightSon):
        self._rightSon = newRightSon

class BinaryTree:
    def __init__(self, root = None):
        self._root = root
    
    def getRoot(self):
        return self._root
    
    def setRoot(self, newRoot):
        self._root = newRoot
        
    def insert(self, z):
        newNode = Node(z)
        y = None
        x = self._root
        while x != None:
            y = x
            if z < x.getData():
                x = x.getLeftSon()
            else:
                x = x.getRightSon()
        newNode.setFather(y)
        if y == None:
            self._root = newNode
        elif z < y.getData():
            y.setLeftSon(newNode)
        else:
            y.setRightSon(newNode)
    
    def search(self, k):
        x = self._root
        while x != None and k != x.getData():
            if k < x.getData():
                x = x.getLeftSon()
            else:
                x = x.getRightSon()
        return x
    
    def minimum(self, x = None):
        if x == None:
            x = self._root
        while x != None and x.getLeftSon() != None:
            x = x.getLeftSon()
        return x
    
    def maximum(self, x = None):
        if x == None:
            x = self._root
        while x != None and x.getRightSon() != None:
            x = x.getRightSon()
        return x
    
    def successor(self, k):
        if isinstance(k, int):
            x = self.search(k)
        else:
            x = k
        if x.getRightSon() != None:
            return self.minimum(x.getRightSon())
        y = x.getFather()
        while y != None and x == y.getRightSon():
            x = y
            y = y.getFather()
        return y
    
    def predecessor(self, k):
        if isinstance(k, int):
            x = self.search(k)
        else:
            x = k
        if x.getLeftSon() != None:
            return self.maximum(x.getLeftSon())
        y = x.getFather()
        while y != None and x == y.getLeftSon():
            x = y
            y = y.getFather()
        return y
    
    def inOrder(self, x):
        if x != None:
            self.inOrder(x.getLeftSon())
            print(x.getData())
            self.inOrder(x.getRightSon())
    
    def preOrder(self, x):
        if x != None:
            print(x.getData())
            self.preOrder(x.getLeftSon())
            self.preOrder(x.getRightSon())
            
    def postOrder(self, x):
        if x != None:
            self.postOrder(x.getLeftSon())
            self.postOrder(x.getRightSon())
            print(x.getData())
            
    def transplant(self, u, v):
        if u.getFather() == None:
            self._root = v
        elif u == u.getFather().getLeftSon():
            u.getFather().setLeftSon(v)
        else:
            u.getFather().setRightSon(v)
        if v != None:
            v.setFather(u.getFather())
    
    def deleteNode(self, k):
        x = self.search(k)
        if x.getLeftSon() == None:
            self.transplant(x, x.getRightSon())
        elif x.getRightSon() == None:
            self.transplant(x, x.getLeftSon())
        else:
            y = self.minimum(x.getRightSon())
            if y.getFather() != x:
                self.transplant(y, y.getRightSon())
                y.setRightSon(x.getRightSon())
                y.getRightSon().setFather(y)
            self.transplant(x, y)
            y.setLeftSon(x.getLeftSon())
            y.getLeftSon().setFather(y)
    
class RedBlackNode(Node):
    def __init__(self, data = None, red = True, father = None, leftSon = None, rightSon = None):
        Node.__init__(self, data, father, leftSon, rightSon)
        self._red = red
        
    def getRed(self):
        return self._red
    
    def setRed(self, newColor):
        self._red = newColor
    
class RedBlackTree(BinaryTree):
    def __init__(self):
        self._None = RedBlackNode(None, False)
        self._root = self._None
        self._aux = []
        
    def percorrer(self, x):
        if x != self._None:
            self._aux.append(x)
            self.percorrer(x.getLeftSon())
            self.percorrer(x.getRightSon())
        
    def minimum(self, x = None):
        if x == None:
            x = self._root
        while x != self._None and x.getLeftSon() != self._None:
            x = x.getLeftSon()
        return x
        
    def search(self, k):
        x = self._root
        while x != self._None and k != x.getData():
            if k < x.getData():
                x = x.getLeftSon()
            else:
                x = x.getRightSon()
        if x == self._None:
            return None
        else: return x
    
    def inOrder(self, x):
        if isinstance(x, int):
            x = self.search(x)
        if x != self._None:
            self.inOrder(x.getLeftSon())
            print(x.getData())
            self.inOrder(x.getRightSon())
            
    def preOrder(self, x):
        if isinstance(x, int):
            x = self.search(x)
        if x != self._None:
            print(x.getData())
            self.preOrder(x.getLeftSon())
            self.preOrder(x.getRightSon())
            
    def postOrder(self, x):
        if isinstance(x, int):
            x = self.search(x)
        if x != self._None:
            self.postOrder(x.getLeftSon())
            self.postOrder(x.getRightSon())
            print(x.getData())
        
    def leftRotate(self, x):
        y = x.getRightSon()
        x.setRightSon(y.getLeftSon())
        if y.getLeftSon() != self._None:
            y.getLeftSon().setFather(x)
        y.setFather(x.getFather())
        if x.getFather() == self._None:
            self._root = y
        elif x == x.getFather().getLeftSon():
            x.getFather().setLeftSon(y)
        else:
            x.getFather().setRightSon(y)
        y.setLeftSon(x)
        x.setFather(y)
        
    def rightRotate(self, x):
        y = x.getLeftSon()
        x.setLeftSon(y.getRightSon())
        if y.getRightSon() != self._None:
            y.getRightSon().setFather(x)
        y.setFather(x.getFather())
        if x.getFather() == self._None:
            self._root = y
        elif x == x.getFather().getRightSon():
            x.getFather().setRightSon(y)
        else:
            x.getFather().setLeftSon(y)
        y.setRightSon(x)
        x.setFather(y)
    
    def insert(self, z):
        newNode = RedBlackNode(z)
        y = self._None
        x = self._root
        while x != self._None:
            y = x
            if z < x.getData():
                x = x.getLeftSon()
            else:
                x = x.getRightSon()
        newNode.setFather(y)
        if y == self._None:
            self._root = newNode
        elif z < y.getData():
            y.setLeftSon(newNode)
        else:
            y.setRightSon(newNode)
        newNode.setLeftSon(self._None)
        newNode.setRightSon(self._None)
        self.insertFixup(newNode)
    
    def insertFixup(self, z):
        while z.getFather().getRed() == True:
            if z.getFather() == z.getFather().getFather().getLeftSon():
                y = z.getFather().getFather().getRightSon()
                if y.getRed() == True:
                    z.getFather().setRed(False)
                    y.setRed(False)
                    z.getFather().getFather().setRed(True)
                    z = z.getFather().getFather()
                else:  
                    if z == z.getFather().getRightSon():
                        z =  z.getFather()
                        self.leftRotate(z)
                    z.getFather().setRed(False)
                    z.getFather().getFather().setRed(True)
                    self.rightRotate(z.getFather().getFather())
            else:
                y = z.getFather().getFather().getLeftSon()
                if y.getRed() == True:
                    z.getFather().setRed(False)
                    y.setRed(False)
                    z.getFather().getFather().setRed(True)
                    z = z.getFather().getFather()
                else:  
                    if z == z.getFather().getLeftSon():
                        z =  z.getFather()
                        self.rightRotate(z)
                    z.getFather().setRed(False)
                    z.getFather().getFather().setRed(True)
                    self.leftRotate(z.getFather().getFather())
        self._root.setRed(False)
    
    def transplant(self, u, v):
        if u.getFather() == self._None:
            self._root = v
        elif u == u.getFather().getLeftSon():
            u.getFather().setLeftSon(v)
        else:
            u.getFather().setRightSon(v)
        v.setFather(u.getFather())
    
    def deleteNode(self, k):
        if k != RedBlackNode():
            k = self.search(k)
        y = k
        yoc = y.getRed()
        if k.getLeftSon() == self._None and k.getRightSon() != self._None:
            x = k.getRightSon()
            self.transplant(k, k.getRightSon())
        elif k.getRightSon() == self._None and k.getLeftSon() != self._None:
            x = k.getLeftSon()
            self.transplant(k, k.getLeftSon())
        elif k.getLeftSon() == self._None and k.getRightSon() == self._None:
            if k.getFather() == self._None:
                self._root = self._None
                x = False
            else:
                if k == k.getFather().getLeftSon():
                    x = k.getFather()
                    x.setLeftSon(self._None)
                else:
                    x = k.getFather()
                    x.setRightSon(self._None)
        else:
            y = self.minimum(k.getRightSon())
            yoc = y.getRed()
            x = y.getRightSon()
            if y.getFather() == k:
                x.setFather(y)
            else:
                self.transplant(y, y.getRightSon())
                y.setRightSon(k.getRightSon())
                y.getRightSon().setFather(y)
            self.transplant(k, y)
            y.setLeftSon(k.getLeftSon())
            y.getLeftSon().setFather(y)
            y.setRed(k.getRed())
        if yoc == False:
            if x != False:
                self.deleteFixup(x)
    
    def deleteFixup(self, x):
        while x != self._root and x.getRed() == False:
            if x == x.getFather().getLeftSon():
                w = x.getFather().getRightSon()
                if w.getRed() == True:
                    w.setRed(False)
                    x.getFather().setRed(True)
                    self.leftRotate(x.getFather())
                    w = x.getFather().getRightSon()
                if w.getLeftSon().getRed() == False and w.getRightSon().getRed() == False:
                    w.setRed(False)
                    x = x.getFather()
                else:
                    if w.getRightSon().getRed() == False:
                        w.getLeftSon().setRed(False)
                        w.setRed(True)
                        self.rightRotate(w)
                        w = x.getFather().getRightSon()
                        w.setRed(x.getFather().getRed())
                        x.getFather().setRed(False)
                    w.getRightSon().setRed(False)
                    self.leftRotate(x.getFather())
                    x = self._root
            else:
                w = x.getFather().getLeftSon()
                if w.getRed() == True:
                    w.setRed(False)
                    x.getFather().setRed(True)
                    self.rightRotate(x.getFather())
                    w = x.getFather().getLeftSon()
                if w.getRightSon().getRed() == False and w.getLeftSon().getRed() == False:
                    w.setRed(False)
                    x = x.getFather()
                else:
                    if w.getLeftSon().getRed() == False:
                        w.getRightSon().setRed(False)
                        w.setRed(True)
                        self.LeftRotate(w)
                        w = x.getFather().getLeftSon()
                        w.setRed(x.getFather().getRed())
                        x.getFather().setRed(False)
                    w.getLeftSon().setRed(False)
                    self.rightRotate(x.getFather())
                    x = self._root
        x.setRed(False)
        
    def enviar(self):
        return self._aux
    
    def limpar(self):
        self._aux = []

