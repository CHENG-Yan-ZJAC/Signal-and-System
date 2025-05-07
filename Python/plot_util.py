#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelmin


def new_subplots(row:int, col:int):
	if row == 1 and col == 1:
		figsize = (4, 2)
	elif row == 2 and col == 1:
		figsize = (6, 4)
	elif row == 2 and col == 2:
		figsize = (8, 4)
	elif row == 2 and col == 3:
		figsize = (10, 4)
	elif row == 3 and col == 1:
		figsize = (6, 4)
	elif row == 3 and col == 2:
		figsize = (8, 4)
	else:
		print('unknown row={} and col={}'.format(row, col))
		pass
	fig, axs = plt.subplots(row, col, figsize=figsize)
	return axs


def plot_mag_phs(w:np.ndarray, mag:np.ndarray, phs:np.ndarray, mag_axs, phs_axs,
		title:str=None,
		w_xlabel:str=None, mag_ylabel:str=None, phs_ylabel:str=None,
		mag_line_fmt:str=None, mag_line_label:str=None, phs_line_fmt:str=None, phs_line_label:str=None,
		w_xlim:list=None, mag_ylim:list=None, phs_ylim:list=None,
		w_xticks_step:float=np.pi, phs_yticks_step:int=90) -> None:

	# plot
	if mag_line_fmt is not None:
		mag_axs.plot(w, mag, mag_line_fmt, label=mag_line_label)
	else:
		mag_axs.plot(w, mag)
		pass
	mag_axs.grid(True)
	if phs_line_fmt is not None:
		phs_axs.plot(w, phs, phs_line_fmt, label=phs_line_label)
	else:
		phs_axs.plot(w, phs)
		pass
	phs_axs.grid(True)

	# title
	if title is not None:
		mag_axs.set_title(title)
		pass

	# label
	if w_xlabel is not None:
		phs_axs.set_xlabel(w_xlabel)
		pass
	if mag_ylabel is not None:
		mag_axs.set_ylabel(mag_ylabel)
		pass
	if phs_ylabel is not None:
		phs_axs.set_ylabel(phs_ylabel)
		pass

	# set w lim, mag lim, phs lim
	if w_xlim is not None:
		mag_axs.set_xlim(w_xlim)
		phs_axs.set_xlim(w_xlim)
		pass
	if mag_ylim is not None:
		mag_axs.set_ylim(mag_ylim)
		pass
	if phs_ylim is not None:
		phs_axs.set_ylim(phs_ylim)
		pass

	# set w xticks
	ticks = []
	label = []
	for i in range(int(np.ceil(w[0]/np.pi)), int(np.ceil(w[-1]/np.pi))+1, int(w_xticks_step/np.pi)):
		ticks.append(i*np.pi)
		label.append(r'${}\pi $'.format(i))
		pass
	mag_axs.set_xticks(ticks, label)
	phs_axs.set_xticks(ticks, label)

	# set phs yticks
	if phs_ylim is not None:
		ticks = []
		label = []
		for i in range(0, abs(phs_ylim[0]), phs_yticks_step):
			if i != 0:
				ticks.insert(0, -i)
				label.insert(0, str(-i))
				pass
			pass
		for i in range(0, phs_ylim[1], phs_yticks_step):
			ticks.append(i)
			label.append(str(i))
			pass
		phs_axs.set_yticks(ticks, label)
		pass

	return


'''
def find_magnitude(mag:np.ndarray, dB:int) -> np.ndarray:
	# check range
	maximum = np.max(mag)
	minimum = np.min(mag)
	if dB > maximum or dB < minimum:
		print('{} out of range, {} - {}.'.format(dB, minimum, maximum))
		return None
	# find dB in mag
	temp = np.abs(mag - dB)
	idx  = argrelmin(temp) # tuple of np.ndarrays
	idx  = idx[0]          # np.ndarray
	if len(idx) == 1:
		idx = idx[0]
	else:
		idx = idx.tolist()
	return idx


def find_phase(phs:np.ndarray, deg:int) -> np.ndarray:
	# check range
	maximum = np.max(phs)
	minimum = np.min(phs)
	if deg > maximum or deg < minimum:
		print('{} out of range, {} - {}.'.format(deg, minimum, maximum))
		return None
	# find deg in phs
	temp = np.abs(phs - deg)
	idx  = argrelmin(temp) # tuple of np.ndarrays
	idx  = idx[0]          # np.ndarray
	if len(idx) == 1:
		idx = idx[0]
	else:
		idx = idx.tolist()
	return idx


def mag_annotate(mag_axs, freq:float, mag:float, xytext:list, color:str=None) -> None:
	if freq > 1e9:
		text = '{:.2f}dB\n{:.1f}GHz'.format(mag, freq/1e9)
	elif freq > 1e6:
		text = '{:.2f}dB\n{:.1f}MHz'.format(mag, freq/1e6)
	elif freq > 1e3:
		text = '{:.2f}dB\n{:.1f}kHz'.format(mag, freq/1e3)
	else:
		text = '{:.2f}dB\n{:.1f}Hz'.format(mag, freq)
	mag_axs.annotate(text, (freq,mag), xytext=xytext, arrowprops=dict(arrowstyle='->'), color=color)


def phs_annotate(phs_axs, freq:float, phs:float, xytext:list, color:str=None) -> None:
	if freq > 1e9:
		text = '{}deg\n{:.1f}GHz'.format(round(phs), freq/1e9)
	elif freq > 1e6:
		text = '{}deg\n{:.1f}MHz'.format(round(phs), freq/1e6)
	elif freq > 1e3:
		text = '{}deg\n{:.1f}kHz'.format(round(phs), freq/1e3)
	else:
		text = '{}deg\n{:.1f}Hz'.format(round(phs), freq)
	phs_axs.annotate(text, (freq,phs), xytext=xytext, arrowprops=dict(arrowstyle='->'), color=color)
'''
