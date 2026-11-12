import json,os,urllib.request as U
E=os.environ["MAKEFUN_ENV_URL"]
P=".1pnbrqk4PNBRQK"
V={"p":100,"n":320,"b":330,"r":500,"q":900,"k":0}
C=[0,1,2,3,4,5,6,7]
def q(path,body):
 r=U.Request(E+path,json.dumps(body).encode(),{"Content-Type":"application/json"})
 return json.load(U.urlopen(r,timeout=9))
def s2(f,r):return r*8+f
def F2(s):
 b=["."]*64;r=7;f=0
 for c in s.split()[0]:
  if c=="/":r-=1;f=0
  elif c.isdigit():f+=int(c)
  else:b[s2(f,r)]=c;f+=1
 return b,s.split()[1]=="w"
def A2(b,s,by):
 p=b[s]
 for i in range(64):
  q=b[i]
  if q=="." or q.isupper()!=by:continue
  d=abs(i%8-s%8);e=abs(i//8-s//8);t=q.lower()
  if t=="p":
   if by and s//8-i//8==1 and d==1:return 1
   if not by and i//8-s//8==1 and d==1:return 1
  elif t=="n":
   if (d,e)in((1,2),(2,1)):return 1
  elif t in"kq":
   if max(d,e)==1 or (t=="q" and (d==0 or e==0 or d==e)):return 1
  elif t in"rb":
   if t=="r"and(d==0 or e==0)or t=="b"and d==e:
    if c2(b,i,s):return 1
 return 0
def c2(b,a,z):
 d=abs(a%8-z%8);e=abs(a//8-z//8);n=max(d,e)
 if not(d==0 or e==0 or d==e):return 0
 x=(z%8-a%8)//n if n else 0;y=(z//8-a//8)//n if n else 0
 for k in range(1,n):
  if b[s2(a%8+x*k,a//8+y*k)]!=".":return 0
 return 1
def M2(b,side):
 out=[]
 for i in range(64):
  p=b[i]
  if p=="."or p.isupper()!=side:continue
  t=p.lower();f=i%8;r=i//8
  st=[]
  if t=="p":
   d=1 if side else -1
   if 0<=r+d<8 and b[s2(f,r+d)]==".":
    st.append(s2(f,r+d))
    if r==(1 if side else 6)and b[s2(f,r+2*d)]==".":st.append(s2(f,r+2*d))
   for df in(-1,1):
    if 0<=f+df<8 and 0<=r+d<8:
     j=s2(f+df,r+d)
     if b[j]!="."and b[j].isupper()!=side:st.append(j)
  elif t=="n":st=[s2(f+a,r+c)for a,c in((1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1))if 0<=f+a<8 and 0<=r+c<8]
  elif t in"kq":
   for a in range(-1,2):
    for c in range(-1,2):
     if a or c:
      if 0<=f+a<8 and 0<=r+c<8:st.append(s2(f+a,r+c))
      if t=="q":
       k=1
       while 0<=f+a*k<8 and 0<=r+c*k<8:
        j=s2(f+a*k,r+c*k)
        if b[j]!=".":
         if b[j].isupper()!=side:st.append(j)
         break
        st.append(j);k+=1
  elif t in"rb":
   for a,c in((1,0),(-1,0),(0,1),(0,-1))if t=="r"else((1,1),(1,-1),(-1,1),(-1,-1)):
    k=1
    while 0<=f+a*k<8 and 0<=r+c*k<8:
     j=s2(f+a*k,r+c*k)
     if b[j]!=".":
      if b[j].isupper()!=side:st.append(j)
      break
     st.append(j);k+=1
  for j in st:
   if b[j]!="."and b[j].isupper()==side:continue
   n=b[:];n[j]=n[i];n[i]="."
   if t=="p"and j//8 in(0,7):n[j]="Q"if side else"q"
   if t=="k"and abs(j%8-i%8)>1:
    if j%8>i%8:n[i+3]=n[i+1];n[i+1]="."
    else:n[i-4]=n[i-1];n[i-1]="."
   out.append((i,j,n))
 return out
def u2(i,j):
 s="abcdefgh"
 return s[i%8]+str(i//8+1)+s[j%8]+str(j//8+1)
def e2(b):
 v=0
 for i,p in enumerate(b):
  if p==".":continue
  x=V[p.lower()];d=3.5-abs(i%8-3.5)/2-abs(i//8-3.5)/2
  v+=x+d if p.isupper()else-(x+d)
 return v
def L2(b,side):
 return[(i,j,n)for i,j,n in M2(b,side)if not A2(n,k2(n,side),not side)]
def k2(b,side):
 for i,p in enumerate(b):
  if p==("K"if side else"k"):return i
 return 0
def Q2(b,side,d,a,z):
 v=e2(b)
 if d<=0:return v
 if v>=z:return v
 if v>a:a=v
 for i,j,n in L2(b,side):
  if b[j]=="."and b[i].lower()!="p":continue
  v=-Q2(n,not side,d-1,-z,-a)
  if v>a:a=v
  if a>=z:break
 return a
def S2(b,side,d,a,z):
 if d==0:return Q2(b,side,2,a,z)
 m=L2(b,side)
 if not m:return -9999 if A2(b,k2(b,side),not side)else 0
 m.sort(key=lambda x:-abs(V.get(b[x[1]].lower(),0)))
 for i,j,n in m:
  v=-S2(n,not side,d-1,-z,-a)
  if v>a:a=v
  if a>=z:break
 return a
def p2(b,side):
 best=None;bs=-1e9
 for i,j,n in L2(b,side):
  v=-S2(n,not side,2,-1e9,1e9)
  if v>bs:bs=v;best=u2(i,j)
 return best
g=0
while 1:
 r=q("/game",{})
 if r.get("status")=="done":break
 if r.get("status")!="your_move":continue
 b,side=F2(r["F2"])
 m=p2(b,side)
 r=q("/move",{"game":r["game"],"move":m})