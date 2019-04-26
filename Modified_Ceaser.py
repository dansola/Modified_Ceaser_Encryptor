import tkinter as tk
from random import randint


class MainApplication(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.parent = master

        # Format Background
        self.canvas = tk.Canvas(self.master, height=HEIGHT, width=WIDTH)
        self.canvas.pack()

        self.background_label = tk.Label(self.master, image=background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Encryption Pane
        self.label_title = tk.Label(self.master, text="Hide Your Password!", font=('Courier', 30), bg='#000000',
                                    fg='#2ad900', relief='ridge', bd=8)
        self.label_title.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.1, anchor='n')

        self.frame = tk.Frame(self.master, bg='#2ad900', bd=8, relief='ridge')
        self.frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')

        self.entry = tk.Entry(self.frame, font=('Courier', 25))
        self.entry.place(relwidth=0.65, relheight=1)

        self.button = tk.Button(self.frame, text='Encrypt Password', font=('Fixedsys', 20),
                                command=lambda: Cipher.encrypt(self, self.entry.get()))
        self.button.place(relx=0.67, relheight=1, relwidth=0.33)

        self.lower_frame = tk.Frame(self.master, bg='#2ad900', bd=8, relief='ridge')
        self.lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.2, anchor='n')

        self.label = tk.Label(self.lower_frame, font=('Courier', 30))
        self.label.place(relwidth=1, relheight=1)

        # Decryption Pane

        self.frame2 = tk.Frame(self.master, bg='#2ad900', bd=8, relief='ridge')
        self.frame2.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.1, anchor='n')

        self.entry2 = tk.Entry(self.frame2, font=('Courier', 25))
        self.entry2.place(relwidth=0.65, relheight=1)

        self.button2 = tk.Button(self.frame2, text='Decrypt Password', font=('Fixedsys', 20),
                                 command=lambda: Cipher.decrypt(self, self.entry2.get()))
        self.button2.place(relx=0.67, relheight=1, relwidth=0.33)

        self.lower_frame2 = tk.Frame(self.master, bg='#2ad900', bd=8, relief='ridge')
        self.lower_frame2.place(relx=0.5, rely=0.7, relwidth=0.75, relheight=0.2, anchor='n')

        self.label2 = tk.Label(self.lower_frame2, font=('Courier', 30))
        self.label2.place(relwidth=1, relheight=1)


class Cipher(MainApplication):
    def encrypt(self, plaintext):
        try:
            cipher = ""  # initialize cipher
            for char in plaintext:
                key = randint(0, 9)  # shift by a random amount for each input character
                cipher += yranoitcid[(dictionary[char] + key) % 93]  # add the shifted character to cipher
                cipher += str(key)  # add amount shifted to the cipher
            # send result to GUI
            self.label['text'] = cipher
            self.label['fg'] = '#000000'
        # send red error message if user enters invalid input (ex. spaces)
        except:
            self.label['text'] = 'Invalid Password'
            self.label['fg'] = 'red'

    def decrypt(self, cipher):
        try:
            plaintext2 = ""  # initialize decrypted password
            for i in range(0, len(cipher), 2):  # only even indexed characters relate to cipher
                key = int(cipher[i + 1])  # use odd indexed characters as the amount to shift
                char = cipher[i]
                plaintext2 += yranoitcid[
                    (dictionary[char] - key) % 93]  # add the unshifted character to the decrypted password
            # send result to GUI
            self.label2['text'] = plaintext2
            self.label2['fg'] = '#000000'
        # send red error message if user enters invalid input (ex. spaces or characters not followed by numbers)
        except:
            self.label2['text'] = 'Invalid Cipher'
            self.label2['fg'] = '#f53e3e'


def main():
    root = tk.Tk()

    global HEIGHT
    global WIDTH
    global background_image
    global dictionary
    global yranoitcid

    HEIGHT = 700
    WIDTH = 800
    background_image = tk.PhotoImage(file='./Images/gui_image.png')

    # initialize reference dictionaries as shuffled alphabet, numbers, and characters
    dictionary = dict(
        zip("4[KJ\\owi`#3_TeGgr+L)Z,dpQDVCsB$};{8<'|U?x!lS]^jEb5YHq2&0~7/X*O6MhWF@u:vzcIRtk%(1Pf-.nAaN>9=ym",
            range(93)))
    yranoitcid = dict(
        zip(range(93),
            "4[KJ\\owi`#3_TeGgr+L)Z,dpQDVCsB$};{8<'|U?x!lS]^jEb5YHq2&0~7/X*O6MhWF@u:vzcIRtk%(1Pf-.nAaN>9=ym"))

    MainApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
