import time
#here u hve to chose wht u wnt
c=int(input("enter 1 for encoding a message and 2 for decoding a message:\n"))
time.sleep(0.5)
if c==1:
  def dec2bin(n):
    return bin(n).replace("0b","") 
#option 1
  st=input("enter a message to be encoded: \n")
  encode=""
  encbin=""
  for i in st:
    encode+=str(ord(i)+1)+","
  s=""
  for i in encode:
    if i!=",":
      s=s+i
    else:
      encbin+=dec2bin(int(s))+","
      s=""
  print(encbin)
  
elif c==2:
  
  def Bin2Dec(a):
    a=str(a)
    return int(a,2)
#option 2
  st1=input("enter the encoded message\n")
  s1=""
  decode=""
  d=""
  for i in st1:
    if i!=",":
      s1=s1+i
    else:
      d=d+str(Bin2Dec(int(s1)))+","
      s1=""
  s1=""
  for i in d:
    if i!=",":
      s1=s1+i
    else:
      decode=decode+chr(int(s1)-1)
      s1=""
  print (decode)