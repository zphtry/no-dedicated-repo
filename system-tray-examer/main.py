from exam import *
from systray import *
import threading
from playsound import playsound

update_interval = 1

def f(oldTray, oldPoint):
	newTray = SysTray()

	if oldPoint != getPoint(): playsound('alert2.mp3')

	oldPoint = getPoint()

	newTray.setTrayNumber(getPoint())

	oldTray.icon.visible = False

	newTray.icon.visible = True

	threading.Timer(update_interval, f, [newTray, oldPoint]).start()

f(SysTray(), getPoint())