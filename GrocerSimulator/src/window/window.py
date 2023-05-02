from tkinter import *
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import Menu
from PIL import ImageTk, Image
from pathlib import Path
from toplevel import *
import sys, os
import webbrowser

CUR_DIR = Path(__file__).parent.absolute()
sys.path.append(os.path.abspath(CUR_DIR / '../../src'))

from utils import *

class Window(Tk):

    Customer = {
        "first_name": "",
        "last_name": "",
        "address1": "",
        "address2": "",
        "city": "",
        "postal_code": "",
        "country": "",
        "payment": {
            "payment_response": None
        }
    }

    def __init__(self, width: int, height: int, type:str, title:str):
        super().__init__()

        self.geometry(str(width) + "x" + str(height) + "+50+50")
        self.title(title)
        self.type = type.upper()
        self.running = False
        self.resizable(False, False)
        # self.iconbitmap('icon.ico')
        self.config(background="grey")
        self.create_menu()
        self.add_welcome_text(width)
        self.add_image()
        self.create_button()
        self.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.update()
        self.update_idletasks()

    def wait_for_close(self):
        self.running = True

        #continuously updates the windows
        while(self.running == True):
            self.redraw()
    
    def create_menu(self):
        #Optional menu
        menubar = Menu(self)
        self.config(menu=menubar)

        featured = Menu(menubar, tearoff=0)
        featured.add_command(label="Customer", command=self.set_customer_details)
        featured.add_command(label="Config", command=self.load_config)
        menubar.add_cascade(label="Featured", menu=featured)

        about = Menu(menubar, tearoff=0)
        about.add_command(label="Github", command=self.open_web)
        menubar.add_cascade(label="About", menu=about, underline=0)

        menubar.add_separator()
        menubar.add_command(
            label='Exit',
            command=self.destroy
        )

    def create_button(self):
        button_start = Button(self, text='Start!', command=self.start_game, activebackground='black', activeforeground='grey', pady=10)
        button_reset = Button(self, text='Reset', command=self.reset_game, activebackground='black', activeforeground='grey', pady=10)
        button_close = Button(self, text='Close', command=self.close, activebackground='black', activeforeground='grey', pady=10)
        button_start.place(x=50, y=75)
        button_reset.place(x=200, y=75)
        button_close.place(x=350, y=75)

    def add_welcome_text(self, width):
        label = Label(self, text = "Welcome to Grocer Simulator :)", padx=10, pady=10, width=width)
        label.grid(column=0, row=0)
        label2 = Label(self, text = "Please visit the About", padx=10, pady=0, fg='red', bg='black', width=width)
        label.grid(column=1, row=1)
        label.config(font=("system-ui", 18))
        label.pack()
        label2.pack()
    
    def add_image(self):
        path = "shs.jpeg"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(master=self, image=img)
        panel.image = img
        panel.pack(side="bottom")

    def load_config(self):
        try:
            if("CONFIG" in TopLevel.WINDOWS):
                TopLevel.WINDOWS.remove("CONFIG")
                window = TopLevel("config")
                window.geometry("300x250")
                window.running = False
                window.resizable = (False, False)
                window.title("View Config Details")
                
                username = Label(window, text="Username:", padx=10, pady=10)
                Username = Label(window, text=Utils.readConfig("username"), padx=10, pady=10, fg="red")
                password = Label(window, text="Password:", padx=10, pady=10)
                Password = Label(window, text=Utils.readConfig("password"), padx=10, pady=10, fg="red")
                host = Label(window, text="Host:", padx=10, pady=10)
                Host = Label(window, text=Utils.readConfig("host"), padx=10, pady=10, fg="red")
                database = Label(window, text="Database:", padx=10, pady=10)
                Database = Label(window, text=Utils.readConfig("database"), padx=10, pady=10,fg="red")
                
                username.place(x=50, y=40)
                Username.place(x=150, y=40)
                password.place(x=50, y=80)
                Password.place(x=150, y=80)
                host.place(x=50, y=120)
                Host.place(x=150, y=120)
                database.place(x=50, y=160)
                Database.place(x=150, y=160)

                window.mainloop()
            else:
                raise Exception("Config window already exists, please close and try again")
        except Exception as error:
            #TODO use logger 'warn' as well
            print(error)
    
    def start_game(self):
        showinfo("Init Game", "Game will load shortly") 

    def reset_game(self):
        showinfo("init Game", "Game will reset shortly")
    
    def set_customer_details(selt):
        try:
            if("CUSTOMER" in TopLevel.WINDOWS):
                TopLevel.WINDOWS.remove("CUSTOMER")
                window_main = TopLevel("customer")
                window_main.geometry("500x500")
                window_main.running = False
                window_main.resizable = (False, False)
                window_main.title("Grocer Simulator | Customer setup")
                
                text = Label(window_main, text="Registration form", width=20, font=("bold", 20))
                text.place(x=80, y=10)

                first_name = Label(window_main, text="First Name", width=20, font=("bold", 10))
                first_name.place(x=70, y=80)

                first_name_field = Entry(window_main)
                first_name_field.place(x=240, y=80)

                last_name = Label(window_main, text="Last Name", width=20, font=("bold", 10))
                last_name.place(x=70, y=120)

                last_name_field = Entry(window_main)
                last_name_field.place(x=240, y=120)

                address1 = Label(window_main, text="Address 1", width=20, font=("bold", 10))
                address1.place(x=70, y=160)

                address1_field = Entry(window_main)
                address1_field.place(x=240, y=160)

                address2 = Label(window_main, text="Address 2", width=20, font=("bold", 10))
                address2.place(x=70, y=200)

                address2_field = Entry(window_main)
                address2_field.place(x=240, y=200)

                city = Label(window_main, text="City", width=20, font=("bold", 10))
                city.place(x=70, y=240)

                city_field = Entry(window_main)
                city_field.place(x=240, y=240)

                postal_code = Label(window_main, text="Postal Code", width=20, font=("bold", 10))
                postal_code.place(x=70, y=280)

                postal_code_field = Entry(window_main)
                postal_code_field.place(x=240, y=280)

                country = Label(window_main, text="Country", width=20, font=("bold", 10))
                country.place(x=70, y=320)

                country_field = Entry(window_main)
                country_field.place(x=240, y=320)

                def get_payment():
                    Window.Customer["payment"]["payment_response"] = int(radio.get())

                #payment
                payment=Label(window_main, text="Payment", width=20,font=('bold',10))
                payment.place(x=70,y=360)
                radio=IntVar()

                Radiobutton(window_main,text="Cash Payment", variable=radio, value=1, command=get_payment).place(x=230,y=360)  
                
                Radiobutton(window_main,text="Bank Payment", variable=radio, value=2, command=get_payment).place(x=290, y=360)

                def get_content():
                    Window.Customer["first_name"] = first_name_field.get()
                    Window.Customer["last_name"] = last_name_field.get()
                    Window.Customer["address1"] = address1_field.get()
                    Window.Customer["address2"] = address2_field.get()
                    Window.Customer["city"] = city_field.get()
                    Window.Customer["postal_code"] = postal_code_field.get()
                    Window.Customer["country"] = country_field.get()

                    try:
                        if(Window.Customer["payment"]["payment_response"] != None 
                        and Window.Customer["payment"]["payment_response"] in [1,2]):
                            if(Window.Customer["payment"]["payment_response"] == 1 and "PAYMENT" in TopLevel.WINDOWS):
                                #cash
                                TopLevel.WINDOWS.remove("PAYMENT")
                                window = TopLevel("payment")
                                window.geometry("500x250")
                                window.running = False
                                window.resizable = (False, False)
                                window.title("Grocer Simulator | Payment Details")

                                text = Label(window, text="Confirm Cash Payment Details", width=25, font=("bold", 15))
                                text.place(x=120, y=10)

                                cash_owner = Label(window, text="Cash Owner", width=20, font=("bold", 10))
                                cash_owner.place(x=70, y=80)

                                cash_owner_field = Entry(window)
                                cash_owner_field.place(x=240, y=80)

                                cash_amount = Label(window, text="Amount (R)", width=20, font=("bold", 10))
                                cash_amount.place(x=70, y=120)

                                cash_amount_field = Entry(window)
                                cash_amount_field.place(x=240, y=120)

                                def get_cash_payment():
                                    Window.Customer["payment"]["cash_owner"] = cash_owner_field.get()
                                    Window.Customer["payment"]["amount"] = cash_amount_field.get()
                                    Utils.export_data(Window.Customer)
                                    window_main.window_close()
                                    window.window_close()
                                    showinfo("Customer Registration Data", "Data has been recorded") 

                                btn = Button(window, text='Submit',width=20,bg='brown',fg='black', command=get_cash_payment)
                                btn.place(x=140,y=160)
                                window.wait_for_close()

                            elif(Window.Customer["payment"]["payment_response"] == 2 and "PAYMENT" in TopLevel.WINDOWS):
                                TopLevel.WINDOWS.remove("PAYMENT")
                                window = TopLevel("payment")
                                window.geometry("500x350")
                                window.running = False
                                window.resizable = (False, False)
                                window.title("Grocer Simulator | Payment Details")

                                text = Label(window, text="Confirm Bank Payment Details", width=25, font=("bold", 15))
                                text.place(x=120, y=10)

                                bank_name = Label(window, text="Bank Name", width=20, font=("bold", 10))
                                bank_name.place(x=70, y=80)

                                bank_name_field = Entry(window)
                                bank_name_field.place(x=240, y=80)

                                branch_id = Label(window, text="Branch ID", width=20, font=("bold", 10))
                                branch_id.place(x=70, y=120)

                                branch_id_field = Entry(window)
                                branch_id_field.place(x=240, y=120)

                                telephone_number = Label(window, text="Telephone Number", width=20, font=("bold", 10))
                                telephone_number.place(x=70, y=160)

                                telephone_number_field = Entry(window)
                                telephone_number_field.place(x=240, y=160)

                                amount = Label(window, text="Amount (R)", width=20, font=("bold", 10))
                                amount.place(x=70, y=200)

                                amount_field = Entry(window)
                                amount_field.place(x=240, y=200)

                                def get_bank_payment():
                                    Window.Customer["payment"]["bank_name"] = bank_name_field.get()
                                    Window.Customer["payment"]["branch_id"] = branch_id_field.get()
                                    Window.Customer["payment"]["telephone_number"] = telephone_number_field.get()
                                    Window.Customer["payment"]["amount"] = amount_field.get()
                                    Utils.export_data(Window.Customer)
                                    window.window_close()
                                    window_main.window_close()
                                    showinfo("Customer Registration Data", "Data has been recorded")

                                btn = Button(window, text='Submit',width=20,bg='brown',fg='black', command=get_bank_payment)
                                btn.place(x=140,y=240)
                                window.wait_for_close()

                    except Exception as error:
                        #TODO logger instead
                        print(error)

                btn = Button(window_main, text='Submit',width=20,bg='brown',fg='black', command=get_content)
                btn.place(x=140,y=400)
                window_main.wait_for_close()

            else:
                raise Exception("Customer window already exists, please close and try again")
            
        except Exception as error:
            #TODO use logger 'warn' as well
            print(error)

    def close(self):
        answer = askokcancel(
            title='Confirmation',
            message='Close Grocer Simulator?',
            icon=WARNING
        )

        #closes the application if 'Yes'
        if(answer):
            self.running = False
    def open_web(self):
        webbrowser.open('https://github.com/Keenan-Faure/Boot-Dev', new=0)  

#Main function
def main():
    win = Window(460, 515, "main", "Grocer Simulator")
    win.wait_for_close()
    print(Utils.import_data())

main()