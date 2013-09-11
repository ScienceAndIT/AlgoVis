# -*- coding: utf-8 -*-

#
#	Autor: Paweł FIK
#	Akademia Marynarki Wojennej
#
#	ver. 0.0.2 - 15.05.2013
#

from visualization.makeGif import *

def bubbleSort(tab): 
		for i in range(len(tab)):
			j=len(tab)-1 
			while j>i:   
				if tab[j]<tab[j-1]: 
					tmp=tab[j]
					tab[j]=tab[j-1]
					tab[j-1]=tmp
					animate(tab, "bubble_sort")
				j-=1	
		return tab