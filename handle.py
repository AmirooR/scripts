#!/usr/bin/env python

import math
from random import randint
def inc_example_indexes(filename,outname):
	"""Parses an input file into an example sequence."""
	# This reads example files of the type read by SVM^multiclass.
	examples = []
	i = 0
	fw = open(outname,'w')
	# Open the file and read each example.
	for line in file(filename):
		# Get rid of comments.
		print i
		i = i + 1
		if line.find('#'): line = line[:line.find('#')]
		tokens = line.split()
		# If the line is empty, who cares?
		if not tokens: continue
		# Get the target.
		target = float(tokens[0])
	        # Get the features.
		tokens = [t.split(':') for t in tokens[1:]]
		fw.write(repr(target) + ' ')
		for k,v in tokens:
			fw.write(repr(int(k)+1))
			fw.write(':')
			fw.write(v)
			fw.write(' ')
		fw.write('\n')
	fw.close()
	#read_examples('all.building.depth.txt','all.building.depth.changed400.txt')

def subsetFromListFile(listFile, num, total,  selectedList, restList):
	i = 0
	k = num
	l = total
	selected  = range(l)
	for i in range(l):
		if randint(0,l-i-1) < k:
			#selected.append(i)
			selected[i] = 1
			k = k - 1
		else: selected[i] = 0
		i = i + 1
	i=0
	fwListSel = open(selectedList,'w')
	fwListRest = open(restList,'w')
	for line in file(listFile):
		print i
		x = line[13:len(line)-5]+'-resized\n'
		if selected[i] == 1:
			fwListSel.write(x)
		else: 
			fwListRest.write(x)
		i = i + 1
	fwListRest.close()
	fwListSel.close()

def subset_selectFile(listFile, num, total, selectedFile, restFile, selectedList, restList, inc):
	i = 0
	k = num
	l = total
	selected  = range(l)
	for i in range(l):
		if randint(0,l-i-1) < k:
			#selected.append(i)
			selected[i] = 1
			k = k - 1
		else: selected[i] = 0
		i = i + 1
	i=0
	fwRest = open(restFile,'w')
	fwSel = open(selectedFile,'w')
	fwListSel = open(selectedList,'w')
	fwListRest = open(restList,'w')
	for line in file(listFile):
		print i
		if selected[i] == 1:
			fw = fwSel
			fwListSel.write(line)
		else: 
			fw = fwRest
			fwListRest.write(line)
		line = line[:len(line)-1]
		for eachLine in file(line):
			tokens = eachLine.split()
			if not tokens: continue
			target = float(tokens[0])
	        	# Get the features.
			tokens = [t.split(':') for t in tokens[1:]]
			fw.write(repr(target) + ' ')
			for k,v in tokens:
				tt = int(k)
				if inc:
					tt = tt + 1
				fw.write(repr(tt))
				fw.write(':')
				fw.write(v)
				fw.write(' ')
			fw.write('\n')
		i = i + 1
	fwRest.close()
	fwSel.close()
	fwListRest.close()
	fwListSel.close()


#selected.append( randint(0, total))
#	for line in file(listFile):
#		print i
#		i = i + 1

def filter_dataset(inputFile,outFile,restFile,eval_string):
	i = 0
	fwOut = open(outFile,'w')
	fwRest = open(restFile,'w')
	for line in file(inputFile):
		print i
		i = i + 1
		tokens = line.split()
		if not tokens: continue
		target = float(tokens[0])
		tokens = [t.split(':') for t in tokens[1:]]
		if eval(eval_string):
			fw = fwOut
		else:	fw = fwRest
		fw.write(repr(target) + ' ')
		for k,v in tokens:
			fw.write(repr(int(k)+1))
			fw.write(':')
			fw.write(v)
			fw.write(' ')
		fw.write('\n')
	fwOut.close()
	fwRest.close()



def write_multi_out(inputFile, targetFile, multiclassFile, multiclassTargetFile, logFile, logTargetFile):
	"""Parses an input file into log,multiclass, and their target files."""
	# This reads example files of the type read by SVM^multiclass.
	examples = []
	i = 0
	fwTarget = open(targetFile,'w')
	fwMultiClass = open(multiclassFile,'w')
	fwLog = open(logFile,'w')
	fwLogTarget = open(logTargetFile,'w')
	fwMCTarget = open(multiclassTargetFile,'w')
	# Open the file and read each example.
	for line in file(inputFile):
		# Get rid of comments.
		print i
		i = i + 1
		if line.find('#'): line = line[:line.find('#')]
		tokens = line.split()
		# If the line is empty, who cares?
		if not tokens: continue
		# Get the target.
		target = float(tokens[0])
	        # Get the features.
		tokens = [t.split(':') for t in tokens[1:]]
		#features = [(int(k)+1,float(v)) for k,v in tokens]
		# Add the example to the list
		#examples.append((features, target))
		#print target, features
		fwTarget.write(repr(target) + '\n')
		logtarget = math.log(target)
		fwLogTarget.write(repr(logtarget)+'\n')
		fwLog.write(repr(logtarget)+' ')
		mctarget = 0
		if target > 40.0:
			mctarget = 1
		elif target > 20.0:
			mctarget = 2
		elif target > 10.0:
			mctarget = 3
		elif target > 5.0:
			mctarget = 4
		elif target > 2.5:
			mctarget = 5
		else: 
			mctarget = 6
		fwMCTarget.write(repr(mctarget)+'\n')
		fwMultiClass.write(repr(mctarget)+' ')
		for k,v in tokens:
			fwMultiClass.write(repr(int(k))+':'+v+' ')
			fwLog.write(repr(int(k))+':'+v+' ')
			#fw.write(repr(int(k)))
			#fw.write(':')
			#fw.write(v)
			#fw.write(' ')
		fwMultiClass.write('\n')
		fwLog.write('\n')
	# Print out some very useful statistics.
	#print len(examples),'examples read'
	#return examples
	fwLog.close()
	fwMultiClass.close()
	fwTarget.close()
	fwLogTarget.close()
	fwMCTarget.close()
#(inputFile, targetFile, multiclassFile, multiclassTargetFile, logFile, logTargetFile)

#write_multi_out('all.building.depth.changed400.txt','target.raw.txt','multiclass.txt','target.multiclass.txt','log.all.txt','target.log.txt')

#filter_dataset(inputFile,outFile,restFile,eval_string)
#filter_dataset('log.all.txt','below_79.log.txt','above_79.log.txt','target < math.log(80)')
#subset_selectFile(listFile, num, total, selectedFile, restFile, selectedList, restList, inc)
#subset_selectFile('groundList.txt',300,400,'ground.selected.all.txt','ground.rest.all.txt','ground.selected.list.txt','ground.rest.list.txt',True)
subsetFromListFile('ground.selected.list.txt', 100, 300,  'sameWall.sel100From300.txt', 'sameWall.sel200From300.txt')

