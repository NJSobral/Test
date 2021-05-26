from graphical_editor import Graphical_editor
import sys


if __name__ == "__main__":
    print("Welcome to Graphical Editor:\n")
    gp = Graphical_editor()
    
    while True:
        print("Enter a command to start(Enter C to reset the array and X to exit the program)")
        command = input("> ")
        args = command.split()
        
        if args[0] == "I":
            if(len(args)==3):
                if(1<=int(args[1])<=250 and 1<=int(args[2])<=250):
                    gp.imageMxN(int(args[1]), int(args[2]))
                else:
                    print("The M and N value must be between 1 and 250!!")
            else:
                print("Number of arguments does not satisfy any of the commands")
        elif args[0] == "L":
            if(len(args)==4):    
                if(1<=int(args[1])<=gp.cols and 1<=int(args[2])<=gp.rows):
                    gp.colorCoords(int(args[1]), int(args[2]), args[3])
                else:
                    str = "The coords of the pixels must be between 1 and the number of rows or cols\n"+"Your current image have "+ str(gp.cols)+ " columns and "+ str(gp.rows)+" rows."
                    print(str)
            else:
                print("Number of arguments does not satisfy any of the commands")
                
        elif args[0] == "V":
            if(len(args)==5):
                if(1<=int(args[1])<=gp.cols and 1<=int(args[2])<=int(args[3]) and int(args[2])<=int(args[3])<=gp.rows):
                    gp.verticalPaint(int(args[1]), int(args[2]), int(args[3]), args[4])
                else:
                    str = "The coords of the pixels must be between 1 and the number of rows or cols\n"+"Your current image have "+ str(gp.cols)+ " columns and "+ str(gp.rows)+" rows."
                    print(str,"Y2 must be greater than Y1!! ")
            else:
                print("Number of arguments does not satisfy any of the commands")   
        elif args[0] == "H":
            if(len(args)==5):
                if(1<=int(args[1])<=int(args[2]) and int(args[1])<=int(args[2])<=gp.cols and 1<=int(args[3])<=gp.rows):
                    gp.horizontalPaint(int(args[1]), int(args[2]), int(args[3]), args[4])
                else:
                    str = "The coords of the pixels must be between 1 and the number of rows or cols\n"+"Your current image have "+ str(gp.cols)+ " columns and "+ str(gp.rows)+" rows."
                    print(str, "X2 must be greater than X1!!")
            else:
                print("Number of arguments does not satisfy any of the commands")
        elif args[0] == "F":
            if(len(args)==4):
                if(1<=int(args[1])<=gp.cols and 1<=int(args[2])<=gp.rows):
                    gp.fillRegion(int(args[1]), int(args[2]), args[3])
                else:
                    str = "The coords of the pixels must be between 1 and the number of rows or cols.\n"+"Your current image have "+ str(gp.cols)+ " columns and "+ str(gp.rows)+" rows."
                    print(str)
            else:
                print("Number of arguments does not satisfy any of the commands")  
        elif args[0] == "S":
            gp.show()
        elif args[0] == "C":
            gp.clear()
        elif args[0] == "X":
            sys.exit()
