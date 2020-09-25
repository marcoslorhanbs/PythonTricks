import tkinter as tk
jan = tk.Tk()
jan.title('New Window')
jan.geometry('500x500')

def GetWinSize():
     WindowSize = jan.geometry()
     WindowSize = WindowSize.split('x')
     width = WindowSize[0]
     height = str(WindowSize[1])
     height = height.split('+')
     height = height[0]
     print(width)
     print(height)
GetWinSize()
#Recommended use a tk.button to call.


jan.mainloop()