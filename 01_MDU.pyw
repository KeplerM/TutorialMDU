from tkinter import *
raiz=Tk() 
raiz.title("Test window")                   # Create title
raiz.resizable(True,True)                   # Window dimensions (width,heigh)
raiz.iconbitmap("AMADEico.ico")             # Add Icon
raiz.geometry("650x350")                    # Predefined window dimensions (width,heigh)
#raiz.config(bg="blue")                     # Background raiz color
raiz.config(bd=45)                          # Edge raiz size
raiz.config(relief="sunken")                # Edge raiz type: groove, sunken,...
raiz.config(cursor="hand2")                 # Cursor raiz type: hand2, pirate,...
miFrame=Frame()                             # Create frame
miFrame.pack()                              # Pack frame between raiz
#miFrame.pack(side="bottom", anchor="e")                              # Location frame
#miFrame.pack(fill="both", expand="True")                              # Expand size frame
miFrame.config(bg="red")                    # Background frame color
miFrame.config(width="650", height="350")   # Frame dimensions 
miFrame.config(bd=35)                       # Edge frame size
miFrame.config(relief="groove")             # Edge frame type: groove, sunken,...
miFrame.config(cursor="pirate")             # Cursor frame type: hand2, pirate,...
raiz.mainloop()
