from tkinter import *
root=Tk()
root.geometry('700x1400')
class c:
    
    b=0#for alternating button values
    d=0#for stoping multiple winner
    w=None#for tracking winner 
    def turn(event):
        d=event.widget
        val=d["text"]
        if (val=="" and c.d==0):
            if (c.b==0):
                if c.w==0:
                    d.config(text="O")#if O win first then start with O
                elif c.w==1:
                    d.config(text="X")#if X win first then start with X
                else:
                    d.config(text="X")#game start with x
                c.b=1#use for alternate values on button i.e x or o
            else:
                if c.w==0:
                    
                    d.config(text="X")
                elif c.w==1:
                    d.config(text="O")
                else:
                     
                    d.config(text="O")
                c.b=0
            
            if (b1["text"]==b2["text"] and b2["text"]==b3["text"] and not b1["text"]=="" ):
               
               b1.config(bg="lightgreen")
               b2.config(bg="lightgreen")
               b3.config(bg="lightgreen")
               if b1["text"]=="X":
                   
                   c.w=1#if X win then first step took by x
                   l2.config(text=b1["text"]+" player"+" wins")
               else:
                   c.w=0 #if O win then first step took by O
                   l2.config(text=b1["text"]+" player"+" wins")
                   
               c.disable()
               c.d=1
            elif (b4["text"]==b5["text"] and b6["text"]==b5["text"] and not b4["text"]==""):
                
            
               b5.config(bg="lightgreen")
               b6.config(bg="lightgreen")
               b4.config(bg="lightgreen")
               if b4["text"]=="X":
                   c.w=1
                   l2.config(text=b4["text"]+" player"+" wins")
               else:
                   c.w=0
                   l2.config(text=b4["text"]+" player"+" wins")
            
                      
               
               c.disable()
               c.d=1
               
            elif (b2["text"] ==b5["text"] and b5["text"]== b8["text"] and not b2["text"]=="" ):
               b5.config(bg="lightgreen")
               b2.config(bg="lightgreen")
               b8.config(bg="lightgreen")
               if b2["text"]=="X":
                   c.w=1
                   l2.config(text=b2["text"]+" player"+" wins")
               else:
                   c.w=0
                   l2.config(text=b2["text"]+" player"+" wins")               
               
               c.disable()
               c.d=1
               
               
           
            elif (b7["text"]==b8["text"] and b8["text"]==b9["text"] and not b7["text"]=="" ):
               b7.config(bg="lightgreen")
               b8.config(bg="lightgreen")
               b9.config(bg="lightgreen")
               if b7["text"]=="X":
                   c.w=1
                   l2.config(text=b7["text"]+" player"+" wins")
               else:
                   c.w=0
                   l2.config(text=b7["text"]+" player"+" wins")
               
              
               c.disable()
               c.d=1
               
            
            elif (b1["text"]==b5["text"] and b5["text"] ==b9["text"]and not b9["text"]=="" ):
               b1.config(bg="lightgreen")
               b5.config(bg="lightgreen")
               b9.config(bg="lightgreen")
               if b1["text"]=="X":
                   c.w=1
                   l2.config(text=b1["text"]+" player"+" wins")
               else:
                   c.w=0
                   l2.config(text=b1["text"]+" player"+" wins")
               
               
               c.disable()
               c.d=1
               
            elif (b7["text"]==b5["text"]and b5["text"]==b3["text"] and not b7["text"]=="" ):
               b7.config(bg="lightgreen")
               b5.config(bg="lightgreen")
               b3.config(bg="lightgreen")
               
               if b7["text"]=="X":
                   c.w=1
                   l2.config(text=b7["text"]+" player"+" wins")
               else:
                   c.w=0
                   l2.config(text=b7["text"]+" player"+" wins")
               c.disable()
               c.d=1
               
            elif (b3["text"] ==b6["text"]and b6["text"] ==b9["text"]and not b6["text"]=="" ):
               b6.config(bg="lightgreen")
               b3.config(bg="lightgreen")
               b9.config(bg="lightgreen")
               
               if b3["text"]=="X":
                   c.w=1
                   l2.config(text=b3["text"]+" player"+" wins")
               else:
                   c.w=0
                   l2.config(text=b3["text"]+" player"+" wins")
               c.disable()
               c.d=1
               
            if (b1["text"]==b4["text"] and b4["text"] ==b7["text"] and not b7["text"]=="" ):
               b1.config(bg="lightgreen")
               b7.config(bg="lightgreen")
               b4.config(bg="lightgreen")
               if b1["text"]=="X":
                   c.w=1
                   l2.config(text=b1["text"]+" player"+" wins")
               else:
                   c.w=0
                   l2.config(text=b1["text"]+" player"+" wins")
               c.disable()
               c.d=1
           
           
           
           
            
            
           
           
           
            
           
               
               
               
    def clear(event):
        
        c.b=0
        c.d=0
        b1.config(text="",bg="black")
        b2.config(text="",bg="black")
        b3.config(text="",bg="black")
        b4.config(text="",bg="black")
        b5.config(text="",bg="black")
        b6.config(text="",bg="black")
        b7.config(text="",bg="black")
        b8.config(text="",bg="black")
        b9.config(text="",bg="black")
        l2.config(text="")
        b1.config(state="normal")
        b2.config(state="normal")
        b3.config(state="normal")
        b4.config(state="normal")
        b5.config(state="normal")
        b6.config(state="normal")
        b7.config(state="normal")
        b8.config(state="normal")
        b9.config(state="normal")
   
        
      
    def disable():
         
         
         b1.config(state="disabled")
         b2.config(state="disabled")
         b3.config(state="disabled")
         b4.config(state="disabled")
         b5.config(state="disabled")
         b6.config(state="disabled")
         b7.config(state="disabled")
         b8.config(state="disabled")
         b9.config(state="disabled")
         
        
        
        




Label(root,text="Tic Tac Toe ",fg="brown", font=("arial",19)).place(x=180,y=20)
l2=Label(root,font=("arial",10))
l2.place(x=250,y=150)




b1=Button(root,text="" ,width=8,fg="yellow",bg="black",borderwidth=10,highlightbackground="red",height=6)
b1.place(x=7,y=250)

b2=Button(root,text="" ,width=8,fg="yellow",borderwidth=10,highlightbackground="red",bg="black", height=6 )

b2.place(x=239,y=250)

b3=Button(root,text="" ,width=8,fg="yellow",borderwidth=10,highlightbackground="red",bg="black", height=6 )

b3.place(x=472,y=250)



b4=Button(root,text="" ,borderwidth=10,highlightbackground="red",width=8,fg="yellow",bg="black", height=6 )

b4.place(x=7,y=520)

b5=Button(root,text="" ,borderwidth=10,highlightbackground="red",width=8,fg="yellow",bg="black", height=6 )

b5.place(x=239,y=520)

b6=Button(root,text="" ,borderwidth=10,highlightbackground="red",width=8,fg="yellow",bg="black", height=6 )

b6.place(x=472,y=520)

b7=Button(root,text="" ,borderwidth=10,highlightbackground="red",width=8,fg="yellow",bg="black", height=6 )

b7.place(x=7,y=790)

b8=Button(root,text="" ,borderwidth=10,highlightbackground="red",width=8,fg="yellow",bg="black", height=6 )

b8.place(x=239,y=790)

b9=Button(root,text="" ,borderwidth=10,highlightbackground="red",width=8,fg="yellow",bg="black", height=6 )

b9.place(x=472,y=790)

b10=Button(root,text="Restart",width=8,fg="yellow",bg="green",height=3)
b10.place(x=239,y=1100)

b1.bind("<Button-1>",c.turn)
b2.bind("<Button-1>", c.turn)
b3.bind("<Button-1>",c.turn)
b4.bind("<Button-1>", c.turn)
b5.bind("<Button-1>",c.turn)
b6.bind("<Button-1>", c.turn)
b7.bind("<Button-1>",c.turn)
b8.bind("<Button-1>", c.turn)
b9.bind("<Button-1>",c.turn)
b10.bind("<Button-1>", c.clear)
root.mainloop()