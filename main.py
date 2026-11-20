import os,json
from urllib.request import Request,urlopen
B=os.environ["MAKEFUN_ENV_URL"]
def P(p,d):
 for _ in range(9):
  try:return json.load(urlopen(Request(B+p,json.dumps(d).encode(),{"Content-Type":"application/json"}),timeout=9))
  except Exception:pass
V=[0,100,320,330,500,900,0]
ND=((1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1))
DD=((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
CR=bytearray(b"\xff"*64)
CR[0]=253;CR[4]=252;CR[7]=254;CR[56]=247;CR[60]=243;CR[63]=251
b=[0]*64;t=1;c=0;e=-1;K=[60,4];S=[]
CAP=30000;N=0;H=[0]*4096
def load(f):
 global b,t,c,e
 b=[0]*64;a=f.split();i=0
 for x in a[0]:
  if x=="/":continue
  if x.isdigit():i+=int(x)
  else:
   p="pnbrqk".find(x.lower())+1
   b[i]=p if x.isupper() else -p
   if p==6:K[0 if x.isupper() else 1]=i
   i+=1
 t=1 if a[1]=="w" else -1
 c=sum(1<<j for j,x in enumerate("KQkq")if x in a[2])
 e=-1 if a[3]=="-" else(8-int(a[3][1]))*8+ord(a[3][0])-97
 H[:]=[0]*4096
def gen():
 M=[]
 for s in range(64):
  p=b[s]
  if p*t<1:continue
  y=abs(p);r,f=divmod(s,8)
  if y==1:
   d=-t;rr=r+d
   if 0<=rr<8:
    q=s+d*8
    if not b[q]:
     if rr in(0,7):
      for u in(2,3,4,5):M.append(s*64+q|u<<12)
     else:
      M.append(s*64+q)
      if r in(1,6)and not b[q+d*8]:M.append(s*64+q+d*8)
    for x in(-1,1):
     if 0<=f+x<8:
      q=s+d*8+x
      if b[q]*t<0 or q==e:
       if rr in(0,7):
        for u in(2,3,4,5):M.append(s*64+q|u<<12)
       else:M.append(s*64+q)
  else:
   ds=ND if y==2 else DD[4:]if y==3 else DD[:4]if y==4 else DD
   for dr,df in ds:
    rr,ff=r+dr,f+df
    while 0<=rr<8 and 0<=ff<8:
     q=rr*8+ff;v=b[q]
     if v*t>0:break
     M.append(s*64+q)
     if v or y<3 or y>5:break
     rr+=dr;ff+=df
 if t>0:
  if c&1 and b[63]==4 and not(b[61]or b[62]):M.append(3840+62)
  if c&2 and b[56]==4 and not(b[57]or b[58]or b[59]):M.append(3840+58)
 else:
  if c&4 and b[7]==-4 and not(b[5]or b[6]):M.append(256+6)
  if c&8 and b[0]==-4 and not(b[1]or b[2]or b[3]):M.append(256+2)
 return M
def mk(m):
 global t,c,e
 f=m>>6&63;q=m&63;pr=m>>12
 p=b[f];S.append((f,q,p,b[q],c,e,K[0],K[1]))
 b[q]=p;b[f]=0
 if abs(p)==1 and q==e and not b[q]:b[q+t*8]=0
 if pr:b[q]=pr*t
 if abs(p)==6:
  K[p>0]=q
  c&=12 if p>0 else 3
  if abs(q-f)==2:
   if q>f:b[q-1]=b[q+1];b[q+1]=0
   else:b[q+1]=b[q-2];b[q-2]=0
 c&=CR[f]&CR[q]
 e=(f+q)//2 if abs(p)==1 and abs(q-f)==16 else -1
 t=-t
def un():
 global t,c,e
 f,q,p,v,c,e,k0,k1=S.pop()
 b[f]=p;b[q]=v
 if abs(p)==1 and not v and q%8!=f%8:b[q-t*8]=-t
 if abs(p)==6 and abs(q-f)==2:
  if q>f:b[q+1]=b[q-1];b[q-1]=0
  else:b[q-2]=b[q+1];b[q+1]=0
 K[0]=k0;K[1]=k1
 t=-t
def ev():
 s=0
 for i in range(64):
  p=b[i]
  if p:
   j=i if p>0 else i^56
   y=abs(p);r=j>>3;f=j&7;v=V[y]
   if y==1:v+=6*r-2*abs(f-3.5)
   elif y==4:v+=2*r
   else:v+=(8,3,0,2,-8)[y-2]*(3-abs(r-3.5)-abs(f-3.5))
   s+=v if p>0 else-v
 return s*t
def sc(m):
 v=b[m&63]
 return (m>>12)*1000+(H[m&4095]>>4)+(900+abs(v)*10-abs(b[m>>6&63])if v else 0)
def ne(a,be,d):
 global N,H
 s=ev()
 if d<1:
  if s>=be:return be
  if s>a:a=s
  if d<-3:return a
 N+=1
 if N>CAP:raise EOFError
 bst=-99999;n=0
 for m in sorted(gen(),key=sc,reverse=True):
  if d<1 and not(b[m&63]or m>>12):continue
  v=b[m&63];mk(m)
  if abs(v)==6:un();return 30000-d
  n=1;x=-ne(-be,-a,d-1);un()
  if x>bst:
   bst=x
   if x>a:
    a=x
    if a>=be:
     H[m&4095]+=d*d
     break
 return a if d<1 else(bst if n else-30000+d)
def mv(u):
 f=(8-int(u[1]))*8+ord(u[0])-97;q=(8-int(u[3]))*8+ord(u[2])-97
 return f<<6|q|(("??nbrq".find(u[4])if len(u)>4 else 0)<<12)
def best(L,d):
 M=[(u,mv(u))for u in L]
 M.sort(key=lambda x:sc(x[1]),reverse=True)
 bs=-1e9;bu=M[0][0]
 for u,m in M:
  mk(m);x=-ne(-1e9,-bs,d-1);un()
  if x>bs:bs=x;bu=u
 return bu
if __name__=="__main__":
 g=P("/game",{})
 while g["status"]!="done":
  if g["status"]=="your_move":
   load(g["fen"]);L=g["legal_moves"];m=L[0];d=1
   try:
    while L and d<6:
     N=0;m=best(L,d);d+=1
   except EOFError:pass
   g=P("/move",{"game":g["game"],"move":m})
  else:g=P("/game",{})
