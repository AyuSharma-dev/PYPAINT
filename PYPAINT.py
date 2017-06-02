from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
global k
from PIL import Image, ImageDraw,ImageTk
k=0


########color functions#######

def black():
    global wid,colorr
    colorr = 'black'
    drawing_area.bind("<Motion>",lambda event: motion(event,'black',wid))
def darkgray():
    global wid,colorr
    colorr = 'darkgray'
    drawing_area.bind("<Motion>",lambda event: motion(event,'darkgray',wid))
def darkred():
    global wid,colorr
    colorr = 'darkred'
    drawing_area.bind("<Motion>",lambda event: motion(event,'darkred',wid))
def red():
    global wid,colorr
    colorr = 'red'
    drawing_area.bind("<Motion>",lambda event: motion(event,'red',wid))
def orange():
    global wid,colorr
    colorr = 'orange'
    drawing_area.bind("<Motion>",lambda event: motion(event,'orange',wid))
def yellow():
    global wid,colorr
    colorr = 'yellow'
    drawing_area.bind("<Motion>",lambda event: motion(event,'yellow',wid))
def darkgreen():
    global wid,colorr
    colorr = 'darkgreen'
    drawing_area.bind("<Motion>",lambda event: motion(event,'darkgreen',wid))
def turquoise():
    global wid,colorr
    colorr = 'turquoise'
    drawing_area.bind("<Motion>",lambda event: motion(event,'turquoise',wid))
def indigo():
    global wid,colorr
    colorr = 'indigo'
    drawing_area.bind("<Motion>",lambda event: motion(event,'indigo',wid))
def purple():
    global wid,colorr
    colorr = 'purple'
    drawing_area.bind("<Motion>",lambda event: motion(event,'purple',wid))
def white():
    global wid,colorr
    colorr = 'white'
    drawing_area.bind("<Motion>",lambda event: motion(event,'white',wid))
def gray():
    global wid,colorr
    colorr = 'gray'
    drawing_area.bind("<Motion>",lambda event: motion(event,'gray',wid))
def lightgray():
    global wid,colorr
    colorr = 'lightgray'
    drawing_area.bind("<Motion>",lambda event: motion(event,'lightgray',wid))
def brown():
    global wid,colorr
    colorr = 'brown'
    drawing_area.bind("<Motion>",lambda event: motion(event,'brown',wid))
def lightgreen():
    global wid,colorr
    colorr = 'lightgreen'
    drawing_area.bind("<Motion>",lambda event: motion(event,'lightgreen',wid))
def gold():
    global wid,colorr
    colorr = 'gold'
    drawing_area.bind("<Motion>",lambda event: motion(event,'gold',wid))
def lightyellow():
    global wid,colorr
    colorr= 'lightyellow'
    drawing_area.bind("<Motion>",lambda event: motion(event,'lightyellow',wid))
def skyblue():
    global wid,colorr
    colorr = 'skyblue'
    drawing_area.bind("<Motion>",lambda event: motion(event,'skyblue',wid))
    print('sky')
def darkblue():
    global wid,colorr
    colorr = 'darkblue'
    drawing_area.bind("<Motion>",lambda event: motion(event,'darkblue',wid))
def pink():
    global wid,colorr
    colorr= 'pink'
    drawing_area.bind("<Motion>",lambda event: motion(event,'pink',wid))

def multi_color():
    global wid,colorr
    color,colorr = colorchooser.askcolor()
    drawing_area.bind("<Motion>",lambda event: motion(event,str(colorr),wid))

def multi_color2():
    global wid,colorr2,shape,colorr,wid
    color,colorr2 = colorchooser.askcolor()
    drawing_area.bind("<ButtonRelease-1>",lambda event: b1up(event,shap = shape,
                                                             color = colorr,wd=wid,color2=colorr2))

############################

def shadow_color():     ##Creating Shadow Color for Text
    global colorr3
    c,colorr3 = colorchooser.askcolor()

def line_width(val):        ##Getting Values From Slider For Width
    
    global wid,colorr,Ewid,shape
    wid = int(val)/5
    Ewid = int(val)/2
    drawing_area.bind("<Motion>",lambda event: motion(event,colorr,wd=wid))
    return wid

def News(event=' '):     ##Clear Canvas Objects
    mess = messagebox.askokcancel(title='Clear Screen',message='Are you sure want to clear the screen')
    if mess==1:
        drawing_area.delete('all')
        #IMAGE = Image.new("RGB", (1190, 590),'white')
        #IMA = Image.new("RGB", (1190, 590),'white')
        #imgh = IMAGE.paste(IMA,(0,0,1190,590))
        draw.rectangle([0,0,1190,590],'white')
def Undo(event = ' '):        ##Undo Canvas Objects
    c = drawing_area.find_all()
    if len(c) >0:
        drawing_area.delete(c[-1])

def opens(event= ' '):
    file = filedialog.askopenfilename()
    
    file1 = Image.open(file)
    if file1.size[0]>1190 and file1.size[1]<590:
        file1 = file1.resize((1190,file1.size[1]))
    if file1.size[1]>590 and file1.size[0]<1190:
        file1 = file1.resize((file1.size[0],590))
    if file1.size[0]>1190 and file1.size[1]>590:
        file1 = file1.resize((1190,590))
    imag = ImageTk.PhotoImage(file1)
    file1 = file1.convert('RGBA')

    iss = drawing_area.create_image(610,310,image = imag)
    
    #draw.bitmap((100,100),file1)
    IMAGE.paste(file1,(610-int(file1.size[0]/2),310-int(file1.size[1]/2)))
    win.mainloop()
    
def saves(event = ' '):
    global IMAGE
    filename= filedialog.asksaveasfilename()
    print(filename)
    IMAGE.save(str(filename)+'.jpg','JPEG')

###################
####Shapes#########
def Line():
    
    global shape,colorr,wid,colorr2
    shape = 'line'
    drawing_area.bind("<Motion>",lambda event: motion(event,colorr,wd=wid,sh='line'))
    
def Curve():

    global shape,colorr,wid,colorr2
    shape = 'curve'
    drawing_area.bind("<ButtonRelease-1>",lambda event: b1up(event,shap = 'curve',
                                                             color = colorr,wd=wid,color2=colorr2))

def Circle():

    global shape,colorr,wid,colorr2
    shape = 'circle'
    drawing_area.bind("<ButtonRelease-1>",lambda event: b1up(event,shap = 'square',
                                                             color = colorr,wd=wid,color2=colorr2))

def Square():

    global shape,colorr,wid,colorr2
    shape = 'square'
    drawing_area.bind("<ButtonRelease-1>",lambda event: b1up(event,shap = 'circle',
                                                             color = colorr,wd=wid,color2=colorr2))

def Triangle():

    global shape,colorr,wid,colorr2
    shape = 'polygon'
    drawing_area.bind("<ButtonRelease-1>",lambda event: b1up(event,shap = 'polygon',
                                                             color = colorr,wd=wid,color2=colorr2))

def Polygon4():

    global shape,colorr,wid,colorr2
    shape = 'polygon4'
    drawing_area.bind("<ButtonRelease-1>",lambda event: b1up(event,shap = 'polygon4',
                                                             color = colorr,wd=wid,color2=colorr2))

def Polygon5():

    global shape,colorr,wid,colorr2
    shape = 'polygon5'
    drawing_area.bind("<ButtonRelease-1>",lambda event: b1up(event,shap = 'polygon5',
                                                             color = colorr,wd=wid,color2=colorr2))

def Polygon6():
    print('hh')
    global shape,colorr,wid,colorr2
    shape = 'polygon6'
    drawing_area.bind("<ButtonRelease-1>",lambda event: b1up(event,shap = 'polygon6',
                                                             color = colorr,wd=wid,color2=colorr2))

def texts(xr=0,yr=0):       ##Giving Functionality to Text_tools
    
    enadisb(sta='normal')
    

    
    def shadow(x,y,text,textcolor,strcolor,style,biu,size):
        drawing_area.create_text(x+5,y,text=text,font=(style,size,biu),fill=strcolor)
        drawing_area.create_text(x,y,text=text,font=(style,size,biu),fill=textcolor)
        
    v1 = B.get()
    v2 = I.get()
    v3 =  U.get()
    txt = A.get()
    ft = a.get()
    siz = s.get()
    if ts.get()==1:
        if v1==1:
            if v2== 0 and v3==0:
                shadow(xr,yr,str(txt),colorr,colorr3,ft,'bold',siz)
            elif v2==1 and v3==1:
                shadow(xr,yr,str(txt),colorr,colorr3,ft,'bold  italic underline',siz)
            elif v2==1 and v3==0:
                shadow(xr,yr,str(txt),colorr,colorr3,ft,'bold  italic ',siz)
            elif v2==0 and v3==1:
                shadow(xr,yr,str(txt),colorr,colorr3,ft,'bold underline',siz)
        elif v2==1:
            if v1== 0 and v3==0:
                shadow(xr,yr,str(txt),colorr,colorr3,ft,'italic',siz)
            elif v1==0 and v3==1:
                shadow(xr,yr,str(txt),colorr,colorr3,ft,'italic underline',siz)
        elif v3 ==1:
            if v2== 0 and v1==0:
                shadow(xr,yr,str(txt),colorr,colorr3,ft,'underline',siz)
        else:
            shadow(xr,yr,str(txt),colorr,colorr3,ft,'normal',siz)
    else:
        if v1==1:
            if v2== 0 and v3==0:
                drawing_area.create_text(xr,yr,text=str(txt),fill=colorr,font=(ft,siz,'bold'))
            elif v2==1 and v3==1:
                drawing_area.create_text(xr,yr,text=str(txt),fill=colorr,font=(ft,siz,'bold italic underline'))
            elif v2==1 and v3==0:
                drawing_area.create_text(xr,yr,text=str(txt),fill=colorr,font=(ft,siz,'bold italic '))
            elif v2==0 and v3==1:
                drawing_area.create_text(xr,yr,text=str(txt),fill=colorr,font=(ft,siz,'bold underline'))
            
        elif v2==1:
            if v1== 0 and v3==0:
                drawing_area.create_text(xr,yr,text=str(txt),fill=colorr,font=(ft,siz,'italic'))
            elif v1==0 and v3==1:
                drawing_area.create_text(xr,yr,text=str(txt),fill=colorr,font=(ft,siz,'italic underline'))
            
        elif v3 ==1:
            if v2== 0 and v1==0:
                drawing_area.create_text(xr,yr,text=str(txt),fill=colorr,font=(ft,siz,'underline'))
        else:
            drawing_area.create_text(xr,yr,text=str(txt),fill=colorr,font=(ft,siz,))



def about():
    w = Tk()
    w.iconbitmap('Slytherin.ico')
    w.title('About')
    f = open('about.txt')
    label = Label(w,text = f.read(),font=('arial',13,'italic')).pack()
        
def tools():        ## Getting Values  From RadioButtons(Tools)
    
    global shape,colorr,wid,dr,cur
    v=to.get()
    if v==1:
        dr=1
    if v==2:
        dr=2
    if v==3:
        dr=3
    if v==4:
        dr=4
    if v==7:
        dr = 7

def motion(event,sharma,wd=5,sh='line',new ='no',image='' ):        ##Creating Motion Effects on Canvas
        
    global Xf,Yf,shape,cur,colorr,dr,unlist
    canvas = event.widget
    X = canvas.canvasx(event.x)
    Y = canvas.canvasy(event.y)
    if new=='new':
        canvas.delete('all')
    if new =='open':
        file = PhotoImage(image)
        canvas.create_image(Xf,Yf,image=file)
    try:
        if dr==1:
             canvas.config(cursor='@cursors/pencil.cur')
             drawing_area.focus_set()
        if dr==2:
            canvas.config(cursor='@cursors/eraser.cur')
            drawing_area.focus_set()
        if dr==3 or dr== 4:
            canvas.config(cursor='@cursors/brush.cur')
            drawing_area.focus_set()
        if to.get()==7:
            shape = ' '
            canvas.config(cursor='@cursors/cross.cur')
            
    except:
        pass
    
    if b1 == "down":
        if dr==2:
            shape = 'line'
            global xold, yold
            if xold is not None and yold is not None:
                    sharma='white'
                    event.widget.create_line(xold,yold,event.x,event.y,fill='white',width=wd*4,smooth=True)
                    draw.line(((xold,yold),(event.x,event.y)),(255,255,255),width=int(wd*4))
        if dr==1:
            global xold, yold
            if shape == 'line':
                if xold is not None and yold is not None:
                    sharma=colorr
                    event.widget.create_line(xold,yold,event.x,event.y,fill=sharma,width=wd,smooth=True)
                    draw.line(((xold,yold),(event.x,event.y)),sharma,width=int(wd))
                    
        if dr == 3:
            shape= 'line'
            global xold, yold
            if xold is not None and yold is not None:
                    sharma=colorr
                    event.widget.create_polygon(xold,yold,event.x,event.y,xold-10,yold-10,tags='delall',fill=sharma,width = wd,outline = sharma)
                   
        if dr == 4:
            shape ='line'
            global xold, yold
            if xold is not None and yold is not None:
                    WD = int(wd/3)
                    sharma=colorr
                    event.widget.create_oval(xold,yold,event.x,event.y,tags='delall',fill=sharma,width = wd,outline = sharma)
                    draw.ellipse([xold-WD,yold-WD,event.x+WD,event.y+WD],sharma)
        xold = event.x
        yold = event.y
        xm = win.winfo_pointerx()
        ym = win.winfo_pointery()
        
def b1down(event):   ## Creating Button Press Events
    
    global b1,Xf,Yf,shape,st,k
    k+=1
    canvas = event.widget
    xf = win.winfo_pointerx()
    yf = win.winfo_pointery()
    Xf= canvas.canvasx(event.x)
    Yf = canvas.canvasy(event.y)
    
    b1 = "down"
    if to.get() == 7:
        shape = 'no'
        texts(Xf,Yf)
    if k==1:
        global labelxy
        labelxy = Label(text = 'x: '+str(Xf)+'           y: '+str(Yf),font=('comicsansms',12,'bold'),bg='lightgray')
        labelxy.place(x=150,y=700)
    else:
        global labelxy
        labelxy.config(text = 'x: '+str(Xf)+'           y: '+str(Yf),bg='lightgray')

        
def b1up(event,shap,color,wd,color2='black'):   ## Creating Button Release Events
    global b1, xold, yold,Xf,Yf,shape
    canvas = event.widget
    xl = win.winfo_pointerx()
    yl = win.winfo_pointery()
    Xl= canvas.canvasx(event.x)
    Yl = canvas.canvasy(event.y)
    if shape == 'square':
        if xold is not None and yold is not None:
                    event.widget.create_rectangle(Xf,Yf,Xl,Yl,fill=color,width = wd,outline=color2)
                    draw.rectangle([Xf-wd,Yf-wd,Xl+wd,Yl+wd],color2)
                    draw.rectangle([Xf,Yf,Xl,Yl],color)
    if shape == 'curve':
        if xold is not None and yold is not None:
            wd2 = int(wd/2)
            points=[Xf,Yf,Xf+25,Yf-50,Xf+50,Yf,Xf+100,Yf+25,Xf+50,Yf+50,Xf+25,Yf+100,Xf,Yf+50,Xf-50,Yf+25]
            points2=[Xf-wd2,Yf-wd2,Xf+25,Yf-50-wd,Xf+50+wd2,Yf-wd2,Xf+100+wd,Yf+25,Xf+50+wd2,Yf+50+wd2,Xf+25,Yf+100+wd,Xf-wd2,Yf+50+wd2,Xf-50-wd,Yf+25]
            event.widget.create_polygon(points,fill=color,width = wd,outline=color2)
            draw.polygon(points2,color2)
            draw.polygon(points,color)
    if shape == 'circle':
        if xold is not None and yold is not None:
            event.widget.create_oval(Xf,Yf,Xl,Yl,fill=color,width = wd,outline=color2)
            draw.ellipse([Xf-wd,Yf-wd,Xl+wd,Yl+wd],color2)
            draw.ellipse([Xf,Yf,Xl,Yl],color)
    if shape == 'polygon':
        if xold is not None and yold is not None:
            
            print(Xf,Yf)
            print(Xl,Yl)
            event.widget.create_polygon([Xf,Yf,Xl-50,Yl-150,Xf-150, Yf-100],fill=color,width = wd,outline= color2)
            draw.polygon([(Xf+wd,Yf+wd),(Xl-50+wd,Yl-150+wd),(Xf-150-wd, Yf-100-wd)],color2)
            draw.polygon([(Xf,Yf),(Xl-50,Yl-150),(Xf-150, Yf-100)],color)
    if shape == 'polygon4':
        if xold is not None and yold is not None:
            points = [Xf,Yf,Xf+100, Yf+100,Xl,Yl,Xf-100,Yf+100]
            points2 = [Xf,Yf-wd,Xf+100+wd, Yf+100,Xl,Yl+wd,Xf-100-wd,Yf+100]
            
            event.widget.create_polygon(points,fill=color,width = wd,outline= color2)
            draw.polygon(points2,color2)
            draw.polygon(points,color)
    if shape == 'polygon5':
        wd2 = int(wd/2)
        if xold is not None and yold is not None:
            points = [Xf,Yf,Xf+100, Yf+50,Xl,Yl,Xl-100,Yl,Xf-100,Yf+50]
            points2 = [Xf,Yf-wd,Xf+100+wd, Yf+50-wd2,Xl+wd2,Yl+wd,Xl-100-wd2,Yl+wd,Xf-100-wd,Yf+50-wd2]
            event.widget.create_polygon(points,fill=color,width = wd,outline= color2)
            
            draw.polygon(points2,color2)
            draw.polygon(points,color)
    if shape == 'polygon6':
        wd2 = int(wd/2)
        if xold is not None and yold is not None:
            points = [Xf,Yf,Xf+100, Yf+50,Xl,Yl,Xl-100,Yl+50,Xl-200,Yl,Xf-100,Yf+50]
            points2 = [Xf,Yf-wd,Xf+100+wd, Yf+50-wd2,Xl+wd,Yl+wd2,Xl-100,Yl+50+wd,Xl-200-wd,Yl+wd2,Xf-100-wd,Yf+50-wd2]
            event.widget.create_polygon(points,fill=color,width = wd,outline= color2)
            print(Xf,Yf)
            print(Xl,Yl)
            draw.polygon(points2,color2)
            draw.polygon(points,color)
    b1 = "up"
    
    xold = None          
    yold = None

def labels():    ##Creating Labels and Icons
    h = 0
    h1 = 55
    h2 = 100
    listop = ['Clear','Open','Save','Undo']
    listL = ['Line','Circle','Square','Triangle','Polygon-4','Polygon-5','Polygon-6','Star']
    for txt in listL:
        label = Label(text = txt,font=('comicsansms',10)).place(x=0,y=70+h)
        h+=90
    rlist = ['Pencil','Eraser','Brushes','Text']
    for txt in rlist:
        label = Label(text = txt,font=('comicsansms',8)).place(x=1300,y=h1)
        h1 +=60
    for txt in listop:
        label = Label(text = txt,font=('comicsansms',10,'bold')).place(x=h2,y=50)
        h2 +=60

    label3 = Label(text = 'Color Palate',font = ('comicsansms',10,'bold')).place(x=580,y = 55)
    label6 = Label(text = 'Text Font',font = ('comicsansms',8)).place(x=1290,y = 360)
    label7 = Label(text = 'Text Size',font = ('comicsansms',8)).place(x=1290,y = 495)
    label4 = Label(text = 'More Colors',font = ('comicsansms',8,'bold')).place(x=825,y=50)
    label5 = Label(text = 'Width',font = ('comicsansms',8,'bold')).place(x=1080,y=50)
    label4 = Label(text = 'Outline',font = ('comicsansms',8,'bold')).place(x=915,y=50)
    label = Label(text = 'Shift+Z',font=('century',12,'underline'),fg='red').place(x = 330, y = 20)
    shadow_c = Label(win,text='Shadow ',font=('comicsansms',10,'bold')).place(x=1300,y=560)
    c_text = Label(win,text='Shadow Color ',font=('comicsansms',8,)).place(x=1290,y=640)

def enadisb(sta='normal'):      ##MAking text tools enable/disable
        
        entryfnt = Entry(win,textvariable=A,borderwidth=2,state=sta,takefocus=' ',width=10,fg='red',disabledforeground='black',
            font=('comicsansms'),highlightcolor='green',insertofftime=(80)) .place(x=1290,y=270)
        fnt = ttk.Combobox(win,textvariable=a,values=valu,state=sta,width=7,takefocus=' ').place(x=1290,y=335)
        siz = ttk.Combobox(win,textvariable=s,values = sizes,state=sta,width=5,takefocus=' ').place(x=1290,y=470)

#########Creating Canvas#########
        
win = Tk()
win.title('PYPAINT')
win.iconbitmap('PYICON.ico')
DspW = 1400
DspH = 900
win.geometry(str(DspW)+'x'+str(DspH)+'+100+100')

try:
    drawing_area = Canvas(win,bd = 7,bg = 'white',height = 590,width = 1190,
                          relief = 'groove',cursor =cur)
except :
    drawing_area = Canvas(win,bd = 10,bg = 'white',height = 590,width = 1190,
                          relief = 'groove',cursor = '@cursors/pencil.cur')   
drawing_area.place(x = 70,y = 80)

IMAGE = Image.new("RGB", (1190, 590),'white')
draw = ImageDraw.Draw(IMAGE)
#################################

##########Creating Drawing Tools  and Shapes###########

ts = IntVar()
to = IntVar()

new  = PhotoImage(file = 'icons/new.png')
new2  = PhotoImage(file = 'icons/ayush.png')
plus = PhotoImage(file = 'icons/plus.png')
minus = PhotoImage(file='icons/minus.png')
mplus = PhotoImage(file = 'icons/mplus.png')
mminus = PhotoImage(file='icons/mminus.png')
poly6 = PhotoImage(file = 'icons/poly6.gif')
poly4 = PhotoImage(file = 'icons/poly4.png')
poly5 = PhotoImage(file = 'icons/poly5.png')
circle = PhotoImage(file = 'icons/circle.png')
line = PhotoImage(file = 'icons/line.png')
triangle = PhotoImage(file = 'icons/triangle.png')
square = PhotoImage(file = 'icons/square.png')
curve = PhotoImage(file = 'icons/curve.png')
Pencil = PhotoImage(file = 'icons/pencil.png')
Eraser = PhotoImage(file = 'icons/eraser.png')
Bucket = PhotoImage(file = 'icons/bucket.png')
Brush = PhotoImage(file = 'icons/brush.png')
Text = PhotoImage(file = 'icons/text.png')
mcolor = PhotoImage(file = 'icons/colors.png')
openf = PhotoImage(file='icons/open.png')
savef = PhotoImage(file = 'icons/save.png')

ima2 = []
ima = []
Brushes = Brush.subsample(2,1)
label2 = Label(image=plus).place(x = 1200,y=-10)
label3 = Label(image=minus).place(x = 970,y=-10)

c = Checkbutton(win,text='Text ',font=('comicsansms',10,'bold'),variable=ts).place(x=1290,y=540)
b = Button(win,image=mcolor,command=shadow_color).place(x = 1300,y = 600)
imglist = [line,circle,square,triangle,poly4,poly5,poly6,curve]

for i,file in zip(range(8),imglist):
    locals()['im'+str(i)] = file.subsample(4,4)
    ima.append(locals()['im'+str(i)])
commands= [Line,Circle,Square,Triangle,Polygon4,Polygon5,Polygon6,Curve]
By = 0

for com,image in zip(commands,ima):
    b = Button(win,image=image,bd=4,command = com).place(x=0,y=10+By)
    By += 90

b1 = Radiobutton(win,image=Pencil,variable=to,value=1,bd=4,indicatoron=0,command = tools).place(x=1300,y=10)
b2 = Radiobutton(win,image=Eraser,variable=to,value=2,bd=4,indicatoron=0,command = tools).place(x=1300,y=70)
b3 = Radiobutton(win,image=Brushes,variable=to,value=3,bd=4,indicatoron=0,command = tools).place(x=1295,y=130)
b4 = Radiobutton(win,image=Brushes,variable=to,value=4,bd=4,indicatoron=0,command = tools).place(x=1320,y=130)
b2 = Radiobutton(win,image=Text,bd=4,variable=to,value=7,indicatoron=0,command = texts).place(x=1300,y=190)
b = Button(win,image = mcolor,bd=4,command = multi_color,compound='center').place(x=840,y =5)
b5 = Button(win,image = mcolor,bd=4,command = multi_color2,compound='center').place(x=920,y =5)

b = Button(win,image= new2,bd=4,command = Undo).place(x = 270,y = 0)
b = Button(win,image= new,bd=4,command = News).place(x = 90,y = 0)
b = Button(win,image= savef,bd=4,command = saves).place(x = 210,y = 0)
b = Button(win,image= openf,bd=4,command = opens).place(x = 150,y = 0)

##################SliDER######################

S = Scale(win,from_=0,to=100,orient = HORIZONTAL,bd=4,tickinterval=10,length=200,width=5,command= line_width).place(x=1000,y=-5)

##############################################

#################Menu#######################

mo = Menu()
f = Menu()
i = Menu()
o = Menu()
h = Menu()
Cp = BooleanVar()
Cp.set(True)
ws = BooleanVar()
sp = BooleanVar()
tl = BooleanVar()
mg = BooleanVar()
        
f.add_command(label = "new                shift+N",font = ("arial",10,"bold"),command=News)
f.add_command(label = "open              shift+O",font = ('comicsansms',10,'bold'),command=opens)
f.add_command(label = "save                shift+S",font = ('comicsansms',10,'bold'),command=saves)
f.add_command(label = "exit",font = ('comicsansms',10,'bold'),command=quit)

h.add_command(label = "about Paint",font = ('comicsansms',10,'bold'),command=about)

mo.add_cascade(label = "file",menu=f)
mo.add_cascade(label = "help",menu=h)

win.config(menu = mo)

##############################################

##########color palate##########################

colors1 = [black,darkgray,darkred,red,orange,yellow,darkgreen,turquoise,indigo,purple]
colors2 = [white,gray,lightgray,brown,lightgreen,gold,lightyellow,skyblue,darkblue,pink]
colorsA = ['black','darkgray','darkred','red','orange','yellow','darkgreen','turquoise','indigo','purple']
colorsB = ['white','gray','lightgray','brown','lightgreen','gold','lightyellow','skyblue','darkblue','pink']
w = 420
w1 = 420

for color,com in zip(colorsA,colors1):
    button = Button(bg = color,command =com,bd=4,height=1,width= 4).place(x=w,y=0)
    w += 40

for color,com in zip(colorsB,colors2):
    button2 = Button(bg =str(color),command =com,bd=4,height=1,width= 4).place(x=w1,y=25)
    w1 += 40

##############################################

########Binding Keys  Declaring Local Variables######

try:
    colorr='black'
    shape='line'
    colorr2='black'
    colorr3 = 'black'
    b1 = "up"
    xold, yold = None, None
    n = 0
    wid=0
    dr = 1
    drawing_area.focus_set()
    drawing_area.bind("<ButtonPress-3>", Undo)
    drawing_area.bind("<Shift-Z>", Undo)
    drawing_area.bind("<ButtonPress-2>", News)
    drawing_area.bind("<Shift-N>", News)
    drawing_area.bind("<Shift-S>", saves)
    drawing_area.bind("<Shift-O>", opens)
    drawing_area.bind("<Motion>", lambda event:motion(event,colorr,wid,shape))
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", lambda event:b1up(event,shape,colorr,wid,colorr2))

except:
        drawing_area.focus_set()
        drawing_area.bind("<ButtonPress-3>", Undo)
        drawing_area.bind("<Shift-Z>", Undo)
        drawing_area.bind("<ButtonPress-2>", News)
        drawing_area.bind("<Shift-N>", News)
        drawing_area.bind("<Shift-S>", saves)
        drawing_area.bind("<Shift-O>", opens)
        drawing_area.bind("<Motion>", lambda event:motion(event,colorr,wid,shape))
        drawing_area.bind("<ButtonPress-1>", b1down)
        drawing_area.bind("<ButtonRelease-1>", lambda event:b1up(event,shape,colorr,wid,colorr2))

###################################

########Creating Text Tools##############
a = StringVar()
s = IntVar()
A = StringVar()
B = IntVar()
I = IntVar()
U = IntVar()
valu = font.families()
sizes = [i for i in range(20,150,10) ]



bold = Checkbutton(win,text='B',font=('comicansms',10,'bold'),variable=B,indicatoron=0,width=2,height=1,bd = 4).place(x=1290,y=380)
ita = Checkbutton(win,text='I',font=('comicansms',10,'italic'),variable=I,indicatoron=0,width=2,height=1,bd=4).place(x=1320,y=380)
und = Checkbutton(win,text='U',font=('comicansms',10,'underline'),variable=U,indicatoron=0,width=2,height=1,bd=4).place(x=1305,y=415)
label = Label(win,text='Enter Text Here',fg = 'black',font=('comicsansms',8)).place(x= 1287,y=300)
       
###############################

labels()
enadisb()
win.mainloop()


