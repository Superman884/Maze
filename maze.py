from time import time
from time import sleep
from PIL import Image
t=time()
url='maze.png'
print('reading image')
wid=Image.open(url).size[0]
hei=Image.open(url).size[1]
pixels=[Image.open(url).load()[x,y] for y in range(Image.open(url).size[0]) for x in range(Image.open(url).size[1])]
real=[]
stuff=[]
for k in pixels:
	if k==(0, 0, 0) or k==(0,0,0,255):
		real.append(0)
	elif k==(255,255,255) or k==(255,255,255,255):
		real.append(1)
	else:
		real.append(2)
class node():
	def __init__(self,pos,connects):
		self.pos=pos
		self.connects=connects
		self.connectors=None
		self.cost=10000
		self.path=[]
		self.dist=0
im=Image.open(url)
pix=im.load()
im.save('maze_nodes.png')
counter=0
sren=[]
noding=[]
for k in range(len(real)):
	if real[k]==2:
		stuff.append((k%wid,k//wid))
		sren.append((k%wid,k//wid))

	if real[k]==1:
		if (real[k-1]!=0 and real[k-wid]!=0) or (real[k+1]!=0 and real[k-wid]!=0) or (real[k-1]!=0 and real[k+wid]!=0) or (real[k+1]!=0 and real[k+wid]!=0):
			stuff.append((k%wid,k//wid))
im.save('maze_nodes.png')
nodes=[node(k,None) for k in stuff]
print('creating time:',time()-t)
print('joining nodes')
t=time()
for i in nodes:
	joined=[]
	coined=[]
	#up
	currpos=i.pos[1]-1
	while True:
		if (i.pos[0],currpos) in stuff:
			k=stuff.index((i.pos[0],currpos))
			joined.append(nodes[k])
			coined.append(k)
			break
		try:
			if real[i.pos[0]+currpos*wid]==0:
				break
		except:
			break
		currpos-=1
		#up
	currpos=i.pos[1]+1
	while True:
		if (i.pos[0],currpos) in stuff:
			k=stuff.index((i.pos[0],currpos))
			joined.append(nodes[k])
			coined.append(k)
			break
		try:
			if real[i.pos[0]+currpos*wid]==0:
				break
		except:
			break
		currpos+=1
		#up
	currpos=i.pos[0]+1
	while True:
		if (currpos,i.pos[1]) in stuff:
			k=stuff.index((currpos,i.pos[1]))
			joined.append(nodes[k])
			coined.append(k)
			break
		try:
			if real[currpos+i.pos[1]*wid]==0:
				break
		except:
			break
		currpos+=1
	#up
	currpos=i.pos[0]-1
	while True:
		if (currpos,i.pos[1]) in stuff:
			k=stuff.index((currpos,i.pos[1]))
			joined.append(nodes[k])
			coined.append(k)
			break
		try:
			if real[currpos+i.pos[1]*wid]==0:
				break
		except:
			break
		currpos-=1
	i.connects=joined
	i.connectors=coined
#pathfinding
astar=True
nodes[0].cost=0
nodes[0].path=['startfun!']
low=0
desired=sren[-1]
required=stuff.index(desired)
count=0
change=0
if astar:
	for m in nodes:
		m.dist=((m.pos[0]-nodes[required].pos[0])**2+(m.pos[1]-nodes[required].pos[1])**2)**0.5
lows=[]
a=0
b=0
print('joining time:',time()-t)
print('pathfinding')
to_explore=[0]
loss=0
while nodes[required-change].path==[]:
	a1=time()
	for childs in range(len(nodes[low].connects)):
		child=nodes[low].connects[childs]
		childy=nodes[low].connectors[childs]
		if True:
			newcost=nodes[low].pos[0]-child.pos[0]+nodes[low].pos[1]-child.pos[1]
			if newcost<0:
				newcost=newcost*(-1)
		newcost=newcost+nodes[low].cost
		if newcost<child.cost:
			child.cost=newcost
			child.path=nodes[low].path+[low]
			to_explore.append(childy)
	mincost=10000
	count+=1
	lows.append(low)
	to_explore.pop(loss)
	a+=time()-a1
	b1=time()
	for y in range(len(to_explore)):
		x=to_explore[y]
		if x in lows:
			continue
		if nodes[x].cost+nodes[x].dist<mincost:
			mincost=nodes[x].cost+nodes[x].dist
			low=x
			loss=y
	if low in lows:
		break
	b+=time()-b1
print('pathfinding time:',a+b)
print('discovering time:',a)
print('finding low:',b)
print('coloring')
nodes[-1].path.append(stuff.index(nodes[-1].pos))
# for i  in nodes:
# 	print('pos',i.pos)
# 	print('costs',i.cost)
# print(stuff)
# print(nodes[-1].cost)
for r in range(len(nodes[-1].path)-1):
	i=nodes[-1].path[r]
	j=nodes[-1].path[r+1]
	if i=='startfun!':
		continue
	i=int(i)
	j=int(j)
	if stuff[i][0]==stuff[j][0]:
		if stuff[i][1]>stuff[j][1]:
			k=-1
		else:
			k=1
		for p in range(stuff[i][1],stuff[j][1]+k,k):
			pix[stuff[i][0],p]=(0,120,0)
	else:
		if stuff[i][0]>stuff[j][0]:
			k=-1
		else:
			k=1
		for p in range(stuff[i][0],stuff[j][0]+k,k):
			pix[p,stuff[i][1]]=(0,120,0)
im.save('maze_nodes.png')
