from array import *

class Graphical_editor:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.img = None

    def imageMxN(self, M , N):
        self.cols = M
        self.rows = N
        self.img = [['O' for j in range(self.cols)] for i in range(self.rows)]

    def clear(self):
        rows = len(self.img)
        cols = len(self.img[0])
        size = (rows * cols)
        tam = "cols : "+str(cols)+", rows: "+ str(rows) + " and size : "+ str(size)
        self.img = [['O' for j in range(cols)] for i in range(rows)]

    def colorCoords(self, coordsX, coordsY, c):
        image = self.img
        image[coordsY-1][coordsX-1] = c
        self.img = image

    def verticalPaint(self, X, Y1, Y2, C ):
        image = self.img
        for i in range(self.rows):
            for j in range(self.cols):
                if( Y1-1 <= i <= Y2-1 ):
                    if (j == X-1):
                        image[i][j] = C
        self.img = image

    def horizontalPaint(self, X1, X2, Y, C ):
        image = self.img
        for i in range(self.rows):
            for j in range(self.cols):
                if (i == Y-1):
                    if( X1-1 <= j <= X2-1 ):
                        image[i][j] = C
        self.img = image

    def checkNeighbor(self, image, i , j, temp):
        if(i+1 < self.rows and image[i+1][j]==temp):
            image[i+1][j]=image[i][j]
            self.checkNeighbor(image, i+1, j, temp)    
            
        if(i-1 >= 0 and image[i-1][j]==temp):
            image[i-1][j]=image[i][j]    
            self.checkNeighbor(image, i-1, j, temp)    
                
            
        if(j-1 >= 0 and image[i][j-1]==temp):
            image[i][j-1]=image[i][j]    
            self.checkNeighbor(image, i, j-1, temp)    
            
                
        if (j+1 < self.cols and image[i][j+1]==temp):
            image[i][j+1]=image[i][j] 
            self.checkNeighbor(image, i, j+1, temp)    
               

    def fillRegion(self, X, Y , C):
        image = self.img
        for i in range(self.rows):
            for j in range(self.cols):
                if (i == Y-1 and j == X-1):
                    temp = image[i][j]
                    image[i][j] = C
                    self.checkNeighbor(image, i, j, temp)   


    def show(self):
        print("=>")
        for r in self.img:
            for c in r:
                print(c, end=" ")
            print()
