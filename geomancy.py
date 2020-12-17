import random
class Geo:
	self.counter=0
		
	def dots(self):
		selections = []
		for i in range(16):
			x= random.randint(1, 16)
			selections.append(x)
		return selections
	
	def sRes(self, array):
		return (i%2 for i in array)
			
	def __iter__(self):
		return self.sRes(self.dots())
	
	def filia(self, array, n):
		s=[]
		length=0
		while length < len(array):
			length+=n
			sv = length - n
			s.append(array[sv:length])
		return s

	def mothers(self):
		z=list(self)
		a=self.filia(z, 4)
		return  a
		
	def daughters(self):
		d=self.mothers()
		s, t, u, v = d
		d1, d2=map(sum, zip(s,t)), map(sum, zip(u,v))
		return (i%2 for i in d1), (i%2 for i in d2)
		
	def judge(self):
		a, b =map(list, self.daughters())
		c = map(sum, zip(a,b))
		return (i%2 for i in c)
	
	def mancy(self):
		r1 = self.dots()
		r2= list(self)
		r3 = self.mothers()
		r4 = list(map(list, self.daughters()))
		r5 = list(self.judge())
		f1=f"Random Samples(16)=>{r1}"
		f2=f"Cleaned data => {r2}"
		f3 = f"mothers => {r3}"
		f4 = f"daughters => {r4}"
		f5 = f"Judge => {r5}"
		print(f1, f2, f3, f4, f5, sep="\n")

geo=Geo()	
geo.mancy()

class Meaning(Geo):
	def __init__(self):
		self.geo = Geo()
		self.conv = dict(puer=(1,1,0,1),
				 fortuna_major=(0,0,1,1),
				 acquisitio=(0,1,0,1),
				 cauda_draconis = (1,1,1,0),
				 albus=(0,0,1,0),
				 puella=(1,0,1,1),
				 tristitia=(0,0,0,1),
				 fortuna_minor =(1,1,0,0),
				 populus=(0,0,0,0),
				 rubeus=(0,1,0,0),
				 laetitia=(1,0,0,0),
				 via=(1,1,1,1),
				 amisio = (1,0,1,0),
				 conjunctio = (0,1,1,0),
				 cancer = (1,0,0,1),
				 capus_draconis = (0,1,1,1)
				)
	
	def __call__(self):
		return geo
	
	def __comp__(self, filia):
		for (u, v) in self.conv.items:
			if v == filia:
				return u.replace('_', ' ')
			
	
			
