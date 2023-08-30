from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergersort import merge_sort


root = Tk()
root.title('Algorithm Simulator')
root.geometry('900x600+200+80')
root.config(bg='#082A46')
data = []

def drawData(data,colorArray):

    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data)+1) #gives spacing for the bar plots
    offset = 10
    spacing_bet_rect = 10
    normalised_data = [i / max(data) for i in data]


#we have multiplied 400 as we will normalise our values 
#one formula so that our data will not exceed our canvas

    for i, height in enumerate(normalised_data):
        x0 = i*x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400

        x1 = (i+1) * x_width
        y1 = canvas_height

        canvas.create_rectangle(x0, y0,x1,y1, fill= colorArray[i])
        canvas.create_text(x0+2 , y0 , anchor=SW , text=str(data[i]),font=("new roman",15,"bold"),
                            fill="orange")

    root.update_idletasks()

def StartAlgorithm():
    global data
    if not data:
        return
    
    if(algo_menu.get() == 'Quick Sort'):
       quick_sort(data, 0, len(data)-1, drawData, speedscale.get())
      
    elif algo_menu.get() == "Bubble Sort":
        bubble_sort(data, drawData, speedscale.get())

    elif algo_menu.get() == "Merge Sort":
        merge_sort(data, drawData, speedscale.get())
    drawData(data, ['green' for x in range(len(data))])



#function to GET the selected algorithm 
def Generate():

    global data
    print('Selected Algorithm: '+selected_algorithm.get())

   #we will take values from our MIN-VALUE scale    
    minivalue = int(minvalue.get())
    #we will take values from our MAX-VALUE scale  
    maxivalue = int(maxvalue.get())   
    #we will take values from our SIZE-VALUE scale   
    sizeevalue = int(sizevalue.get())


    data = []
    for _ in range(sizeevalue):
        #we will add that speed scale by appending it 
        data.append(random.randrange(minivalue,maxivalue+1))   

    drawData(data,['#A90042' for x in range(len(data))])



selected_algorithm = StringVar()

#header laber - SORTING ALGORITHM
header = Label(text="SORTING ALGORITHMS", width=105,font=("new roman",10,"bold"))
#header position
header.place(x=20,y=5)

#Label - ALGORITHM 
mainlabel = Label(root, text="Algorithm : ", font = ("new roman",10,"bold"),bg = "white",width="10", fg="black",relief=GROOVE, bd = 5)
#Label - ALGORITHM position
mainlabel.place(x=20,y=30)

#Combobox Label - sorting algorithms list
algo_menu = ttk.Combobox(root, width=15, font = ("new roman",10,"bold"),textvariable=selected_algorithm,
                         values=['Bubble Sort','Merge Sort','Quick Sort'])
#Combobox Label - sorting algorithms list position
algo_menu.place(x=120,y = 30)

algo_menu.current(0)#by default bubble sort

#Random number generator
random_generate = Button(root,text="Generate",bg="#40E0D0",font=("ariel",10,"bold"),relief = SUNKEN,
                         activebackground="#05945B",activeforeground="white",bd=2,width=10,command=Generate)
random_generate.place(x=740,y=75)

#slider Scale - Size
sizevaluelabel = Label(root,text="Size: ",font=("new roman",10,"bold"),
                         bg = "#40E0D0",width="10", height=2,fg="black",relief=GROOVE, bd = 5)
sizevaluelabel.place(x=20,y=80)

sizevalue = Scale(root,from_=0, to=30,resolution=1,orient = HORIZONTAL, font=("arial",10,"bold"),relief=GROOVE,bd=2,width=10)
sizevalue.place(x=120,y=80)

# slider Scale - Min Value
minvaluelabel = Label(root,text="Min Value: ",font=("new roman",10,"bold"),
                         bg = "#40E0D0",width="10", height=2,fg="black",relief=GROOVE, bd = 5)
minvaluelabel.place(x=240,y=80)

minvalue = Scale(root,from_=0, to=10,resolution=1,orient = HORIZONTAL, font=("arial",10,"bold"),relief=GROOVE,bd=2,width=10)
minvalue.place(x=340,y=80)


# slider Scale - Max Value
maxvaluelabel = Label(root,text="Max Value: ",font=("new roman",10,"bold"),
                         bg = "#40E0D0",width="10", height=2,fg="black",relief=GROOVE, bd = 5)
maxvaluelabel.place(x=460,y=80)

maxvalue = Scale(root,from_=0, to=100,resolution=1,orient = HORIZONTAL, font=("arial",10,"bold"),relief=GROOVE,bd=2,width=10)
maxvalue.place(x=560,y=80)

#START btn to begin the sorting
start = Button(root,text="Start",bg="#40E0D0",font=("ariel",10,"bold"),relief = SUNKEN,
                         activebackground="#40E0D0",activeforeground="#DE3163",bd=2,width=10, command=StartAlgorithm)
start.place(x=740,y=35)

#SPEED of sorting value
speedlabel = Label(root,text="Speed: ",font=("new roman",10,"bold"),
                         bg = "#40E0D0",width="10", height=2,fg="black",relief=GROOVE, bd = 5)
speedlabel.place(x=256,y=30)

speedscale = Scale(root,from_= 0.1, to = 5.0, resolution = 0.2, length = 200, digits= 2,orient = HORIZONTAL, font=("arial",10,"bold"),relief=GROOVE,bd=2,width=10)
speedscale.place(x=356,y=30)

canvas = Canvas(root, width=870,height=450,bg="black")
canvas.place(x=10,y=130)



root.mainloop()