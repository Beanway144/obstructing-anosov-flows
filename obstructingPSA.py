"""
Code to find manifolds admitting no veering triangulations.
Based on Schmalian, Obstructing Anosov Flows on Cusped 3-Manifolds.

Requires Nathan Dunfield's QHSpheres.csv.bz2
"""

import pandas

qhs = pandas.read_csv('QHSpheres.csv.bz2') # takes a while to load in

def hasNoPersistentlyFoliarDC(M): # returns true if M has no persistently foliar double cover
	double_covers = M.covers(2)
	for c in double_covers:
		# be lazy: give up if a double cover has more than one cusp
		if c.num_cusps() > 1:
			return False
		# be scared: give up if snappy doesn't know what's goin on
		if len(c.identify()) == 0:
			return False
		s = str(c.identify()[0]).split('(')[0] # get name of cover
		fillings = qhs[qhs["name"].str.startswith(s)] # filter Dunfield's list to get the fillings of c
		notTaut = fillings[fillings["taut"] == -1]
		if len(notTaut) <= 1: # found a cover which is *possibly* persistently foliar
			return False
	return True

def checkCensus():
	# snappy won't recognize double covers after ~500 census manifolds
	for j in range(500):
		M = snappy.OrientableCuspedCensus[j]
		if hasNoPersistentlyFoliarDC(M):
			print(M)