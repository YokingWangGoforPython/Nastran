# -*- coding: utf-8
'''
Created on %(date)
@author:Yujin Wang
'''
import time
import numpy as np,pandas as pd 
from operator import itemgetter,attrgetter
from scipy import signal
from Post import *

class basic():
	'''This is the base class for for the module'''
	try:
		def __init__(self,src,des,flag1,flag2,flag3):
			self.src = src
			self.des = des
			self.flag1 = flag1
			self.flag2 = flag2
			self.flag3 = flag3
			self.time = time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))
	except:
		print ("Some arguments don't be inputted! Please! LOL!")

class nodout_SMP(basic):
	'''This class is used 4 share memory process!'''
	@property
	def simply(self):
		self.data1 = []
		self.data2 = []
		for line in open(self.src):
			if ('time' in line):
				timestep = float(line[105:116])
			elif (len(line) == 155):
				string1 = []
				string1.append(timestep)
				string1.append(int(line[:10]))
				for i in range(12):
					string1.append(float(line[(11+i*12):(22+i*12)]))
				self.data1.append(string1)
			elif (len(line)==119 and 'n' not in line):
				string2 = []
				for i in range(3):
					string2.append(float(line[(11+i*12):(22+i*12)]))
				self.data2.append(string2)
		res1 = pd.DataFrame(self.data1,columns=['Xcor','Node','x-disp','y-disp','z-disp','x-vel','y-vel','z-vel','x-accl','y-accl','z-accl','xc','yc','zc'])
		res2 = pd.DataFrame(self.data2,columns=['x-rot','y-rot','z-rot'])
		res.merge(res1,res2,left_index=True,right_index=True)
		return res

class nodout_MPP(basic):
	'''This class is used 4 share memory process!'''
	@property
	def simply(self):
		self.data1 = []
		self.data2 = []
		for line in open(self.src):
			if ('time' in line):
				timestep = float(line[104:116])
			elif (len(line) == 155):
				string1 = []
				string1.append(timestep)
				string1.append(int(line[:10]))
				for i in range(12):
					string1.append(float(line[(10+i*12):(22+i*12)]))
				self.data1.append(string1)
			elif (len(line)==119 and 'n' not in line):
				string2 = []
				for i in range(3):
					string2.append(float(line[(10+i*12):(22+i*12)]))
				self.data2.append(string2)
		res1 = pd.DataFrame(self.data1,columns=['Xcor','Node','x-disp','y-disp','z-disp','x-vel','y-vel','z-vel','x-accl','y-accl','z-accl','xc','yc','zc'])
		res2 = pd.DataFrame(self.data2,columns=['x-rot','y-rot','z-rot'])
		res.merge(res1,res2,left_index=True,right_index=True)
		return res

		class Rep4FRB(basic):
		'''It is used to achieve the FRB results from nodal file'''
			def Rep4Dis
			'''It is used to calculate the node displacement in tracking system'''
			scalename = self.flag1
			list1 = self.flag2
			refnum = self.flag3
			data1 = self.src
			reld = []
			for nodenum in list1:
				title = str(nodenum) + scalename
				inputdata = plotdata(data1,nodenum,scalename)
				if scalename in ['x-disp','y-disp','z-disp']:
					inputdata.iloc[:,1] = rel_disp(data1,nodenum,refnum)
				figure = plot(title,'Time','Disp','k',1,1,'111',inputdata)
				reld.append([nodenum,figure.reldis()[0],figure.reldis()[1]])#plot
				res = pd.DataFrame(reld,columns=[scalename,'Max','Min'])
			max_y = max(res['MAX'])#Find the maximum value
			max_xid = res['MAX'].idmax()
			max_x = res[scalename][max_xid]
			node_maxdis = reld
			reld = []
			plt.clf()
			title = str(max_x) + scalename
			inpoutdata.iloc[:,1] = rel_disp(data1,max_x,refnum)
			figure = plot(title,u'时间/s',u'侵入量/mm','k',1,1,'111',inputdata)
			reld.append([max_x,figure.reldis()[0],figure.reldis()[1]])
			string = 'Max rel_Disp:\n %10.2f	@	%10d\n' %(max_y,max_x)
			plt.savefig('Displacement figure.png',dpi=1000)
			return string,node_maxdis

		def Rep4Accl(self,accllist,period):
			'''It is used to calculate the node accelerating'''
			data1 = self.src
			res = []
			corr = {}
			for node in accllist:
				Res = plotdata(data1,node,'x-accl')
				Res.iloc[:,1] = list(cfc60(np.array(Res['x-accl']/9810.)))
				figure = plot(u'加速度',u'时间/s'，u'加速度/g',u'b',1,2,'111',Res)
				res.append(figure.accl(period))
				corr[node] = Res.iloc[:,1]
			string = 'B pillar acceleration:	%10.2f\t@%10.3f\n :%10.2f\t@%10.3f\n' %(res[0][0],res[0][1],res[1][0],res[1][1])
			return string,corr

		def Rep4Corr(self,basefile,casedata,list1,scalename,period)
			'''It is used to calculate the correlation coefficient'''
			data = nodout_MPP(basefile,'',0,0,0)
			data = data.simply
			string = ''
			for nodenum in list1:
				basedata = plotdata(data,nodenum,scalename)
				basedata.iloc[:,1] = list(cfc60(np.array(basedata['x-accl']/9810.)))
				figure = plot(u'加速度',u'时间/s'，u'加速度/g',u'b',1,2,'111',basedata)
				corr = round(np.corrcoef(casedata[nodenum],basedata.iloc[:,1][:len(casedata[nodenum])])[0][1],2)
				string += 'Correlation Coefficient(Base data) @%-8d:%5.2f\n' %(nodenum,corr)
			plt.legend('C1006','C1007','B1006','B1007').loc = 'best'
			plt.savefig('Acceleration figure.png',dpi=1000)
			return string

		def report(self,*args):
			'''The FRB report will be generated!'''
			print (len(args))
			print (self.statement)
			string1,node_maxdis = self.Rep4Dis()
			string2,corr = self.Rep4Accl([1006,1007],1,1)
			string3 = 'Correlation Coefficient(B-Pillar);\t'+str(round(np.corrcoef(corr[1006],corr[1007])[0][1],2)) + '\n'
			string4 = 'Compared files:\n'
			if len(args) > 0:
				for i in args:
					string4 += i + '\n'
					temp = self.Rep4Corr(i,corr,[1006,1007],'x-accl,1100')
					string4 += temp
			fout = open(self.des,'w')
			print (string1,string2,string3,string4)
			fout.write(string1+string2+string3+string4)
			fout.close()
			plt.show()
			return node_maxdis

		def plotdata(inputdata,nodenum,dataloc):
			'''Extract the data used for plotting from the database'''
			return inputdata[inputdata['Node'],isin([nodenum])].loc[:,['Xcor',dataloc]]

		def cfc60(data):
			'''This is a filter function used 4 handling the accelaration, which is a butterworth filter. Please refer to SAE J211-2003'''
			b,a = signal.butter(4,0.0278,'lowpass')
			return signal.filtfilt(b,a,data)

		def cfc180(data):
			'''This is a filter function used 4 handling the accelaration, which is a butterworth filter. Please refer to SAE J211-2003'''
			b,a = signal.butter(4,0.075,'lowpass')
			return signal.filtfilt(b,a,data)

		def rel_disp(data,nodenum,ref):
			'''This function is used to achieve the relative displacement in the user-defined system or a node'''
			A = np.array(data[data['Node'].isin([nodenum])].iloc[:,['xc','yc','zc']])
			O = np.array(data[data['Node'].isin([ref['O']])].iloc[:,['xc','yc','zc']])
			X = np.array(data[data['Node'].isin([ref['X']])].iloc[:,['xc','yc','zc']])
			'''预留侧碰
			Y = np.array(data[data['Node'].isin([ref['Y']])].iloc[:,['xc','yc','zc']])
			'''
			OX_mode = [sum([(X[j][i] - O[j][i])**2 for i in range(3)])**0.5 for j in range(len(x))]
			tracking_system_disX = [np.vdot(np.subtract(A[i],O[i]),np.subtract(X[i],O[i]))/OX_mode[i] for i in range(len(A))]
			tracking_system_disX = cfc180([abs(tracking_system_disX[i]-tracking_system_disX[0]) for i in range(len(tracking_system_disX))])
			return tracking_system_disX

		def rep_diff(data1,data2):
			'''This function is used to print the relation between two datas'''
			x1,y1 = maxdata(data1)
			x2,y2 = maxdata(data2)
			d1 = data1.loc[:,data1.columns[1]]
			d2 = data2.loc[:,data2.columns[1]]
			data_corr = d1.corr(d2)
			if x2*0.95<x1<x2*1.05:
				print ('#'*80)
				print ('The MAX Diffenrence : %10.5f g@ %10.5f s%(10.5f s)' %(abs(y1-y2),x1,x2))
				print ('#'*80)

		def maxdata(data):
			'''Find the maximum value and location'''
			max_y = max(data.loc[:,data.columns[1]])
			max_xcor = data.loc[:,data.columns[1]].idmax()
			max_x = data.loc[:,data.columns[0]][max_xcor]
			return max_x,max_y

		class Dyna_extr(basic):




			@property
			def subs(self):
			'''self.src = read a modified file(csv)
				self.flag1 = write a updata mainfile(Dyna)
				self.flag2 = write a updata materialfile(Dyna)
			'''
			print self.statement
			isStart = 0
			fout1 = open('New_'+self.flag1,'w')
			fout2 = open('New_' + self.flag2,'w')
			part = pd.read_csv(self.src)
			partlist = list(part.iloc[:,0])
			for line in open(self.flag1):
				if '*PART\n' in line:
					fout1.write(line)
					isStart = 1
				elif isStart == 1 and line[:10].strip().isdigit():
					if int(line[:10]) not in partlist:
						fout1.write(line)
					else:
						pos = part[part.iloc[:,0]] == int(line[:10])].iloc[0,:]
						partnum = pos[0]
						matnum = pos[2]
						secnum = pos[3]
						if self.flag3 = 'Unknown':
							string = '%10d%10d%10d\n' %(partnum,secnum,matnum)
						else:
							string = '%10d%10d' %(partnum,secnum)
						fout1.write(string+line[:20])
				elif '*' in line and 'PART' not in line:
					fout1.write(line)
					isStart = 0
				else:
					fout1.write(line)
			fout1.close()
			isStart = 1
			for line in open(self.flag2):
				if isStart == 1 and '*SECTION_SHELL_TITLE' in line:
					isStart = 0
					for i in range(len(part)):
						pos = part.iloc[i,:]
						partname = pos[1]
						secnum = pos[3]
						thick = pos[4]
						fout2.write('*SECTION_SHELL_TITLE\n')
						fout2.write(partname + '\n')
						fout2.write('$#	secid	elform	shrf	nip	propt	qr/irid	icomp	setyp\n')
						fout2.write('%10d	2	0.83333	3	0	0	0	0\n' %secnum)
						fout2.write('$#	t1	t2	t3	t4	nloc	marea	idof	edgset\n')
						fout2.write('%10f%10f%10f%10f	0.00	0.00	1.000000	0\n' %(thick,thick,thick,thick))
						fout2.write('*SECTION_SHELL_TITLE\n')
				else:
					fout2.write(line)
			fout2.close()
			data = [[part.iloc[i,5],part.iloc[i,4]] for i in range(len(part))]
			return data

		class clearresidual(basic):
			@property
			def run(self):
				fout = open(self.des,'w')
				for line in open(self.src):
					if line[0] != self.flag1:
						fout.write(line)
				fout.close()
