# -*- coding: utf-8 -*-

#
#	Autor: Paweł FIK
#	Akademia Marynarki Wojennej
#
#	ver. 0.0.2 - 15.05.2013
#

import os
import sys
import matplotlib.pylab as plt
from PIL import Image
from visualization.images2gif import writeGif

steps = {}
tempDir = "temp"

def animate(sequence, name):
	"""Tworzy serię plików PNG 
	"""
	
	if steps.has_key(name):
		step = steps[name]
		steps[name] += 1
	else:
		step = 0
		steps[name] = 0
  
	ax = plt.subplot(111)
	ax.plot(range(len(sequence)), sequence, "b.")
	ax.set_title(name.replace("_", " "))  
	ax.set_xlabel("Indeks w tablicy")
	ax.set_ylabel(u"Wartosć")
	
	fileName = '%s_%05d.png'%(name, step)
	tempFileDir = os.path.join(tempDir, fileName)
	plt.savefig(tempFileDir)
	plt.clf()
	print "Zapisuje plik: %s"%fileName
	
def makeGIF(fileName):
		"""Z plików PNG tworzy plik GIF
		Użyłem tutaj zewnętrznego modułu images2gif.py do konwersji PNG do GIF
		(nie wiem czy tag mogę zrobić bo ten moduł nie jest napisany przeze mnie)
		"""
		
		files = sorted((fn for fn in os.listdir(tempDir) if fn.endswith('.png')))
		#print "%s"%tempDir
		#print "%s"%files
		images = [Image.open(os.path.join(os.path.abspath('.'),tempDir,fn)) for fn in files]
		try:
				print u"Tworzę plik GIF - %s"%fileName
				writeGif(fileName, images, duration=0.6)
				try:
						#os.remove(os.path.join(os.path.abspath('.'),tempDir,f)) for f in os.listdir(tempDir) if f.endswith('.png')
						
						for f in files: 
							if f.endswith(".png"): 
								os.unlink(os.path.join(os.path.abspath('.'),tempDir,f))
							
				except:
						print u"Nie mogę usunąć plików."
		except:
				print u"Problem z konwersją."