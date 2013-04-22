import sys
import numpy as np
f = open('labelList.dat')
ls = f.readlines()
i = 0
for x in ls:
	i = i + 1;
	print repr(i) + '\n'
	a = x[:len(x)-1]
	b = a[:len(a)-3] + 'seg'
	labArr = np.loadtxt(a,dtype=int)
	fw = open(b,'w')
	normArr = labArr
	dic = {}
	num_lab = -1
	for r in range(labArr.shape[0]):
		for c in range(labArr.shape[1]):
			if dic.has_key(labArr[r,c]):
				normArr[r,c] = dic[labArr[r,c]]
			else:
			 	num_lab = num_lab+1
			 	dic[labArr[r,c]] = num_lab
			 	normArr[r,c] = num_lab
			fw.write(repr(normArr[r,c])+' ')
		fw.write('\n')
	#normArr.tofile(b," ")
	fw.close()
f.close()

