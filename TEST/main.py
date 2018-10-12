import win32gui

########################################################################################################################
#                                                    VALEURS                                                           #
########################################################################################################################

listWindows = []
mainChar = ''
mainWindow = []

########################################################################################################################
#                                                    FONCTIONS                                                         #
########################################################################################################################

#Recuperation des fenetres de personnages de Dofus
def getDofusWindows(hwnd, top_windows):
    if win32gui.IsWindowVisible(hwnd) and '- Dofus' in win32gui.GetWindowText(hwnd):
        top_windows.extend((hwnd, win32gui.GetWindowText(hwnd)))

#Recuperation de la fenetre du personnage maitre
def getMainWindow(hwnd, top_windows):
    if win32gui.IsWindowVisible(hwnd) and mainChar in win32gui.GetWindowText(hwnd) \
            and '- Dofus' in win32gui.GetWindowText(hwnd):
        top_windows.extend((hwnd, win32gui.GetWindowText(hwnd)))

########################################################################################################################
#                                                     PROGRAMME                                                        #
########################################################################################################################

mainChar = raw_input ("Entrer le nom du personnage de la fenetre principale:")

win32gui.EnumWindows(getDofusWindows, listWindows)
print listWindows

win32gui.EnumWindows(getMainWindow, mainWindow)
print mainWindow

win32gui.ShowWindow(mainWindow[0],5)
win32gui.SetForegroundWindow(mainWindow[0])