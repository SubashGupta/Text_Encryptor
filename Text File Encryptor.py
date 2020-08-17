#Gui Part Using tkinter
from tkinter import *
root=Tk()
global inputfile,outputfile,password,var
var = IntVar()
root.title("FILE ENCRYPTOR")
root.geometry("640x640+0+0")
heading=Label(root,text="Welcome to the security app",font=("arial",25,"bold"),fg="steelblue").pack()
lalbel=Label(root,text="Input File Location : ",font=("arial",10,"bold"),fg="black").place(x=3,y=50)
inputfile=StringVar()
entry_box=Entry(root,textvariable=inputfile,width=50,bg="white").place(x=150,y=50)
lalbel=Label(root,text="Output File Location : ",font=("arial",10,"bold"),fg="black").place(x=3,y=100)
outputfile=StringVar()
entry_box=Entry(root,textvariable=outputfile,width=50,bg="white").place(x=150,y=100)
lalbel = Label(root, text="Password : ", font=("arial", 10, "bold"), fg="black").place(x=3, y=150)
password=StringVar()
entry_box = Entry(root, textvariable=password, width=50, bg="white").place(x=150, y=150)
radio_low = Radiobutton(root, text="Encrypt", variable=var, value=1)
radio_low.place(x=150,y=200)
radio_middle = Radiobutton(root, text="Decrypt", variable=var, value=0)
radio_middle.place(x=250,y=200)
def do():
    global inputfile
    print(str(inputfile.get()))
    if int(var.get())==0:
        totaldecrypt()
    elif int(var.get())==1:
        totalencrypt()
generate=Button(root,text="GENERATE",width=30,height=5,bg="grey",command=do).place(x=300,y=300)




#These are all the characters a text file could contain.
characters=["1","2","3","4","5","6","7","8","9","0","-","=","~","`","!","@","#","$","%","^","&","*","(",")","_","+","\n"," ","q","w","e","r","t","y","u","i","o","p","{","}","|","[","]","a","s","d","f","g","h","j","k","l",":",";","'",'"',"z","x","c","v","b","n","m",",",".","/","?",">","<","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
len_characters=len(characters)

#Function used to create keys for the Affine Cipher and Vignere Ciphers from Password entered by the user at the time of Encryption or Decryption.
#Passwords can be only of the length 6 or 7 or 8.
def generatekeys():
# global password
 pwd=str(password.get())
 pwd_len=len(pwd)
 multi_inverese=[]
#To Find Multiplicative inverses of the numbers in the range of characters.
#Which is not necessary for every number to have a multiplicative inverse in the given range.
#For the taken list of characters there will be only 72 integers have multiplicative inverse.
 for i in range(1,95):
    for j in range(1,95):
        if((i*j)%95==1):
            multi_inverese.append(i)
 total_inverses=len(multi_inverese)
 for i in range(total_inverses):
    print(multi_inverese[i])
 if(pwd_len==6):
    index_inverse=(ord(pwd[0])+ord(pwd[2])+ord(pwd[4])+10)%72
    add_key=(ord(pwd[1])+ord(pwd[3])+ord(pwd[5])+10)%95
    vig_key=pwd[1]+pwd[3]+pwd[4]+pwd[2]
 elif(pwd_len==7):
    index_inverse=(ord(pwd[0])+ord(pwd[2])+ord(pwd[4])+ord(pwd[6])+10)%72
    add_key=(ord(pwd[1])+ord(pwd[3])+ord(pwd[5])+10)%95
    vig_key=pwd[1]+pwd[5]+pwd[4]+pwd[0]+pwd[6]
 elif(pwd_len==8):
    index_inverse=(ord(pwd[0])+ord(pwd[2])+ord(pwd[4])+ord(pwd[6])+10)%72
    add_key=(ord(pwd[1])+ord(pwd[3])+ord(pwd[5])+ord(pwd[7])+10)%95
    vig_key=pwd[1]+pwd[6]+pwd[2]+pwd[4]+pwd[6]+pwd[5]
 mult_key=multi_inverese[index_inverse]
 return(mult_key,add_key,vig_key)


#The Double Encryption Method
def totalencrypt() :
 key1, key2, key3 = generatekeys()
 print(str(inputfile.get()))
 f=open(str(inputfile.get()),'r')
 for line in f:
  encrypt1(line,key1,key2)
 m=open("cipher.txt",'r')
 for line in m:
  encrypt2(line,key3)
 file1=open("cipher.txt",'w')
 file1.write('')
#Encryption method for Affine Cipher
def encrypt1(text, multi_k, add_k):
     # global inputfile,outputfile
     result = ""
     for i in range(len(text)):
         char = text[i]
         for j in range(len_characters):
             if (char == characters[j]):
                 q = j
         ch = (((q * multi_k) + add_k) % len_characters)
         result += str(characters[ch])
     out = open("cipher.txt", 'a')
     out.write(result)
     return result
#Encryption method for Vignere Cipher
def encrypt2(text, vig_key):
     # global inputfile, outputfile
     result = ""
     b = []
     for i in range(len(vig_key)):
         for j in range(len_characters):
             if (vig_key[i] == characters[j]):
                 b.append(j)
     pos = 0
     vig_key_len = len(vig_key)
     for i in range(len(text)):
         char = text[i]
         for l in range(len_characters):
             if (char == characters[l]):
                 ti = l
         ki = b[pos]
         ch = ((ti + ki) % len_characters)
         result += str(characters[ch])
         pos = pos + 1
         if (vig_key_len == pos or str(characters[ch]) == "\n"):
             pos = 0
     out = open(str(outputfile.get()), 'a')
     out.write(result)



def totaldecrypt():
 #global inputfile,outputfile
 key1, key2, key3 = generatekeys()
 n=open(str(inputfile.get()),'r')
 for line in n:
    decrypt2(line,key3)
 #This Loop Finds the Inverse of the Multplication key(mult_key) used for encryption
 for o in range (1,len_characters):
    if(((key1*o)%len_characters)==1):
        inv_key1=o;

 g=open("cipher.txt",'r')
 for line in g:
   decrypt1(line,inv_key1,key2)
 file1=open("cipher.txt",'w')
 file1.write('')

#Decryption method for Affine Cipher
def decrypt1(text, mult_key, add_key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        for j in range(len_characters):
            if (char == characters[j]):
                q = j
        ch = (((q - add_key) * mult_key) % len_characters)
        result += str(characters[ch])
    out = open(str(outputfile.get()), 'a')
    out.write(result)
    return result

#Decryption method for Vignere Cipher
def decrypt2(text,vig_key):
    #global inputfile,outputfile
    pwd_vig_indexes=[]
    for i in range(len(vig_key)):
        for j in range(len_characters):
            if (vig_key[i] == characters[j]):
                pwd_vig_indexes.append(j)
    result=""
    pos=0
    vig_key_len = len(vig_key)
    for i in range(len(text)):
     char=text[i]
     for l in range(len_characters):
        if(char==characters[l]):
            ti=l
     ki=pwd_vig_indexes[pos]
     ch = ((ti - ki) % len_characters)
     result += str(characters[ch])
     pos = pos+1
     if (pos == vig_key_len or characters[ch] == "\n"):
         pos = 0
    out1 = open("cipher.txt", 'a')
    out1.write(result)

#Calling the Gui
root.mainloop()