# Draw a game board
#Assumption: Board is always a square since nothing is specified
def draw_height(heightinp): #Function to draw vertical lines of board
    print("|   " * (heightinp+1))

def draw_width(widthinp):   #Function to draw horizontal lines of board
    print (" ---" * (widthinp))

def board_draw(heightinp,widthinp):
    if(heightinp == widthinp):  #To check if the board is square
        i=1
        while i<=heightinp: #keep looping till it reaches board size
            draw_width(widthinp)    #Call function to draw horizontal lines of the current row
            draw_height(heightinp)  #Call function to draw vertical lines of the current row
            i = i + 1   #To draw the second row of the board
        draw_width(widthinp)    #Draw horizontal border at the end to close the board
    else:
        print("Enter board size of same size")  #print if width and height are not same

#Enter height and width of the board

heightinp= int(input("Enter the height of the board: "))
widthinp= int(input("Enter the width of the board: "))
board_draw(heightinp,widthinp)  #call board_draw to draw a board
