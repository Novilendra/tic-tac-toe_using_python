import sys 
print("           Tik Toc Toe")
box = ["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-"]
def game():
    print("\n\n"+box[0]+" | "+box[1]+" | "+box[2])
    print(box[3]+" | "+box[4]+" | "+box[5])
    print(box[6]+" | "+box[7]+" | "+box[8])
game()
for i in range(9): 
    if i%2==0:
        print("            "+"player 1")
        print("Enter position from 1:9 : ")
        position = int(input())
        j = position
        if box[j-1] != "x" and box[j-1] != "o":
            box[j-1] = "x"
            game()
                          
        else:
            l=1
            while l < 5:
                print("Player 1 Enter position again from 1:9 this is already reserved : ")
                position = int(input())
                j = position
                if box[j-1] != "x" and box[j-1] != "o":
                    l= l+5
                    box[j-1] = "x"
                    game()
                    
                else :
                    l =1
                    game()
                        
                        
        if (box[0] == "x" and box[1] == "x" and box[2] == "x" ) or (box[0] == "x" and box[4] == "x" and box[8] == "x" ) or (box[0] == "x" and box[3] == "x" and box[6] == "x" )or (box[1] == "x" and box[4] == "x" and box[7] == "x" )or (box[2] == "x" and box[5] == "x" and box[8] == "x" ) or (box[6] == "x" and box[7] == "x" and box[8] == "x" ) or (box[2] == "x" and box[4] == "x" and box[6] == "x") or (box[3] == "x" and box[4] == "x" and box[5] == "x"):
            print("\n\nPlayer 1 Win !")
            break
                
           
    
    else:
        print("           "+"player 2")
        print("Enter postion from 1:9 : ")
        position = int(input())
        j = position
        if box[j-1] != "x" and box[j-1]!="o":
            box[j-1] = "o"
            game()
            
        else:
            k=1
            while k < 5:
                print("Player 2 Enter position again from 1:9 this is already reserved : ")
                position = int(input())
                j = position
                if box[j-1] != "x" and box[j-1] != "o":
                    k= k+5
                    box[j-1] = "o"
                    game()
                    
                else :
                    k =1
                    game()
                 
                 
        if (box[0] == "o" and box[1] == "o" and box[2] == "o" ) or (box[0] == "o" and box[4] == "o" and box[8] == "o" ) or (box[0] == "o" and box[3] == "o" and box[6] == "o" )or (box[1] == "o" and box[4] == "o" and box[7] == "o" )or (box[2] == "o" and box[5] == "o" and box[8] == "o" ) or (box[6] == "o" and box[7] == "o" and box[8] == "o" ) or (box[2] == "o" and box[4] == "o" and box[6] == "o" )or (box[3] == "o" and box[4] == "o" and box[5] == "o" ):
            
            print("\n\nPlayer 2 Win !")
            break
            
                
    if i==9:
        print("\n\n                 Game Tie")
        break
        print("Time")
print("Press N to exit : ")
check = input()
if check == "n":
    print("Thank You!")
    quit()
    

        