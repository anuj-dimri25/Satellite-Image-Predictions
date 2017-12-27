import tkMessageBox
import tkFileDialog
import ImageTk
from Tkinter import *
import os
import math
from tkFileDialog import askopenfilename
from PIL import ImageTk, Image

#FUNCTION TO VIEW IMAGE IN CANVAS WITH SCROLLBARS
def viewimg(filenameview):
    
    root32=Toplevel()
    #OPENING THE IMAGE
    im22=Image.open(filenameview)
    img = ImageTk.PhotoImage(im22)
    #pix22=im22.load()
    print filenameview,"in view"
    #MAKING FRAME AND CANVAS AND ADDING SCROLLBARS
    frame=Frame(root32,width=3000,height=3000)
    frame.grid(row=0,column=0)
    canvas=Canvas(frame,bg='#FFFFFF',width=1500,height=1500,scrollregion=(0,0,img.width(),img.height()))
    hbar=Scrollbar(frame,orient=HORIZONTAL)
    hbar.pack(side=BOTTOM,fill=X)
    hbar.config(command=canvas.xview)
    vbar=Scrollbar(frame,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=canvas.yview)
    canvas.config(width=700,height=500)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack(side=LEFT,expand=True,fill=BOTH)
    
    print filenameview
    print img.width(),img.height()
    canvas.create_image(00,00, anchor=NW, image=img)
    root32.mainloop()


#FUNCTION TO VIEW IMAGE IN CANVAS WITH SCROLLBARS AND RENAMING THE FILE
def viewimg22(filename1,filename2):
    
    root32=Toplevel()
    #RENAMING THE FILE
    #filename2 IS GIVEN BY USER
    os.rename(filename1,filename2)
    im21=Image.open(filename2)

    img = ImageTk.PhotoImage(im21)
    
    #MAKING FRAME AND CANVAS AND ADDING SCROLLBARS
    frame=Frame(root32,width=3000,height=3000)
    frame.grid(row=0,column=0)
    canvas=Canvas(frame,bg='#FFFFFF',width=1500,height=1500,scrollregion=(0,0,img.width(),img.height()))
    hbar=Scrollbar(frame,orient=HORIZONTAL)
    hbar.pack(side=BOTTOM,fill=X)
    hbar.config(command=canvas.xview)
    vbar=Scrollbar(frame,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=canvas.yview)
    canvas.config(width=700,height=500)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack(side=LEFT,expand=True,fill=BOTH)
    
    print filename2
   
    print img.width(),img.height()
    canvas.create_image(00,00, anchor=NW, image=img)
    root32.mainloop()



'''#DEFINING THE MAIN WINDOW
global root1
root1=Tk()
root1.geometry('1300x1000')#SIZE OF WINDOW
root1.configure(background="#9999ff")'''


#MARKOV PREDICTION
def displaying1():
    '''#execfile('guiprediction.py')
    #DEFINING PREDICTION WINDOW
    global root
    root=Tk()
    root.title('MARKOV PREDICTIVE ANALYSIS')
    root.geometry('800x900')#SIZE OF WINDOW
    scrollbar=Scrollbar(root)
    root.configure(background="#9999ff")
    scrollbar.pack(side=RIGHT, fill=Y)
    filename1=""
    filename2=""'''
    
    #FUNCTION TO INPUT THE IMAGES FOR PREDICTION
    def inputfile1():
        #newimgw=Toplevel(root)
        print 'fgh'
        #INPUT IMAGE 1
        filename1 = askopenfilename()
        print filename1
        #LABEL TO PRINT THE FILENAME OF THE INPUT IMAGE ON SCREEN
        Label(root, text='Input image1 ->'+filename1,font=('Arial',14)).pack(padx=5, pady=5)
        #INPUT IMAGE 2
        filename2 = askopenfilename()
        print filename2
        #LABEL TO PRINT THE FILENAME OF THE INPUT IMAGE ON SCREEN
        Label(root, text='Input image2 ->'+filename2,font=('Arial',14)).pack(padx=5, pady=5)

        #LABEL AND ENTRY TO ASK YEAR OF PREDICITON
        l1=Label(root,text="Enter the year of prediction",font=('Arial',15))
        l1.pack(side=LEFT)
        l1.place(x=140,y=290)
        E10=Entry(root,font=('Arial',15),bd=5)
        E10.pack(side=RIGHT)
        E10.place(x=390,y=290)
        predy=E10.get()
        print predy
        
            
        #BUTTON TO START THE PREDICTION,IT CALLS predict(,,) FUNCTION
        B3 = Button(root, text ="START PREDICTION",font=('Arial',18),command=lambda:predict(filename1,filename2,E10.get()))
        B3.pack(padx=5, pady=5)
        B3.place(x=180,y=350)

        
 
    #THIS FUNCTION IS USED TO PREDICT THE IMAGE
    #filename1 is input image1
    #filename2 is input image2
    #predy is the predicito9n year

    def predict(filename1,filename2,predy):
      print filename1,'gfhh6'
      print 'in prediction'
      print 'in fxn',predy
      #name of output image
      outputfile=E1.get()
      print outputfile,'output'
      #print 'e10 called',E10.get()

      #OPENING AND LOADING FIRST IMAGE
      im=Image.open(filename1)
      pix=im.load()
      print pix[200,200]

      #OPENING AND LOADING SECOND IMAGE
      im2=Image.open(filename2)
      pix2=im2.load()
      print pix2[200,200]
      #tkimage = ImageTk.PhotoImage(im2)
      #Label(newimgw, image=tkimage).pack()

      
      #############countdown ###########
      '''for t in range(400, -1, -1):
            # format as 2 digit integers, fills with zero to the left
            # divmod() gives minutes, seconds
            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
            print(sf)  # test
            time_str.set(sf)
            root.update()
            # delay one second
            time.sleep(1)'''




      #CREATING NEW IMAGE
      imgnew = Image.new( 'P', (1010,1118), 0)
      #MODE P IS FOR PALETTE WHICH STORES THE COLOURS WITH INDEX STARTING FROM 0
      imgnew.putpalette([
          0, 0, 0, # black background
          45, 138, 86, # index 1 is darkgreen
          0, 254, 0, # index 2 is lightgreen
          254, 254, 0, # index 3 is yellow
          0,0,254,# index 4 is yellow
          254,0,254,# index 5 is magenta
          254,254,254# index 6 is white
      ])
      #LOADING THE IMAGE
      pixels=imgnew.load()
      #DECLARATION OF VARIABLES
      x=0
      y=0
      j=0
      k=0
      l=0
      #print im.size #Get the width and height of the image for iterating over
      #w contains width and h contains height
      w=int(im.size[0])
      #print w
      h=int(im.size[1])
      #print h
      #print 'hiii'
      #print pix[200,241]
      pix_02=[] # list for FIRST image
      pix_13=[] # list for SECOND image
      obs=[]
      maxi=0
      a=[[0],[0],[0],[0],[0],[0]]
      ############################################################333333333pi########################################
      # setting initial parameters to 0
      #dv=dense forest dark green and is denoted by 1
      #of=open forest light green and is denoted by 2
      #ag=agricultural land yellow and is denoted by 3
      #ri=dry river bed blue and is denoted by 4
      #ub=urban magenta and is denoted by 5
      #bl=barren land white and is denoted by 6 
      dv=0
      of=0
      ag=0
      bl=0
      ub=-296105#THIS IS DONE AS BORDER AREAS HAVE CHANGED TO URBANLAND...IT SHOULD BE ZERO IF BORDER AREA IS BLACK
      ri=0
      count=[]
      count1=[]
      c=0#for observation matrix
      #LOOPING ACROSS THE ENTIRE IMAGE
      while x < w:
          pix_02.append([])
          y=0
          while y < h:
              #print pix[x,y]
              r=pix[x,y]
              #g=pix[x,y][1]
              #b=pix[x,y][2]
              if (r==1):#dark green
                  pix_02[x].append(1)
                  dv+=1
              elif (r==2) : #light green 
                  pix_02[x].append(2)
                  of+=1
              elif (r==3) :#yellow
                  pix_02[x].append(3)
                  ag+=1
              elif (r==4) :#blue
                  pix_02[x].append(4)
                  ri+=1
              elif (r==5) :#magenta
                  pix_02[x].append(5)
                  ub+=1
              elif(r==6) :#white
                  pix_02[x].append(6)
                  bl+=1
              else:#black pixel....not under consideration 
                  pix_02[x].append(0)
              y=y+1
          x=x+1
      #print len(pix_02)
      #print len(pix_02[0])
      #print hv,of,sc,ag,ri,op
      tot=float(dv+of+bl+ag+ub+ri)
      #count is a list containing sum of all LULC
      count=[dv,of,bl,ag,ub,ri]
      #calculating probability
      pi=[dv/tot,of/tot,bl/tot,ag/tot,ub/tot,ri/tot]
      #pi is a stochastic initial matrix of order 1*6
      #print pi
          

      #pit is the transpose of pi...hence its order is 6*1
      pit=[]
      pit.append([])
      pit[0].append(pi[0])
      pit.append([])
      pit[1].append(pi[1])
      pit.append([])
      pit[2].append(pi[2])
      pit.append([])
      pit[3].append(pi[3])
      pit.append([])
      pit[4].append(pi[4])
      pit.append([])
      pit[5].append(pi[5])
      print 'in transpose'
      #print pit
      #print pix_02
           #while x<w:
       #   while y<h:
        #      print pix_02[x,y],
         #     y=y+1
          #print ''
          #x=x+1
      #print ''

      ##########################################################333pi2##################################################3

      #calculating initial matrix with respect to SECOND image    
      dv1=0
      of1=0
      bl1=0
      ag1=0
      ub1=0
      ri1=-296105
      x=0
      y=0
      r1=0
      g1=0
      b1=0
      while x < w:
          #print 'out loop'
          pix_13.append([])
          y=0
          while y < h:
              #print 'inner'
              r1=pix2[x,y]
              #g1=pix2[x,y][1]
              #b1=pix2[x,y][2]
              #print pix[x,y],x,y
              
              if (r1==1):
                  pix_13[x].append(1)
                  dv1+=1
                  #print 'rgb values'
                  #print r,g,b
                  #print 'end'
                  #print '1',
              elif (r1==2) :
                    #pix_02[x,y]=2
                    #print '2',
                    pix_13[x].append(2)
                    of1+=1
              elif (r1==3) :
                    #pix_02[x,y]=3
                    #print '3',
                     pix_13[x].append(3)
                     ag1+=1
              elif (r1==4) :
                   #pix_02[x,y]=4
                   #print '4',
                    pix_13[x].append(4)
                    ri1+=1
              elif (r1==5) :
                    #pix_02[x,y]=5
                    #print '5',
                     pix_13[x].append(5)
                     ub1+=1
              elif (r1==6) :
                   #pix_02[x,y]=6
                   #print '6',
                    pix_13[x].append(6)
                    bl1+=1
              else:
                  pix_13[x].append(0)
              y=y+1
          x=x+1
          #print ''
      #print 'second pic'
      #print pix_13
      #v=0
      #b=0
      #while v<w:
      #    b=0
      #    while b<h:
      #        print pix_13[v][b]
      #    b=b+1
      #v=v+1
      #print 'after'
      '''print hv1,of1,sc1,ag1,ri1,op1
      tot1=float(hv1+of1+sc1+ag1+ri1+op1)
      pi2=[hv1/tot1,of1/tot1,sc1/tot1,ag1/tot1,ri1/tot1,op1/tot1]
      print 'pi'
      print pi
      print 'pi2'
      print pi2
      print 'individal'
      print pi2[1]
      print sum(pi2)
      print sum(pi)
      #pit2 is the transpose version of 2013 initial matrix i.e. pi2
      pit2=[]
      pit2.append([])
      pit2[0].append(pi2[0])
      pit2.append([])
      pit2[1].append(pi2[1])
      pit2.append([])
      pit2[2].append(pi2[2])
      pit2.append([])
      pit2[3].append(pi2[3])
      pit2.append([])
      pit2[4].append(pi2[4])
      pit2.append([])
      pit2[5].append(pi2[5])
      print 'in transpose the next matrix'
      print pit2
      '''
      #############################################################transition##################################3
      x=0
      #naive approach for calculating transition matrix...a long list of variables depicting change from 2002 to 2013 as per their name
      one_one=0
      one_two=0
      one_three=0
      one_four=0
      one_five=0
      one_six=0
      two_one=0
      two_two=0
      two_three=0
      two_four=0
      two_five=0
      two_six=0
      three_one=0
      three_two=0
      three_three=0
      three_four=0
      three_five=0
      three_six=0
      four_one=0
      four_two=0
      four_three=0
      four_four=0
      four_five=0
      four_six=0
      five_one=0
      five_two=0
      five_three=0
      five_four=-296105# THIS IS BECAUSE OF BORDERS IF BORDERS BLACK THEN MAKE 0
      five_five=0
      five_six=0
      six_one=0
      six_two=0
      six_three=0
      six_four=0
      six_five=0
      six_six=0


      x=0
      y=0

      #CALCULATING THE TRANSITION MATRIX
      #iterating through the complete image
      while x<w:
          y=0
          while y<h:
              #IF FIRST IMAGE IS 1 
              if(pix_02[x][y]==1):
                  if (pix_13[x][y]==1):
                     one_one+=1
                  if (pix_13[x][y]==2):
                      one_two+=1
                  if (pix_13[x][y]==3):
                      one_three+=1
                  if (pix_13[x][y]==4):
                      one_four+=1
                  if (pix_13[x][y]==5):
                      one_five+=1
                  if (pix_13[x][y]==6):
                      one_six+=1
              #IF FIRST IMAGE IS 2
              elif(pix_02[x][y]==2):
                  if (pix_13[x][y]==1):
                      two_one+=1
                  if (pix_13[x][y]==2):
                      two_two+=1
                  if (pix_13[x][y]==3):
                      two_three+=1
                  if (pix_13[x][y]==4):
                      two_four+=1
                  if (pix_13[x][y]==5):
                      two_five+=1
                  if (pix_13[x][y]==6):
                      two_six+=1
              #IF FIRST IMAGE IS 3  
              elif(pix_02[x][y]==3):
                  if (pix_13[x][y]==1):
                      three_one+=1
                  if (pix_13[x][y]==2):
                      three_two+=1
                  if (pix_13[x][y]==3):
                      three_three+=1
                  if (pix_13[x][y]==4):
                      three_four+=1
                  if (pix_13[x][y]==5):
                      three_five+=1
                  if (pix_13[x][y]==6):
                      three_six+=1
              #IF FIRST IMAGE IS 4  
              elif(pix_02[x][y]==4):
                  if (pix_13[x][y]==1):
                      four_one+=1
                  if (pix_13[x][y]==2):
                      four_two+=1
                  if (pix_13[x][y]==3):
                      four_three+=1
                  if (pix_13[x][y]==4):
                      four_four+=1
                  if (pix_13[x][y]==5):
                      four_five+=1
                  if (pix_13[x][y]==6):
                      four_six+=1
              #IF FIRST IMAGE IS 5   
              elif(pix_02[x][y]==5):
                  if (pix_13[x][y]==1):
                      five_one+=1
                  if (pix_13[x][y]==2):
                      five_two+=1
                  if (pix_13[x][y]==3):
                      five_three+=1
                  if (pix_13[x][y]==4):
                      five_four+=1
                  if (pix_13[x][y]==5):
                      five_five+=1
                  if (pix_13[x][y]==6):
                      five_six+=1
              #IF FIRST IMAGE IS 6  
              elif(pix_02[x][y]==6):
                  if (pix_13[x][y]==1):
                      six_one+=1
                  if (pix_13[x][y]==2):
                      six_two+=1
                  if (pix_13[x][y]==3):
                      six_three+=1
                  if (pix_13[x][y]==4):
                      six_four+=1
                  if (pix_13[x][y]==5):
                      six_five+=1
                  if (pix_13[x][y]==6):
                      six_six+=1
              y=y+1
          x=x+1
      
      #FIRST IMAGE IS OF 2005
      #SECOND IMAGE IS OF 2013
      #2013-2005=8 YEARS
      predyear=int(predy)-2014
      predyear=float(predyear)/8
      print predyear
      #row1 contains transitions from 1
      row1=[one_one*predyear,one_two*predyear,one_three*predyear,one_four*predyear,one_five*predyear,one_six*predyear]
      po=0
      
      '''print 'one-one',
      print one_one
      print 'one-two',
      print one_two
      print 'one-three',
      print one_three
      print 'one-four',
      print one_four
      print 'one-five',
      print one_five
      print 'one-six',
      print one_six
      print 'two-one',
      print two_one
      print 'two-two',
      print two_two
      print 'two-three',
      print two_three
      print 'two-four',
      print two_four
      print 'two-five',
      print two_five
      print 'two-six',
      print two_six
      print 'three-one',
      print three_one
      print 'three-two',
      print three_two
      print 'three-three',
      print three_three
      print 'three-four',
      print three_four
      print 'three-five',
      print three_five
      print 'three-six',
      print three_six
      print 'four-one',
      print four_one
      print 'four-two',
      print four_two
      print 'four-three',
      print four_three
      print 'four-four',
      print four_four
      print 'four-five',
      print four_five
      print 'four-six',
      print four_six
      print 'five-one',
      print five_one
      print 'five-twe',
      print five_two
      print 'five-threee',
      print five_three
      print 'five-four',
      print five_four
      print 'five-five',
      print five_five
      print 'five-six',
      print five_six
      print 'six-one',
      print six_one
      print 'six-two',
      print six_two
      print 'six-three',
      print six_three
      print 'six-four',
      print six_four
      print 'six-five',
      print six_five
      print 'six-six',
      print six_six'''

      # we add +1 as if no transition so divide by zero is not possible
      sum1=sum(row1)+1
      #print 'sum1',
      #print sum1

      
      #row1 in stochastic form
      row1=[one_one/float(sum1),one_two/float(sum1),one_three/float(sum1),one_four/float(sum1),one_five/float(sum1),one_six/float(sum1)]

      #row2 contains transitions from 2
      #row1=row1*predyear
      row2=[two_one*predyear,two_two*predyear,two_three*predyear,two_four*predyear,two_five*predyear,two_six*predyear]
      sum2=sum(row2)+1
      #print 'sum2',
      #print sum2
      #row2 in stochastic form
      row2=[two_one/float(sum2),two_two/float(sum2),two_three/float(sum2),two_four/float(sum2),two_five/float(sum2),two_six/float(sum2)]

      #row3 contains transitions from 3
      row3=[three_one*predyear,three_two*predyear,three_three*predyear,three_four*predyear,three_five*predyear,three_six*predyear]
      sum3=sum(row3)+1
      #print 'sum3',
      #print sum3
      #row3 in stochastic form
      row3=[three_one/float(sum3),three_two/float(sum3),three_three/float(sum3),three_four/float(sum3),three_five/float(sum3),three_six/float(sum3)]

      #row4 contains transtitions from 4
      row4=[four_one*predyear,four_two*predyear,four_three*predyear,four_four*predyear,four_five*predyear,four_six*predyear]
      sum4=sum(row4)+1
      #print 'sum4',
      #print sum4
      #row 4 in stochastic form
      row4=[four_one/float(sum4),four_two/float(sum4),four_three/float(sum4),four_four/float(sum4),four_five/float(sum4),four_six/float(sum4)]

      #row5 contains transitions from 5
      row5=[five_one*predyear,five_two*predyear,five_three*predyear,five_four*predyear,five_five*predyear,five_six*predyear]
      sum5=sum(row5)+1
      #print 'sum5',
      #print sum5
      #row5 in stochastic form
      row5=[five_one/float(sum5),five_two/float(sum5),five_three/float(sum5),five_four/float(sum5),five_five/float(sum5),five_six/float(sum5)]

      #row6 contains transitions from 6
      row6=[six_one*predyear,six_two*predyear,six_three*predyear,six_four*predyear,six_five*predyear,six_six*predyear]
      sum6=sum(row6)+1
      #print 'sum6',
      #print sum6
      #row6 in stochastic form
      row6=[six_one/float(sum6),six_two/float(sum6),six_three/float(sum6),six_four/float(sum6),six_five/float(sum6),six_six/float(sum6)]

      #tr is the transition matrix
      #w=E10.get()
      #print 'year',w
      

      #THE FINAL TRANSITION MATRIX IS tr
      tr=[row1,row2,row3,row4,row5,row6]
      print 'transition aftr changes'
      print tr

      #ttr is the transposed version of tr i.e. the transposed matrix
      '''ttr=[]
      i=0
      j=0
      #while i<6:
      #    ttr.append([])
      #    j=0
      #
      #    while j<6:
      #        ttr[j].append(tr[i][j])
      #        j=j+1
      #    i=i+1


      #naive approach of transpodsing arr[i][j]=arr[j][i]
      ttr.append([])
      ttr[0].append(tr[0][0])
      ttr[0].append(tr[1][0])
      ttr[0].append(tr[2][0])
      ttr[0].append(tr[3][0])
      ttr[0].append(tr[4][0])
      ttr[0].append(tr[5][0])
      ttr.append([])
      ttr[1].append(tr[0][1])
      ttr[1].append(tr[1][1])
      ttr[1].append(tr[2][1])
      ttr[1].append(tr[3][1])
      ttr[1].append(tr[4][1])
      ttr[1].append(tr[5][1])
      ttr.append([])
      ttr[2].append(tr[0][2])
      ttr[2].append(tr[1][2])
      ttr[2].append(tr[2][2])
      ttr[2].append(tr[3][2])
      ttr[2].append(tr[4][2])
      ttr[2].append(tr[5][2])
      ttr.append([])
      ttr[3].append(tr[0][3])
      ttr[3].append(tr[1][3])
      ttr[3].append(tr[2][3])
      ttr[3].append(tr[3][3])
      ttr[3].append(tr[4][3])
      ttr[3].append(tr[5][3])
      ttr.append([])
      ttr[4].append(tr[0][4])
      ttr[4].append(tr[1][4])
      ttr[4].append(tr[2][4])
      ttr[4].append(tr[3][4])
      ttr[4].append(tr[4][4])
      ttr[4].append(tr[5][4])
      ttr.append([])
      ttr[5].append(tr[0][5])
      ttr[5].append(tr[1][5])
      ttr[5].append(tr[2][5])
      ttr[5].append(tr[3][5])
      ttr[5].append(tr[4][5])
      ttr[5].append(tr[5][5])'''

      o=[[0],[0],[0],[0],[0],[0]]
      p=[[0],[0],[0],[0],[0],[0]]
      result1=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
      result2=[[0],[0],[0],[0],[0],[0]]
      c=0


      #THIS FUNCTION IS USED FOR MULTIPLICATION tr*obs*pi
      def multi(ttr2,obs,pi):
          result1=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
          result2=[[0],[0],[0],[0],[0],[0]]
          #print 'multiplication fxn'
          for i in range(len(ttr2)):
              for j in range(len(obs[0])):
                  for k in range(len(obs)):
                      result1[i][j]+=ttr2[i][k]*obs[k][j]
          #for r in result1:
              #print r

          for i in range(len(result1)):
              #print 'length of pi[0]',
              #print len(pi[0])
              for j in range(len(pi[0])):
                  for k in range(len(pi)):
                      result2[i][j]+=result1[i][k]*pi[k][j]
          '''for r in result2:
              print r
          print 'max'
          maxi=result2.index(max(result2))+1
          print maxi'''
         
          return result2


      #THIS FUNCTION USES BAUM-WELCH ALGORITHM'S FORWARD APPROACH
      def fwd(i):

         #THIS IS BASE CASE 
         if i==0:
              o=pit
              #print 'base case',
              #print i
              return o

         #THIS IS RECURSIVE CASE
         else :
             #a[i]=ttr*obs[i-1]*fwd(i-1)
             #print 'in recursion',
             #print i
             o=fwd(i-1)
             #print 'vl now call multiplic with i=',
             #print i
             #print 'printing o'
             #print o
             #print'printing obs[c][i-1] ',
             #print c,(i-1)
             #print obs[c][i-1]
             o=multi(tr,obs[c][i-1],o)
             #print 'after multiplicatn'
             #print 'printing maxi',
            
             return o

      ############    OBSERVATION MATRIX     #######################
      q=4
      r=4
      #q and r are the pixel values set
      #list of variables which will contain the count of a particular LULC 
      oone=0
      otwo=0
      othree=0
      ofour=0
      ofive=0
      osix=0
      z=0
      #w=w/2
      #h=h/2
      #LOOPING ACROSS THE ENTIRE IMAGE
      while q<w-4:
          x=0
          r=0
          check=0
          #print 'next'
          while r<h-4:
              #print q,r
              #OBSERVATIONMATRIX WITH RESPECT TO FIRST IMAGE
              obs_02=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]] #observation matrix with respect to 2002 image
              #print 'value of q and r',
    
              #as the observation matrix has to be 6*6 for baum-walch algorithm's forward approach so iterate from q-3 to q+3 and r-3 to r+3
              e=q-1
              
              x=0
              #if j==0:
              #    x=x+1
              #if k==0:
              #    x=x+1
              #if l==0:
              #    x=x+1
              #print x
              #if x==3 and check==1:
              #   break;
              if x!=3:
                  check=1
                  #VIEWING THE NEIGHBORING 9 PIXELS OF q,r
                  while e<q+1:
                      f=r-1
                      #obs_02.append([])
                      while f<=r+1:
                          if pix_02[e][f]==1 :
                              #obs_02[z].append(1)
                              oone=oone+1
                          elif pix_02[e][f]==2 :
                              #obs_02[z].append(2)
                              otwo=otwo+1
                          elif pix_02[e][f]==3 :
                              #obs_02[z].append(3)
                              othree=othree+1
                          elif pix_02[e][f]==4 :
                              ofour=ofour+1
                              #obs_02[z].append(4)
                          elif pix_02[e][f]==5 :
                              ofive=ofive+1
                              #obs_02[z].append(5)
                          elif pix_02[e][f]==6 :
                              #obs_02[z].append(6)
                              osix=osix+1
                          else :
                              po=1
                              #obs_02[z].append(0)
                          f=f+1
                      e=e+1
                      z=z+1
                  osum=oone+otwo+othree+ofour+ofive+osix
                  #print 'new obs matrix'
                  #print obs_02[1][1]
                  #this observation matrix contains only diagonal entries [0,0] is hv [1,1] of [2,2] is sc [3,3] is ag [4,4] is ri [5,5] is oa
                  if osum==0:
                      osum=osum+1
                  obs_02[0][0]=oone/float(osum)
                  obs_02[1][1]=otwo/float(osum)
                  obs_02[2][2]=othree/float(osum)
                  obs_02[3][3]=ofour/float(osum)
                  obs_02[4][4]=ofive/float(osum)
                  obs_02[5][5]=osix/float(osum)
                  z=0
                  while z<6:
                      u=0
                      while u<6:
                          if z!=u:
                              #non-diagonal entris are 0
                              obs_02[z][u]=0
                          u=u+1
                      z=z+1

                      #############OBSERVATION MATRIX WITH RESPECT TO SECOND IMAGE#######################
                  oone=0
                  otwo=0
                  othree=0
                  ofour=0
                  ofive=0
                  osix=0
                  z=0
                  #print 'obs 13'
                  obs_13=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]] #observation matrix with respect to 2013 image
                  e=q-1
                  while e<q+1:
                      f=r-1
                      #obs_13.append([])
                      while f<r+1:
                          if pix_13[e][f]==1 :
                              #obs_13[z].append(1)
                              oone=oone+1
                          elif pix_13[e][f]==2 :
                              #obs_13[z].append(2)
                              otwo=otwo+1
                          elif pix_13[e][f]==3 :
                              #obs_13[z].append(3)
                              othree=othree+1
                          elif pix_13[e][f]==4 :
                              ofour=ofour+1
                              #obs_13[z].append(4)
                          elif pix_13[e][f]==5 :
                              ofive=ofive+1
                              #obs_13[z].append(5)
                          elif pix_13[e][f]==6 :
                              #obs_13[z].append(6)
                              osix=osix+1
                          else :
                              po=1
                              #obs_13[z].append(0)
                          f=f+1
                      e=e+1
                      z=z+1
                              
                  #print 'obs13 matrix'
                  #print obs_13
                  #print oone,otwo,othree,ofour,ofive,osix
                  osum=oone+otwo+othree+ofour+ofive+osix
                  #print 'osum ',
                  #print osum
                  #print 'new obs13 matrix'
                  if osum==0:
                      osum=osum+1
                  obs_13[0][0]=oone/float(osum)
                  obs_13[1][1]=otwo/float(osum)
                  obs_13[2][2]=othree/float(osum)
                  obs_13[3][3]=ofour/float(osum)
                  obs_13[4][4]=ofive/float(osum)
                  obs_13[5][5]=osix/float(osum)
                  z=0
                  while z<6:
                      u=0
                      while u<6:
                          if z!=u:
                              obs_13[z][u]=0
                          u=u+1
                      z=z+1
                  #print 'the matrix finally of 2013'
                  #print obs_13
                  oone=0
                  otwo=0
                  othree=0
                  ofour=0
                  ofive=0
                  osix=0
                  z=0
                  obs.append([])
                  obs[c].append(obs_02)
                  obs[c].append(obs_13)
                  #print 'obs value'
                  #print obs[c][0]
                  #print 'obs'
                  #print obs[c]
                      
                  #print 'multiplication'
                  #print obs[c][0]


                  #CALLING THE FUNCTION
                  p=fwd(2)
                  #print 'in main'
                  '''t=0
                  if j==0:
                     t=t+1
                  if k==0:
                      t=t+1
                  if l==0:
                      t=t+1
                  if t!=3:'''


                  #CALCULATIN THE INDEX OF MAX VALUE AND ADDING 1 AS INDEX STARTS FROM 0
                  maxi=p.index(max(p))+1
                  #print 'LULC VALUE',
                  #print maxi,
                  if maxi==1:
                      pixels[q,r]=1
                  elif maxi==2:
                      pixels[q,r]=2
                  elif maxi==3:
                      pixels[q,r]=3
                  elif maxi==4:
                      pixels[q,r]=4
                  elif maxi==5:
                      pixels[q,r]=5
                  elif maxi==6:
                      pixels[q,r]=6
                  else:
                      pixels[q,r]=(0,0,0)

                  # PRESERVING THE URBAN LAND PIXELS
                  if pix_13[e][f]==5 :
                      pixels[q,r]=5
                  if pix_02[e][f]==5 :
                      pixels[q,r]=5  
                          
                  c=c+1
              r=r+1
          q=q+1
          #print ''
      #import webbrowser
      print 'done'


      #SAVING THE IMAGE
      filename481=outputfile
      imgnew.save(filename481)
      '''#webbrowser.open(filename)
      newimgw=Toplevel(root)
      im48=Image.open(filename48)
      tkimage = ImageTk.PhotoImage(im48)
      Label(newimgw, image=tkimage).pack()'''

      #BUTTON TO VIEW THE IMAGE
      B52 = Button(root, text ="VIEW IMAGE",font=('Arial',18),command=lambda:viewimg(filename481))
      B52.pack(padx=1, pady=1)
      B52.place(x=180,y=400)


      #BUTTON TO VIEW THE TRANSITION MATRIX
      B50 = Button(root, text ="TRANSITION MATRIX",font=('Arial',18),command=lambda:predicttr(tr))
      B50.pack(padx=1, pady=1)
      B50.place(x=180,y=450)

      #BUTTON TO VIEW THE TRANSITION MAPS
      B51 = Button(root, text ="VIEW TRANSITION MAPS",font=('Arial',18),command=lambda:transition(pix,pix2,w,h))
      B51.pack(padx=1, pady=1)
      B51.place(x=180,y=500)
      
      
      #iterate over the complete length and breath of image to find 6*1 matrix which is transposed and find the max value in the matrix
      #corresponding to the max value find the index+1 value which corresponds to the LULC value
      #according to this LULC value draw a new image deferencing the LULC value with the RGB values



      print 'done'


    #FUNCTION TO VIEW THE TRANSITION MATRIX
    def predicttr(tr):
        
        #global root5
        root5=Toplevel()
        label_font = ('helvetica', 20)
        label_font1 = ('helvetica', 10)

        #MAKING LABELS FOR HEADING AND VALUES OF TRANSITION MATRIX
        Label(root5, text='The transition matrix is:',font=label_font, bg='white', 
             fg='black', relief='raised', bd=3).pack(padx=10, pady=10)
        Label(root5, text=tr[0],font=label_font1, bg='white', 
             fg='black', relief='raised', bd=3).pack(padx=5, pady=5)
        Label(root5, text=tr[1],font=label_font1, bg='white', 
             fg='black', relief='raised', bd=3).pack(padx=5, pady=5)
        Label(root5, text=tr[2],font=label_font1, bg='white', 
             fg='black', relief='raised', bd=3).pack(padx=5, pady=5)
        Label(root5, text=tr[3],font=label_font1, bg='white', 
             fg='black', relief='raised', bd=3).pack(padx=5, pady=5)
        Label(root5, text=tr[4],font=label_font1, bg='white', 
             fg='black', relief='raised', bd=3).pack(padx=5, pady=5)
        Label(root5, text=tr[5],font=label_font1, bg='white', 
             fg='black', relief='raised', bd=3).pack(padx=5, pady=5)

        label_font = ('Arial', 15)

        #LABEL AND ENTRY TO INPUT THE OUTPUT FILE NAME WHICH WILL CONTAIN THE TRANSITION MATRIX
        Label(root5, text='Enter output filename', font=label_font, bg='white', 
           fg='#666666', relief='raised', bd=3).pack()
    
        E15=Entry(root5,text='output',font=('Arial',20),bd=5)
        E15.pack()

        
        # BUTTON TO SAVE THE CONTENTS OF TRANSITION MATRIX IN A FILE
        B3 = Button(root5, text ="save to file",command=lambda :savetofile(tr,E15.get()))
        B3.pack(padx=5, pady=5)
        root5.mainloop()



    #FUNCTION WHICH THE CONTENTS OF TRANSITION MATRIX IN A FILE
    def savetofile(tr,name):
        
        thefile=open(name,'w')
        for item in tr:
            thefile.write("%s\n"%item)


    #THIS FUNCTION DESTROYS THE ROOT. IT IS CALLED WHEN EXIT BUTTON IS CLICKED
    def displaying3():
        global root
        root.destroy()


    #THIS FUNCTION IS USED IN GENERATING TRANSITION MAPS
    def transition(pix,pix2,w,h):
        execfile('guitransition.py')

        #MAKING A DROP DOWN MENU TO SELECT LEGEND 1
        var1=StringVar(root)
        var1.set('1')
        choices=[1,2,3,4,5,6]
        option1=OptionMenu(root,var1,*choices)
        option1.configure(font=('Arial',12))
        option1.pack()
        option1.place(x=180,y=580)


        #MAKING A DROP DOWN MENU TO SELECT LEGEND 2
        var2=StringVar(root)
        var2.set('1')
        option2=OptionMenu(root,var2,*choices)
        option2.configure(font=('Arial',12))
        option2.pack()
        option2.place(x=280,y=580)
        print var2.get()

        #BUTTON TO START CALCULATING THE TRANSITION MAP
        B6 = Button(root,text ="start",font=('Arial',12),relief='raised', bd=3,command=lambda:transmap(var1.get(),var2.get(),pix,pix2,w,h))
        B6.pack()
        B6.place(x=180,y=620)



    #FUNCTION TO CALCULATE THE TRANSITION FROM var1 AND var2 AND VICE-VERSA
    def transmap(var1,var2,pix,pix2,w,h):
        print pix[116,405]
        print 'var1',var1,'var2',var2

        #MAKING A NEW IMAGE AND IT'S PALETTE
        imgnew11 = Image.new( 'P', (w,h), 0)
        imgnew11.putpalette([
          0, 0, 0, # black background
          45, 138, 86, # index 1 is darkgreen
          0,0,254,# index 2 is yellow
          
        ])

        #LOADING THE IMAGE
        pixels=imgnew11.load()
        
        #w=int(im.size[0])
        #h=int(im.size[1])
        var11=int(var1)
        var21=int(var2)
        x=0
        y=0

        #LOOPING ACROSS THE ENTIRE IMAGE
        while x<w:
            y=0
            while y<h:
                c=0

                #CALCULATING CHANGES FROM LEGEND1 TO LEGEND2
                if pix[x,y]==var11:
                    if pix2[x,y]==var21:
                        pixels[x,y]=1

                #CALCULATING CHANGES FROM LEGEND2 TO LEGEND1
                if pix2[x,y]==var11:
                    if pix[x,y]==var21:
                        pixels[x,y]=2
                y=y+1
            x=x+1

                        
        label_font = ('Arial', 15)
        #SAVING THE IMAGE AND GIVING A DEFAULT NAME
        filename="transmap.tif"
        imgnew11.save(filename)

        #ASKING THE USER TO INPUT THE OUTPUT FILE NAME
        label11=Label(root, text='Enter output filename', font=label_font, bg='white', 
         fg='#666666', relief='raised', bd=3)
        label11.place(x=180,y=670)
    
        Et=Entry(root,text='output',font=('Arial',20),bd=5)
        Et.place(x=180,y=700)


        #BUTTON TO VIEW THE TRANSITION MAP
        #IT CALLS viewimg22(,) FUNCTION WITH 2 ARGUMENTS. ARGUMENT1 IS DEFAULT NAME,ARGUMENT2 IS USER'S OUTPUT NAME
        #IN viewimg22() THE FILE WILL BE RENAMED
        #THIS IS DONE BECAUSE OF EVENT-MANAGEMENT
        B54 = Button(root, text ="VIEW TRANSITION MAP",font=('Arial',15),command=lambda:viewimg22(filename,Et.get()))
        B54.pack(padx=5, pady=5)
        B54.place(x=180,y=750)

      
       
    #DEFINING PREDICTION WINDOW
    global root
    root=Tk()
    root.title('MARKOV PREDICTIVE ANALYSIS')
    root.geometry('800x900')#SIZE OF WINDOW
    scrollbar=Scrollbar(root)
    root.configure(background="#9999ff")
    scrollbar.pack(side=RIGHT, fill=Y)
    filename1=""
    filename2=""

    
    #THIS IS USED TO DISPLAY THE HEADING    
    label_font = ('helvetica', 30)
    Label(root, text='MARKOV PREDICTIVE ANALYSIS',font=label_font, bg='white', 
             fg='#666666', relief='raised', bd=3).pack(fill='x', padx=5, pady=5)
    

    #THIS BUTTON IS USED TO INPUT THE IMAGES
    B1 = Button(root, text ="CLICK TO INPUT THE IMAGES",font=('Arial',18),command=inputfile1)
    B1.pack(padx=5, pady=5)


    
    #LABEL AND ENTRY COMBINATION TO INPUT THE OUTPUT FILE NAME
    label_font = ('Arial', 15)
    Label(root, text='Enter output filename', font=label_font, bg='white', 
         fg='#666666', relief='raised', bd=3).pack()
    E1=Entry(root,bd=5,font=('Arial',18))
    E1.pack()
    #label1.pack(padx=5, pady=5)

    #THIS BUTTON IS USED TO CLOSE THE CURRENT WINDOW
    B7 = Button(root, text ="EXIT",relief='raised',font=('Arial',18), bd=3,command=displaying3)
    B7.pack(padx=5, pady=5,side=BOTTOM) 
    root.mainloop()

#THIS FUNCTION IS CALLED WHEN USER CLICKS SUPER RESOLUTION BUTTON FROM THE MAIN WINDOW
def displaying2():
    outputfilesup=""
    #execfile('guisuperresolution.py')

    #THIS FUNCTION IS USED TO CLASSIFY THE INPUT IMAGES
    def classify111(filename1,filename2,filename3,filename4,filename5,filename6):
        print filename1,filename2,filename3,filename4,filename5,filename6

        #THIS LABEL IS USED TO PRINT MESSAGE ON SCREEN
        Label(root2, text='Wait for super resolute button to appear on screen', bg='white', 
             fg='#666666', relief='raised', bd=3).pack(padx=5, pady=5)


        #OPENING THE INPUT IMAGES
        im1=Image.open(filename1)
        im2=Image.open(filename2)
        im3=Image.open(filename3)
        im4=Image.open(filename4)
        im5=Image.open(filename5)
        im6=Image.open(filename6)

        #CREATING A NEW IMAGE IN PALETTE MODE USED TO STORE LEGENDS
        imgnew1 = Image.new( 'P', (1700,1250), 0)

        #CREATING A NEW IMAGE IN FLOAT MODE USED TO STORE DN VALUES
        imgnew2=Image.new('F',(1700,1250),0)
        
        imgnew1.putpalette([
            0, 0, 0, # black background
            254, 0,254, # index 1 is magenta
            254, 254, 0, # index 2 is yellow
            0,0, 254, # index 3 is blue
            254,254,254,# index 4 is white
            45,138,86,# index 5 is dark green
            0,254,0# index 6 is light green
        ])

        pixels1=imgnew1.load()
        pixels2=imgnew2.load()
        #pixels2=imgnew2.load()
        #pixels3=imgnew3.load()


        #THIS IS THE TRAINING DATA FOR URBANLAND
        ubpure=[[(9152+8444+9054+8513+8584+8594)/float(6)],
                [(8626+7826+8409+7926+8011+7968)/float(6)],
                [(8609+7572+8439+7715+7865+7739)/float(6)],
                [(9477+9869+9375+9157+9237+9204)/float(6)],
                [(9495+8708+9088+8570+9216+8808)/float(6)],
                [(8606+7729+8263+7778+8240+7941)/float(6)]]

        #THIS IS THE TRAINING DATA FOR AGRICLUTURE LAND
        agpure=[[(8272+8205+8201+8077+8189+8312)/float(6)],
                [(7856+7645+7819+7664+7686+7817)/float(6)],
                [(7893+7645+7340+7206+7124+8009)/float(6)],
                [(11961+10742+11690+11172+11767+10527)/float(6)],
                [(11960+8997+9686+9455+9177+11769)/float(6)],
                [(9442+7488+8059+7681+7433+9673)/float(6)]]

        #THIS IS THE TRAINING DATA FOR DRY RIVER BED
        rbpure=[[(9234+10145+10104+9026+9478+9252)/float(6)],
                [(8851+9699+9953+8592+9082+9086)/float(6)],
                [(8799+9838+10239+8579+9063+9403)/float(6)],
                [(8916+10186+11108+9751+9325+10759)/float(6)],
                [(8651+10183+11337+9962+9340+10896)/float(6)],
                [(7826+9016+9964+8774+8438+9391)/float(6)]]

        #THIS IS THE TRAINING DATA FOR BARREN LAND
        blpure=[[(7852+7967+7956+8134+7962+7969)/float(6)],
                [(7106+7349+7275+7564+7287+7361)/float(6)],
                [(6950+7177+7027+7582+7036+7181)/float(6)],
                [(8772+9920+9816+9705+10090+10200)/float(6)],
                [(10369+10029+10399+10947+10053+10283)/float(6)],
                [(8491+8301+8419+9048+8153+8251)/float(6)]]

        #THIS IS THE TRAINING DATA FOR DENSE FOREST
        dfpure=[[(8002+7920+8014+7588+7492+7594)/float(6)],
                [(7229+7154+7792+6926+7062+7065)/float(6)],
                [(6666+6593+7960+6280+6654+6421)/float(6)],
                [(9915+11738+13316+12322+13092+13343)/float(6)],
                [(9046+9231+13142+8873+9955+9563)/float(6)],
                [(7093+7090+7154+6626+7417+7122)/float(6)]]

        #THIS IS THE TRAINING DATA FOR OPEN FOREST
        ofpure=[[(7569+7449+7597+7556+7605+7509)/float(6)],
                [(6839+6824+6896+6809+7005+6861)/float(6)],
                [(6182+6129+6199+6139+6349+6195)/float(6)],
                [(11118+11682+10614+11592+11475+11308)/float(6)],
                [(7752+7546+7676+7668+8127+8033)/float(6)],
                [(6077+5938+6100+5975+6298+6181)/float(6)]]

        print 'pure pixels of urban land'
        print ubpure
        print ubpure[1][0]
        print 'pure pixels of agriculture land'
        print agpure
        print 'pure pixels of dry river bed'
        print rbpure
        print 'pure pixles of barren land'
        print blpure
        print 'pure pixels of dense forest'
        print dfpure
        print 'pure pixels of open forest'
        print ofpure

        #LOADING THE IMAGES
        pix1=im1.load()
        pix2=im2.load()
        pix3=im3.load()
        pix4=im4.load()
        pix5=im5.load()
        pix6=im6.load()

        flag=1
        #flag IS SET TO ONE AND IN LOOP WILL EXECUTE TILL LESS THAN 5 AS 8 IMAGES WILL BE FORMED 
        while flag<5:
            print flag
            x=0
            y=0

            #LOOPING ACROSS THE ENTIRE IMAGE 
            while x<1686:
                y=0
                while y<1215:
                    a=pix1[x,y]
                    b=pix2[x,y]
                    c=pix3[x,y]
                    d=pix4[x,y]
                    e=pix5[x,y]
                    f=pix6[x,y]
                    a11=ubpure[0][0]
                    a12=ubpure[1][0]
                    a13=ubpure[2][0]
                    a14=ubpure[3][0]
                    a15=ubpure[4][0]
                    a16=ubpure[5][0]

                    b11=agpure[0][0]
                    b12=agpure[1][0]
                    b13=agpure[2][0]
                    b14=agpure[3][0]
                    b15=agpure[4][0]
                    b16=agpure[5][0]

                    c11=rbpure[0][0]
                    c12=rbpure[1][0]
                    c13=rbpure[2][0]
                    c14=rbpure[3][0]
                    c15=rbpure[4][0]
                    c16=rbpure[5][0]

                    d11=blpure[0][0]
                    d12=blpure[1][0]
                    d13=blpure[2][0]
                    d14=blpure[3][0]
                    d15=blpure[4][0]
                    d16=blpure[5][0]

                    e11=dfpure[0][0]
                    e12=dfpure[1][0]
                    e13=dfpure[2][0]
                    e14=dfpure[3][0]
                    e15=dfpure[4][0]
                    e16=dfpure[5][0]

                    f11=ofpure[0][0]
                    f12=ofpure[1][0]
                    f13=ofpure[2][0]
                    f14=ofpure[3][0]
                    f15=ofpure[4][0]
                    f16=ofpure[5][0]
                     
                    
                    #FINDING THE EUCLIDIAN DISTANCE
                    z=0
                    dist1=math.sqrt(math.pow(a-a11,2)+math.pow(b-a12,2)+math.pow(c-a13,2)+math.pow(d-a14,2)+math.pow(e-a15,2)+math.pow(f-a16,2))
                    dist2=math.sqrt(math.pow(a-b11,2)+math.pow(b-b12,2)+math.pow(c-b13,2)+math.pow(d-b14,2)+math.pow(e-b15,2)+math.pow(f-b16,2))
                    dist3=math.sqrt(math.pow(a-c11,2)+math.pow(b-c12,2)+math.pow(c-c13,2)+math.pow(d-c14,2)+math.pow(e-c15,2)+math.pow(f-c16,2))
                    dist4=math.sqrt(math.pow(a-d11,2)+math.pow(b-d12,2)+math.pow(c-d13,2)+math.pow(d-d14,2)+math.pow(e-d15,2)+math.pow(f-d16,2))
                    dist5=math.sqrt(math.pow(a-e11,2)+math.pow(b-e12,2)+math.pow(c-e13,2)+math.pow(d-e14,2)+math.pow(e-e15,2)+math.pow(f-e16,2))
                    dist6=math.sqrt(math.pow(a-f11,2)+math.pow(b-f12,2)+math.pow(c-f13,2)+math.pow(d-f14,2)+math.pow(e-f15,2)+math.pow(f-f16,2))
                    distsum=dist1+dist2+dist3+dist4+dist5+dist6
                    dist11=[[dist1],[dist2],[dist3],[dist4],[dist5],[dist6]]

                 
                    dist=[[dist1/float(distsum)],[dist2/float(distsum)],[dist3/float(distsum)],[dist4/float(distsum)],[dist5/float(distsum)],[dist6/float(distsum)]]
                    #print 'stochastic'
                    #print dist
                    dist=[[1/dist[0][0]],[1/dist[1][0]],[1/dist[2][0]],[1/dist[3][0]],[1/dist[4][0]],[1/dist[5][0]]]
                    #print 'inverse'
                    #print dist
                    newsum=dist[0][0]+dist[1][0]+dist[2][0]+dist[3][0]+dist[4][0]+dist[5][0]
                    #print newsum
                    clas=[[dist[0][0]/newsum],[dist[1][0]/newsum],[dist[2][0]/newsum],[dist[3][0]/newsum],[dist[4][0]/newsum],[dist[5][0]/newsum]]

                    #CO IS USED TO FIND FIRST MAXIMUM,SECOND MAXIMUM AND SO ON OF EACH IMAGE
                    co=0
                    #print clas
                    while co<flag:
                        maxi=clas.index(max(clas))+1
                        maxi1=clas[maxi-1][0]
                        #maxi=maxi-1
                        clas[maxi-1][0]=0
                        #print  maxi1
                        
                        co=co+1
                    
                    
                    #print 'LULC VALUE',
                    #print maxi1

                    #STORING VALUE IN NEW IMAGE
                    pixels2[x,y]=maxi1   
                    if maxi==1:
                        pixels1[x,y]=1
                        
                    elif maxi==2:
                        pixels1[x,y]=2
                    elif maxi==3:
                        pixels1[x,y]=3
                    elif maxi==4:
                        pixels1[x,y]=4
                    elif maxi==5:
                        pixels1[x,y]=5
                    elif maxi==6:
                        pixels1[x,y]=6
                    else:
                        pixels1[x,y]=0
                      

                    #maxi=maxi-1
                    #clas[maxi][0]=0
                    #z=z+1
                        
                    y=y+1
                #print 'ggd'
                x=x+1

            #GETTING THE VALUE OF OUTPUT IMAGE
            outputfileclas=E1.get()

            #SAVING THE NEW IMAGES
            if flag==1:
                filename10=outputfileclas[:2]+"classi1"+outputfileclas[2:]
                imgnew1.save(filename10)
                filename20=outputfileclas[:2]+"values1"+outputfileclas[2:]
                imgnew2.save(filename20)
            if flag==2:
                filename30=outputfileclas[:2]+"classi2"+outputfileclas[2:]
                imgnew1.save(filename30)
                filename40=outputfileclas[:2]+"values2"+outputfileclas[2:]
                imgnew2.save(filename40)
            if flag==3:
                filename50=outputfileclas[:2]+"classi3"+outputfileclas[2:]
                imgnew1.save(filename50)
                filename60=outputfileclas[:2]+"values3"+outputfileclas[2:]
                imgnew2.save(filename60)
            if flag==4:
                filename70=outputfileclas[:2]+"classi4"+outputfileclas[2:]
                imgnew1.save(filename70)
                filename80=outputfileclas[:2]+"values4"+outputfileclas[2:]
                imgnew2.save(filename80)

            flag=flag+1


        var=StringVar(root2)

        label1=Label(root2,font=('Arial',10),text="Enter output file name")
       

        #DROP DOWN MENU TO SELECT 0.01,0.02,0.03,0.04,0.05
        var.set('0.03')
        choices=[0.00,0.01,0.02,0.03,0.04,0.05]
        option=OptionMenu(root2,var,*choices)
        option.configure(font=('Arial',12))
        option.pack()
        option.place(x=100,y=530)
        print var.get()


        #BUTTON TO SUPER RESOLUTE THE IMAGES
        B6 = Button(root2,text ="SUPER RESOLUTE",font=('Arial',20),relief='raised', bd=3,command=lambda:superresolution(filename10,filename20,filename30,filename40,filename50,filename60,filename70,filename80,var.get()))
        B6.pack()
        B6.place(x=175,y=530)

        


    #THIS IMAGE IS USED FOR SUPER RESOLUITON
    def superresolution(filename10,filename20,filename30,filename40,filename50,filename60,filename70,filename80,value):

        print 'value is',value,type(value)
        value1=float(value)
        print value1,type(value1)
        print 'rehy'
        outputfilesup=E1.get()
        print outputfilesup

        #OPENING THE IMAGES WHICH WERE MADE IN classified11 FUNCTION
        im1=Image.open(filename20)
        im2=Image.open(filename40)
        im3=Image.open(filename60)
        im4=Image.open(filename80)
        #im5=Image.open('clas16jul5values.tif')
        #im6=Image.open('clas16jul6values.tif')
        im7=Image.open(filename10)
        im8=Image.open(filename30)
        im9=Image.open(filename50)
        im10=Image.open(filename70)

        #im11=Image.open('clas16jul5.tif')
        #im12=Image.open('clas16jul6.tif')

        #MAKING THE NEW IMAGE IN PALETTE MODE
        imgnew=Image.new( 'P', (4000,3000), 0)
        pixels1=imgnew.load()
        imgnew.putpalette([
            0, 0, 0, # black background
            254, 0,254, # index 1 is magenta
            254, 254, 0, # index 2 is yellow
            0,0, 254, # index 3 is blue
            254,254,254,# index 4 is white
            45,138,86,# index 5 is dark green
            0,254,0# index 6 is light green
        ])

        #LOADING ALL THE IMAGES
        pix1=im1.load()
        pix2=im2.load()
        pix3=im3.load()
        pix4=im4.load()
        #pix5=im5.load()
        #pix6=im6.load()
        pix7=im7.load()
        pix8=im8.load()
        pix9=im9.load()
        pix10=im10.load()

        #pix11=im11.load()
        #pix12=im12.load()

        #INITIALIZATION OF VARIABLES
        ub=0
        ag=0
        dr=0
        bl=0
        df=0
        of=0
        x=2
        y=2
        u=x
        print pix1[290,406]
        print pix2[29,40]
        print pix3[900,67]


        #ITERATING ACROSS THE ENTIRE IMAGE
        while x<1686:
            y=2
            v=y
            while y<1215:
                ub=0
                ag=0
                dr=0
                bl=0
                df=0
                of=0
                e=x-1
                f=y-1
                while e<x+2:
                    f=y-1
                    while f<y+2:
                        
                        #C1 AND C2 CONTAIN THE PIXEL VALUES
                        c1=pix7[e,f]
                        c2=pix1[e,f]
                        if(c1==1):
                            ub=ub+c2
                        if(c1==2):
                            ag=ag+c2
                        if(c1==3):
                            dr=dr+c2
                        if(c1==4):
                            bl=bl+c2
                        if(c1==5):
                            df=df+c2
                        if(c1==6):
                            of=of+c2
                        c1=pix8[e,f]
                        c2=pix2[e,f]
                        if(c1==1):
                            ub=ub+c2
                        if(c1==2):
                            ag=ag+c2
                        if(c1==3):
                            dr=dr+c2
                        if(c1==4):
                            bl=bl+c2
                        if(c1==5):
                            df=df+c2
                        if(c1==6):
                            of=of+c2
                        c1=pix9[e,f]
                        c2=pix3[e,f]
                        if(c1==1):
                            ub=ub+c2
                        if(c1==2):
                            ag=ag+c2
                        if(c1==3):
                            dr=dr+c2
                        if(c1==4):
                            bl=bl+c2
                        if(c1==5):
                            df=df+c2
                        if(c1==6):
                            of=of+c2
                        c1=pix10[e,f]
                        c2=pix4[e,f]
                        if(c1==1):
                            ub=ub+c2
                        if(c1==2):
                            ag=ag+c2
                        if(c1==3):
                            dr=dr+c2
                        if(c1==4):
                            bl=bl+c2
                        if(c1==5):
                            df=df+c2
                        if(c1==6):
                            of=of+c2
                        '''c1=pix11[e,f]
                        c2=pix5[e,f]
                        if(c1==1):
                            ub=ub+c2
                        if(c1==2):
                            ag=ag+c2
                        if(c1==3):
                            dr=dr+c2
                        if(c1==4):
                            bl=bl+c2
                        if(c1==5):
                            df=df+c2
                        if(c1==6):
                            of=of+c2
                        c1=pix12[e,f]
                        c2=pix6[e,f]
                        if(c1==1):
                            ub=ub+c2
                        if(c1==2):
                            ag=ag+c2
                        if(c1==3):
                            dr=dr+c2
                        if(c1==4):
                            bl=bl+c2
                        if(c1==5):
                            df=df+c2
                        if(c1==6):
                            of=of+c2'''
                        f=f+1
                    e=e+1
                tot=ub+ag+dr+bl+df+of

                #P IS A LIST WHICH STORES THE PROBABILITY OF OCCURING OF EACH LEGEND
                p=[[ub/float(tot)],[ag/float(tot)],[dr/float(tot)],[bl/float(tot)],[df/float(tot)],[of/float(tot)]]
                #print 'max value',max(p)
                #print p
                

                #CALCULATING THE MAXIMUM PROBABILITY
                maxi=p.index(max(p))+1
                qty1=p[maxi-1][0]
                
                #qty=p[maxi-1]
                maxi1=maxi-1
                p[maxi1][0]=0
                maxi1=p.index(max(p))+1
                #qty1=max(p)
                qty11=p[maxi1-1][0]
                #print maxi,qty1,maxi1,qty11

                '''if value=='0.04':
                    value1=0.04'''
                '''value1=float(value)
                print value1,type(value1)'''


                #VALUE1 IS INPUT FROM USER AND IF THE DIFFERENCE BETWEEN LARGEST AND SECOND LARGEST IS GREATER THAN VALUE1 THEN MAXI1=MAXI
                if qty1-qty11>value1:
                    maxi1=maxi
                pixels1[u,v]=pix7[x,y]


                #AS SCALE 2 SO 1 PIXEL NOW REPRESENTS 4 PIXELS
                if maxi==1:
                    #pixels1[u,v]=1
                    pixels1[u,v+1]=1
                    pixels1[u+1,v+1]=maxi1
                    pixels1[u+1,v]=1
                elif maxi==2:
                    #pixels1[u,v]=2
                    pixels1[u,v+1]=2
                    pixels1[u+1,v+1]=maxi1
                    pixels1[u+1,v]=2
                elif maxi==3:

                    #pixels1[u,v]=3
                    pixels1[u,v+1]=3
                    pixels1[u+1,v+1]=maxi1
                    pixels1[u+1,v]=3
                elif maxi==4:
                    #pixels1[u,v]=4
                    pixels1[u,v+1]=4
                    pixels1[u+1,v+1]=maxi1
                    pixels1[u+1,v]=4
                elif maxi==5:
                    #pixels1[u,v]=5
                    pixels1[u,v+1]=5
                    pixels1[u+1,v+1]=maxi1
                    pixels1[u+1,v]=5
                elif maxi==6:
                    #pixels1[u,v]=6
                    pixels1[u,v+1]=6
                    pixels1[u+1,v+1]=maxi1
                    pixels1[u+1,v]=6
                else:
                    #pixels1[u,v]=(0,0,0)
                    pixels1[u,v+1]=(0,0,0)
                    pixels1[u+1,v+1]=(0,0,0)
                    pixels1[u+1,v]=(0,0,0)
                v=v+2

                y=y+1
            u=u+2
            x=x+1
        #import webbrowser

        #SAVING THE IMAGE    
        filenamefinal=outputfilesup
        imgnew.save(filenamefinal)


        #THIS IS USED TO CLEAR THE BUFFER BUT WAS GIVING ERROR
        '''os.unlink(filename10)
        os.unlink(filename20)
        os.unlink(filename30)
        os.unlink(filename40)
        os.unlink(filename50)
        os.unlink(filename60)
        os.unlink(filename70)
        os.unlink(filename80)'''
        
        

        #THIS BUTTON IS USED TO VIEW THE IMAGE
        B3 = Button(root2, text ="view",font=('Arial',18),command=lambda:viewimg(filenamefinal))
        B3.pack(padx=5, pady=5)



    #THIS FUNCTION IS USED TO INPUT THE IMAGES FOR SUPER RESOLUTION
    def inputfile1():
        #newimgw=Toplevel(root)

        # INPUT FIRST IMAGE 
        filename1 = askopenfilename()
        print filename1
        Label(root2, text='Input image1 ->'+filename1,font=('Arial',10)).pack(padx=1, pady=1)

        # INPUT SECOND IMAGE 
        filename2 = askopenfilename()
        print filename2
        Label(root2, text='Input image2 ->'+filename2,font=('Arial',10)).pack(padx=1, pady=1)

        # INPUT THIRD IMAGE 
        filename3 = askopenfilename()
        print filename3
        Label(root2, text='Input image3 ->'+filename3,font=('Arial',10)).pack(padx=1, pady=1)

        # INPUT FOURTH IMAGE 
        filename4 = askopenfilename()
        print filename4
        Label(root2, text='Input image4 ->'+filename4,font=('Arial',10)).pack(padx=1, pady=1)

        # INPUT FIFTH IMAGE 
        filename5 = askopenfilename()
        print filename5
        Label(root2, text='Input image5 ->'+filename5,font=('Arial',10)).pack(padx=1, pady=1)

        # INPUT SIXTH IMAGE 
        filename6 = askopenfilename()
        print filename6
        Label(root2, text='Input image6 ->'+filename6,font=('Arial',10)).pack(padx=1, pady=1)


        #THIS BUTTON IS USED TO CLASSIFY THE INPUT IMAGES
        B3 = Button(root2, text ="CLASSIFY",font=('Arial',20),command=lambda:classify111(filename1,filename2,filename3,filename4,filename5,filename6))
        B3.pack(padx=5, pady=5)

        


    #THIS FUNCTION IS USED TO CLOSE THE CURRENT WINDOW
    #IT IS EXECUTED WHEN EXIT BUTTON IS CLICKED
    def displaying3():
        global root2
        root2.destroy()
    


    #THIS IS USED TO MAKE THE SUPER RESOLUTION WINDOW
    global root2
    root2=Tk()
    root2.title('MARKOV SUPER RESOLUTION')

    #DEFINING THE SIZE OF THE WINDOW
    root2.geometry('700x700')
    root2.configure(background="#9999ff")
    scrollbar=Scrollbar(root2)
    scrollbar.pack(side=RIGHT, fill=Y)
        

    #HEADING OF SUPER RESOLUTION WINDOW
    label_font = ('helvetica', 35)
    Label(root2, text="SUPER RESOLUTION",font=label_font, bg='white', 
             fg='#666666', relief='raised', bd=3).pack(fill='x', padx=5, pady=5)

    #BUTTON TO INPUT THE IMAGES
    B1 = Button(root2, text ="CLICK TO INPUT THE IMAGES",font=('Arial',20),command=inputfile1)
    B1.pack(padx=5, pady=5)


    #LABEL AND ENTRY TO TAKE OUTPUT FILENAME FROM USER
    label_font = ('Arial', 15)
    Label(root2, text='Enter output filename', font=label_font, bg='white', 
         fg='#666666', relief='raised', bd=3).pack()
    
    E1=Entry(root2,text='output',font=('Arial',20),bd=5)
    E1.pack()
    #label1.pack(padx=5, pady=5)


    #THIS BUTTON IS USED TO EXIT FROM THE WINDOW
    B7 = Button(root2,text ="EXIT",relief='raised',font=('Arial',20), bd=3,command=displaying3)
    B7.pack(side=BOTTOM) 

    root2.mainloop()


#THIS FUNCTION IS USED TO CLOSE THE MAIN WINDOW 
def displaying3():
    global root1
    root1.destroy()


#DEFINING THE MAIN WINDOW
global root1
root1=Tk()
root1.geometry('1300x1000')#SIZE OF WINDOW
root1.configure(background="#9999ff")


#THIS IS THE HEADING OF THE MAIN WINDOW
time_str1='Markov Random Field Predictive Modeling'
label_font = ('helvetica', 30)
Label(root1, text=time_str1, font=label_font, bg='white', 
         fg='#666666', relief='raised', bd=3).pack(fill='x', padx=5, pady=5)


#A TEXT FIELD
text1=Text(root1,height=5,width=800,font=('Arial',20))
text1.tag_configure('bold',font=('Arial',24,'bold'))
text1.pack(padx=10, pady=10)
ss1=""
ss1="""Markov Random Fields(MRF) are widely used in probabilistic models of "prior knowledge",which are used for regularization in a variety of computer vision problems,in particluar those with low level vision.
MRF are particularly used in prediction and super resolution of images."""
text1.insert(END,ss1)

#A TEXT FIELD
text2=Text(root1,height=5,width=800,font=('Arial',20))
text2.tag_configure('bold',font=('Arial',24,'bold'))
text2.pack(padx=10, pady=10)
ss2=""
ss2="""In image prediction we set up a intial matrix then we calculate the transition matrix which tells us how the pixels many have changed. Then we view the observation matrix which contains the neighboring pixels and on these trends we predict the image."""
text2.insert(END,ss2)

#BUTTON WHICH TAKES US TO PREDICTION WINDOW
B = Button(root1, text ="PREDICTION",font=('Arial',20),relief='raised', bd=3,command=displaying1)
B.pack(padx=5, pady=5)

#A TEXT FIELD
text3=Text(root1,height=5,width=800,font=('Arial',20))
text3.tag_configure('bold',font=('Arial',24,'bold'))
text3.pack(padx=10, pady=10)
ss3=""
ss3="""Super resolution mapping is a method in the remote sensing area where mixed pixels are divided into subpixels and for which every subpixel will be classified.Several methods are available for optimizing the image. We use Markov Random Field for super resolution to determine the final result."""
text3.insert(END,ss3)

#BUTTON WHICH TAKES US TO SUPER RESOLUTION WINDOW
B1 = Button(root1, text ="SUPER RESOLUTION",font=('Arial',20),relief='raised', bd=3,command=displaying2)
B1.pack(padx=10, pady=10)


#BUTTON WHICH IS USED TO EXIT FROM THE MAIN WINDOW
B2 = Button(root1, text ="EXIT",relief='raised',font=('Arial',20), bd=3,command=displaying3)
B2.pack(padx=10, pady=10)

root1.mainloop()

#END
