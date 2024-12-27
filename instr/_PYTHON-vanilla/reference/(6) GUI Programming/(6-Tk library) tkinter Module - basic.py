## tkinter Module
import tkinter              # load the tkinter (tk interface) module into memory
import tkinter.messagebox   # load the tkinter.messagebox module into memory (contains showinfo Function)


## Widgets (objects)
class MyGuI:
    def __init__(self):
        ## Tk Class (Main Window)
        self.tk_object = tkinter.Tk()
            # create a Tk object for main window 


        ## Frame Class (Containers)
        self.frame_object_1 = tkinter.Frame(self.tk_object)
        self.frame_object_2 = tkinter.Frame(self.tk_object)
        self.frame_object_3 = tkinter.Frame(self.tk_object)
        self.frame_object_4 = tkinter.Frame(self.tk_object)
        self.frame_object_5 = tkinter.Frame(self.tk_object)
        self.frame_object_6 = tkinter.Frame(self.tk_object)
        self.frame_object_7 = tkinter.Frame(self.tk_object)
            # create a Frame object for the root widget (object)


        ## Widgets (Contents)
        self.label_1 = tkinter.Label(self.frame_object_1, text='1st frame') # 1st frame
        self.label_object_1 = tkinter.Label(self.frame_object_1, text='1st text')
        self.label_object_2 = tkinter.Label(self.frame_object_1, text='2nd text')
        self.label_object_3 = tkinter.Label(self.frame_object_1, text='Try to click the following buttons!')

        self.label_2 = tkinter.Label(self.frame_object_2, text='2nd frame') # 2nd frame
        self.label_object_4 = tkinter.Label(self.frame_object_2, text='Buttons: ')
        self.button_object_1 = tkinter.Button(self.frame_object_2, text='Click', command=self.callback_function_1)
        self.button_object_2 = tkinter.Button(self.frame_object_2, text='Quit', command=self.tk_object.destroy)

        self.label_3 = tkinter.Label(self.frame_object_3, text='3rd frame') # 3rd frame
        self.label_object_5 = tkinter.Label(self.frame_object_3, text='Enter a number to double:')
        self.entry_object_1 = tkinter.Entry(self.frame_object_3, width=10)

        self.label_4 = tkinter.Label(self.frame_object_4, text='4th frame') # 4th frame
        self.stringVar_object_1 = tkinter.StringVar()
        self.label_object_6 = tkinter.Label(self.frame_object_4, text='The doubled value:')
        self.label_object_7 = tkinter.Label(self.frame_object_4, textvariable=self.stringVar_object_1)

        self.label_5 = tkinter.Label(self.frame_object_5, text='5th frame') # 5th frame
        self.button_object_3 = tkinter.Button(self.frame_object_5, text='Calculate', command=self.callback_function_2)

        self.label_6 = tkinter.Label(self.frame_object_6, text='6th frame') # 6th frame
        self.intVar_object_1 = tkinter.IntVar()
        self.radiobutton_object_1 = tkinter.Radiobutton(self.frame_object_6, text='Option 1', variable=self.intVar_object_1, value=1)
        self.radiobutton_object_2 = tkinter.Radiobutton(self.frame_object_6, text='Option 2', variable=self.intVar_object_1, value=2)
        self.radiobutton_object_3 = tkinter.Radiobutton(self.frame_object_6, text='Option 3', variable=self.intVar_object_1, value=3)

        self.label_7 = tkinter.Label(self.frame_object_7, text='7th frame') # 7th frame
        self.button_object_4 = tkinter.Button(self.frame_object_7, text='Ok', command=self.callback_function_3)


        ## pack Method
        self.label_1.pack() # 1st frame
        self.label_object_1.pack() 
        self.label_object_2.pack()
        self.label_object_3.pack()

        self.label_2.pack() # 2nd frame
        self.label_object_4.pack(side='left') 
        self.button_object_1.pack(side='left')
        self.button_object_2.pack(side='left')

        self.label_3.pack() # 3rd frame
        self.label_object_5.pack(side='left')
        self.entry_object_1.pack(side='left')

        self.label_4.pack() # 4th frame
        self.label_object_6.pack(side='left')
        self.label_object_7.pack(side='left')

        self.label_5.pack() # 5th frame
        self.button_object_3.pack()

        self.label_6.pack() # 6th frame
        self.radiobutton_object_1.pack()
        self.radiobutton_object_2.pack()
        self.radiobutton_object_3.pack()

        self.label_7.pack() # 7th frame
        self.button_object_4.pack()
        
        self.frame_object_1.pack()
        self.frame_object_2.pack()
        self.frame_object_3.pack()
        self.frame_object_4.pack()
        self.frame_object_5.pack()
        self.frame_object_6.pack()
        self.frame_object_7.pack()
            # side kyword argument determines where a widget should be positioned
            # pack method makes the widget visible
            # Valid Arguments: side='left', side='right', side='bottom', side='top' (default)


        ## mainloop Function
        tkinter.mainloop()
            # displays every main Tk objects like an infinite loop


    ## Event Handler (Callback Function)
    def callback_function_1(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.') # showinfo Function makes dialog box

    def callback_function_2(self):
        x = float(self.entry_object_1.get()) * 2    # get method returns a string
        self.stringVar_object_1.set(str(x))         # set method sets the value of an object of StringVar Class
        tkinter.messagebox.showinfo('Response', 'The doubled value is ' + self.stringVar_object_1.get())

    def callback_function_3(self):
        tkinter.messagebox.showinfo('Selection', 'You have selected option ' + str(self.intVar_object_1.get()))

def main():
    my_gui = MyGuI()

main()
