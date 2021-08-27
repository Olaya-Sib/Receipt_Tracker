from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
from Search_Tab import UpdatingEntryBox
from Database_Functions import get_vendors, search_vendors, search_vendors_by_tax, insert_entry, Vendor, delete_entry
from tkinter import messagebox
import math

root = Tk()
root.title("Supplier Date-Format Database")
root.iconphoto(True, PhotoImage(file="./images/icon/receipt.png"))

notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)

menu = Frame(notebook, width=400, height=500)
search = Frame(notebook, width=400, height=500)
result = Frame(notebook, width=400, height=500)
update = Frame(notebook, width=400, height=500)

notebook.add(menu, text="Main Menu")
notebook.add(search, text="Search")
notebook.add(result, text="Results")
notebook.add(update, text='Update')

######################
## SEARCH FUNCTIONS ##
######################
searched_vendors = []


def SelectedSearch(Entry_Box):
    global searched_vendors
    print("You've selected: {}".format(Entry_Box.get()))
    searched_vendors = search_vendors(Entry_Box.get())
    handler.instantiate_entry()


def SelectedQuery(List_Box):
    global searched_vendors
    print("You've selected: {}".format(List_Box.get(ANCHOR)))
    searched_vendors = search_vendors(List_Box.get(ANCHOR))
    handler.instantiate_entry()


##############
## CHECKOUT ##
##############
def select_menu():
    notebook.select(0)


def select_search():
    notebook.select(1)


def select_result():
    notebook.select(2)


def select_update():
    notebook.select(3)


###############
## MAIN MENU ##
###############

Header = Label(menu, text="Supplier Date-Format Database", font='Helvetica 15', foreground="midnight blue")
Header.grid(row=1, column=0, columnspan=2)

Main_Menu = Label(menu, text="Main Menu", font="Helvetica 15", foreground="gray56")
Main_Menu.grid(row=2, column=0, columnspan=2, pady=5)

Search_Photo = PhotoImage(file="./images/main_menu/search.png")
Search_Button = Button(menu, text='Search', underline=1, command=select_search)
Search_Button.grid(row=3, column=0, columnspan=2, pady=10)
Search_Button.configure(width=20)

Update_Photo = PhotoImage(file="./images/main_menu/Update.png")
Update_Button = Button(menu, text="Update", underline=0, command=select_update)
Update_Button.grid(row=4, column=0, columnspan=2)

############
## SEARCH ##
############

Listbox_SubFrame = Frame(search)
Listbox_Scrollbar = Scrollbar(Listbox_SubFrame, orient=VERTICAL)

listbox = Listbox(Listbox_SubFrame, yscrollcommand=Listbox_Scrollbar)
listbox.grid(row=0, column=0, columnspan=1, ipadx=40, sticky=W)
listbox.configure(height=10)

Listbox_Scrollbar.config(command=listbox.yview)
Listbox_Scrollbar.grid(sticky=E, row=0, column=1)

Listbox_SubFrame.grid(row=1, column=1)

Search_Label = Label(search, text="Search Vendor", font='Helvetica 12 bold')
Search_Label.grid(row=0, column=0, padx=10)

Close_Matches = Label(search, text="Close Queries", font='Helvetica 12')
Close_Matches.grid(row=1, column=0, sticky=N)

Entry_Box = UpdatingEntryBox(search)
Entry_Box.set_completion_list(vendors_list=sorted(list(set(get_vendors()))), my_listbox=listbox)
Entry_Box.grid(row=0, column=1, sticky=W)
Entry_Box.configure(width=20)
Entry_Box.focus_set()

Search_Button = Button(search, text="Search", underline=0, command=lambda: SelectedSearch(Entry_Box=Entry_Box))
Search_Button.grid(row=0, column=1, padx=10, sticky=E)

Select_Button = Button(search, text="Select", underline=0, command=lambda: SelectedQuery(List_Box=listbox))
Select_Button.grid(row=2, column=1)

#############
## RESULTS ##
#############

identifier_frame = Frame(result)
identifier_frame.grid(row=0, column=0)
identifier_frame.config(width=500, height=100)

receipt_frame = Frame(result)
receipt_frame.grid(row=1, column=0)
receipt_frame.config(width=500, height=195)

invoice_frame = Frame(result)
invoice_frame.grid(row=2, column=0)
invoice_frame.config(width=500, height=195)

gap_frame = Frame(result)
gap_frame.grid(row=3, column=0)
gap_frame.config(width=500, height=10)

"""
IDENTIFIER FRAME
"""
vendor_label = Label(identifier_frame, text="Vendor: ", font='Helvetica 12 bold')
vendor_label.grid(row=0, column=0, sticky=W, pady=5, padx=10)

tax_num = Label(identifier_frame, text="GST/HST Num: ", font='Helvetica 12')
tax_num.grid(row=1, column=0, sticky=W, columnspan=2, pady=5, padx=10)

vendor_box = Entry(identifier_frame, state=DISABLED)
vendor_box.grid(row=0, column=2, sticky=W)
vendor_box.configure(width=20)

tax_num_box = Entry(identifier_frame, state=DISABLED)
tax_num_box.grid(row=1, column=2, sticky=W)
tax_num_box.configure(width=20)

entry = Label(identifier_frame, text='Entry:', font='Helvetica 11 bold')
entry.grid(row=0, column=3, sticky=E, padx=10)

entry_numerator = Entry(identifier_frame, state=DISABLED)
entry_numerator.grid(row=0, column=4, padx=5)
entry_numerator.configure(width=2)

slash = Label(identifier_frame, text='/', font='Helvetica 11 bold')
slash.grid(row=0, column=5, sticky=W)

entry_denominator = Entry(identifier_frame, state=DISABLED)
entry_denominator.grid(row=0, column=6, padx=5)
entry_denominator.configure(width=2)

prev_button = Button(identifier_frame, text="Pre.", underline=0, state=DISABLED)
prev_button.grid(row=1, column=3)
prev_button.config(width=4)

next_button = Button(identifier_frame, text="Next", underline=0, state=DISABLED)
next_button.grid(row=1, column=4, columnspan=3)
next_button.config(width=4)

"""
RECEIPT FRAME
"""
receipts = Label(receipt_frame, text="Receipts", font="Helvetica 15 bold")
receipts.grid(row=0, column=0, columnspan=2)

primary_receipt = Label(receipt_frame, text="Primary Receipt:", font="Helvetica 12")
primary_receipt.grid(row=1, column=0, sticky=W, pady=2, padx=5)

primary_receipt_box = Entry(receipt_frame, state=DISABLED)
primary_receipt_box.grid(row=1, column=1)
primary_receipt.configure(width=20)

secondary_receipt = Label(receipt_frame, text="Secondary Receipt:", font="Helvetica 12")
secondary_receipt.grid(row=2, column=0, sticky=W, pady=2, padx=5)

secondary_receipt_box = Entry(receipt_frame, state=DISABLED)
secondary_receipt_box.grid(row=2, column=1)
secondary_receipt.configure(width=20)

tertiary_receipt = Label(receipt_frame, text="Tertiary Receipt:", font="Helvetica 12")
tertiary_receipt.grid(row=3, column=0, sticky=W, pady=2, padx=5)

tertiary_receipt_box = Entry(receipt_frame, state=DISABLED)
tertiary_receipt_box.grid(row=3, column=1)
tertiary_receipt.configure(width=20)

"""
INVOICE FRAME
"""
invoices = Label(invoice_frame, text="Invoices", font="Helvetica 15 bold")
invoices.grid(row=0, column=0, columnspan=2)

primary_invoice = Label(invoice_frame, text="Primary Invoice:", font="Helvetica 12")
primary_invoice.grid(row=1, column=0, sticky=W, pady=2, padx=5)

primary_invoice_box = Entry(invoice_frame, state=DISABLED)
primary_invoice_box.grid(row=1, column=1)
primary_invoice.configure(width=20)

secondary_invoice = Label(invoice_frame, text="Secondary Invoice:", font="Helvetica 12")
secondary_invoice.grid(row=2, column=0, sticky=W, pady=2, padx=5)

secondary_invoice_box = Entry(invoice_frame, state=DISABLED)
secondary_invoice_box.grid(row=2, column=1)
secondary_invoice.configure(width=20)

tertiary_invoice = Label(invoice_frame, text="Tertiary Invoice:", font="Helvetica 12")
tertiary_invoice.grid(row=3, column=0, sticky=W, pady=2, padx=5)

tertiary_invoice_box = Entry(invoice_frame, state=DISABLED)
tertiary_invoice_box.grid(row=3, column=1)
tertiary_invoice.configure(width=20)


##############
## HANDLERS ##
##############

class RHandler(object):
    def __init__(self):
        self.index = 0

        self.tax_num_box = tax_num_box
        self.vendor_box = vendor_box

        self.numerator = entry_numerator
        self.denominator = entry_denominator

        self.primary_receipt_box = primary_receipt_box
        self.secondary_receipt_box = secondary_receipt_box
        self.tertiary_receipt_box = tertiary_receipt_box

        self.primary_invoice_box = primary_invoice_box
        self.secondary_invoice_box = secondary_invoice_box
        self.tertiary_invoice_box = tertiary_invoice_box

        self.prev = prev_button
        self.next = next_button

    def instantiate_entry(self):
        if searched_vendors:
            select_result()

            self.vendor_box.config(state=NORMAL)
            self.vendor_box.delete(0, END)
            self.vendor_box.insert(END, searched_vendors[0][1])
            self.vendor_box.config(state=DISABLED)

            self.numerator.config(state=NORMAL)
            self.numerator.delete(0, END)
            self.numerator.insert(END, '1')
            self.numerator.config(state=DISABLED)

            self.denominator.config(state=NORMAL)
            self.denominator.delete(0, END)
            self.denominator.insert(END, len(searched_vendors))
            self.denominator.config(state=DISABLED)

            self.update_receipt()
            self.update_numerator()
            self.update_invoice()
            self.update_tax()

            if len(searched_vendors) > 1:
                self.prev.config(state=NORMAL, command=self.decrease_index)
                self.next.config(state=NORMAL, command=self.increase_index)

        else:
            print("This does not match an entry.")

    def update_receipt(self):
        self.primary_receipt_box.config(state=NORMAL)
        self.primary_receipt_box.delete(0, END)
        self.primary_receipt_box.insert(END, str(searched_vendors[self.index][2]))
        self.primary_receipt_box.config(state=DISABLED)

        self.secondary_receipt_box.config(state=NORMAL)
        self.secondary_receipt_box.delete(0, END)
        self.secondary_receipt_box.insert(END, str(searched_vendors[self.index][3]))
        self.secondary_receipt_box.config(state=DISABLED)

        self.tertiary_receipt_box.config(state=NORMAL)
        self.tertiary_receipt_box.delete(0, END)
        self.tertiary_receipt_box.insert(END, str(searched_vendors[self.index][4]))
        self.tertiary_receipt_box.config(state=DISABLED)

    def update_invoice(self):
        self.primary_invoice_box.config(state=NORMAL)
        self.primary_invoice_box.delete(0, END)
        self.primary_invoice_box.insert(END, str(searched_vendors[self.index][5]))
        self.primary_invoice_box.config(state=DISABLED)

        self.secondary_invoice_box.config(state=NORMAL)
        self.secondary_invoice_box.delete(0, END)
        self.secondary_invoice_box.insert(END, str(searched_vendors[self.index][6]))
        self.secondary_invoice_box.config(state=DISABLED)

        self.secondary_invoice_box.config(state=NORMAL)
        self.secondary_invoice_box.delete(0, END)
        self.secondary_invoice_box.insert(END, str(searched_vendors[self.index][7]))
        self.secondary_invoice_box.config(state=DISABLED)

    def update_tax(self):
        self.tax_num_box.config(state=NORMAL)
        self.tax_num_box.delete(0, END)
        self.tax_num_box.insert(END, searched_vendors[self.index][0])
        self.tax_num_box.config(state=DISABLED)

    def update_numerator(self):
        self.numerator.config(state=NORMAL)
        self.numerator.delete(0, END)
        self.numerator.insert(END, self.index + 1)
        self.numerator.config(state=DISABLED)

    def increase_index(self):
        if int(self.denominator.get()) > self.index + 1:
            self.index += 1

            self.update_receipt()
            self.update_numerator()
            self.update_invoice()
            self.update_tax()

    def decrease_index(self):
        if self.index > 0:
            self.index -= 1

            self.update_receipt()
            self.update_numerator()
            self.update_invoice()
            self.update_tax()


############
## UPDATE ##
############

############
## FRAMES ##
############

Company_Screen = Frame(update)
Company_Screen.grid(row=0, column=0)

Formats_Screen = Frame(update)
Formats_Screen.grid(row=1, column=0)

Receipts_Screen = Frame(Formats_Screen)
Receipts_Screen.grid(row=0, column=0)

Invoices_Screen = Frame(Formats_Screen)
Invoices_Screen.grid(row=0, column=2)

ttk.Separator(Formats_Screen, orient=VERTICAL).grid(row=0, column=1, sticky='ns')

#################
## UPDATE VARs ##
#################

Company = StringVar()
TaxNum = IntVar()

RPrimary = StringVar()
RSecondary = StringVar()
RTertiary = StringVar()

IPrimary = StringVar()
ISecondary = StringVar()
ITertiary = StringVar()

result_set = []

##############################
## Invoice & Receipt Labels ##
##############################

Label(Receipts_Screen, text="Receipts", font='verdana 14 bold').grid(row=0, column=0, padx=60)
Label(Invoices_Screen, text="Invoices", font='verdana 14 bold').grid(row=0, column=0, padx=60)


def primary_receipt_features():
    RPrimary_Frame = LabelFrame(Receipts_Screen, text='Primary Format', relief=GROOVE)
    RPrimary_Frame.grid(row=1, column=0, padx=20)

    RPrimary_Button1 = Radiobutton(RPrimary_Frame, text='Month/Day/Year', variable=RPrimary, value='Month / Day / Year')
    RPrimary_Button1.grid(row=0, column=0)

    RPrimary_Button2 = Radiobutton(RPrimary_Frame, text='Day/Month/Year', variable=RPrimary, value='Day / Month / Year')
    RPrimary_Button2.grid(row=1, column=0)

    RPrimary_Button3 = Radiobutton(RPrimary_Frame, text='Year/Month/Day', variable=RPrimary, value='Year / Month / Day')
    RPrimary_Button3.grid(row=2, column=0)

    def clear_1():
        RPrimary.set('')

    RPrimary_Clear = Button(RPrimary_Frame, text="Clear", underline=0, command=clear_1)
    RPrimary_Clear.grid(row=3, column=0)

    globals().update(locals())


primary_receipt_features()


def secondary_receipt_features():
    RSecondary_Frame = LabelFrame(Receipts_Screen, text='Secondary Format', relief=GROOVE)
    RSecondary_Frame.grid(row=2, column=0, padx=20)

    RSecondary_Button1 = Radiobutton(RSecondary_Frame, text='Month/Day/Year', variable=RSecondary,
                                     value='Month / Day / Year')
    RSecondary_Button1.grid(row=0, column=0)

    RSecondary_Button2 = Radiobutton(RSecondary_Frame, text='Day/Month/Year', variable=RSecondary,
                                     value='Day / Month / Year')
    RSecondary_Button2.grid(row=1, column=0)

    RSecondary_Button3 = Radiobutton(RSecondary_Frame, text='Year/Month/Day', variable=RSecondary,
                                     value='Year / Month / Day')
    RSecondary_Button3.grid(row=2, column=0)

    def clear_2():
        RSecondary.set('')

    RSecondary_Clear = Button(RSecondary_Frame, text="Clear", underline=0, command=clear_2)
    RSecondary_Clear.grid(row=3, column=0)

    globals().update(locals())


secondary_receipt_features()


def tertiary_receipt_features():
    RTertiary_Frame = LabelFrame(Receipts_Screen, text='Tertiary Format', relief=GROOVE)
    RTertiary_Frame.grid(row=3, column=0, padx=20)

    RTertiary_Button1 = Radiobutton(RTertiary_Frame, text='Month/Day/Year', variable=RTertiary,
                                    value='Month / Day / Year')
    RTertiary_Button1.grid(row=0, column=0)

    RTertiary_Button2 = Radiobutton(RTertiary_Frame, text='Day/Month/Year', variable=RTertiary,
                                    value='Day / Month / Year')
    RTertiary_Button2.grid(row=1, column=0)

    RTertiary_Button3 = Radiobutton(RTertiary_Frame, text='Year/Month/Day', variable=RTertiary,
                                    value='Year / Month / Day')
    RTertiary_Button3.grid(row=2, column=0)

    def clear_3():
        RTertiary.set('')

    RTertiary_Clear = Button(RTertiary_Frame, text="Clear", underline=0, command=clear_3)
    RTertiary_Clear.grid(row=3, column=0)

    globals().update(locals())


tertiary_receipt_features()


def primary_invoice_features():
    IPrimary_Frame = LabelFrame(Invoices_Screen, text='Primary Format', relief=GROOVE)
    IPrimary_Frame.grid(row=1, column=0, padx=20)

    IPrimary_Button1 = Radiobutton(IPrimary_Frame, text='Month/Day/Year', variable=IPrimary, value='Month / Day / Year')
    IPrimary_Button1.grid(row=0, column=0)

    IPrimary_Button2 = Radiobutton(IPrimary_Frame, text='Day/Month/Year', variable=IPrimary, value='Day / Month / Year')
    IPrimary_Button2.grid(row=1, column=0)

    IPrimary_Button3 = Radiobutton(IPrimary_Frame, text='Year/Month/Day', variable=IPrimary, value='Year / Month / Day')
    IPrimary_Button3.grid(row=2, column=0)

    def clear_4():
        IPrimary.set('')

    IPrimary_Clear = Button(IPrimary_Frame, text="Clear", underline=0, command=clear_4)
    IPrimary_Clear.grid(row=3, column=0)

    globals().update(locals())


primary_invoice_features()


def secondary_invoice_features():
    ISecondary_Frame = LabelFrame(Invoices_Screen, text='Secondary Format', relief=GROOVE)
    ISecondary_Frame.grid(row=2, column=0, padx=20)

    ISecondary_Button1 = Radiobutton(ISecondary_Frame, text='Month/Day/Year', variable=ISecondary,
                                     value='Month / Day / Year')
    ISecondary_Button1.grid(row=0, column=0)

    ISecondary_Button2 = Radiobutton(ISecondary_Frame, text='Day/Month/Year', variable=ISecondary,
                                     value='Day / Month / Year')
    ISecondary_Button2.grid(row=1, column=0)

    ISecondary_Button3 = Radiobutton(ISecondary_Frame, text='Year/Month/Day', variable=ISecondary,
                                     value='Year / Month / Day')
    ISecondary_Button3.grid(row=2, column=0)

    def clear_5():
        ISecondary.set('')

    ISecondary_Clear = Button(ISecondary_Frame, text="Clear", underline=0, command=clear_5)
    ISecondary_Clear.grid(row=3, column=0)

    globals().update(locals())


secondary_invoice_features()


def tertiary_invoice_features():
    ITertiary_Frame = LabelFrame(Invoices_Screen, text='Tertiary Format', relief=GROOVE)
    ITertiary_Frame.grid(row=3, column=0, padx=20)

    ITertiary_Button1 = Radiobutton(ITertiary_Frame, text='Month/Day/Year', variable=ITertiary,
                                    value='Month / Day / Year')
    ITertiary_Button1.grid(row=0, column=0)

    ITertiary_Button2 = Radiobutton(ITertiary_Frame, text='Day/Month/Year', variable=ITertiary,
                                    value='Day / Month / Year')
    ITertiary_Button2.grid(row=1, column=0)

    ITertiary_Button3 = Radiobutton(ITertiary_Frame, text='Year/Month/Day', variable=ITertiary,
                                    value='Year / Month / Day')
    ITertiary_Button3.grid(row=2, column=0)

    def clear_6():
        ITertiary.set('')

    ITertiary_Clear = Button(ITertiary_Frame, text="Clear", underline=0, command=clear_6)
    ITertiary_Clear.grid(row=3, column=0)

    globals().update(locals())


tertiary_invoice_features()


def create_buttons_list():
    radiobuttons = [RPrimary_Button1, RPrimary_Button2, RPrimary_Button3, RSecondary_Button1, RSecondary_Button2,
                    RSecondary_Button3, RTertiary_Button1, RTertiary_Button2, RTertiary_Button3, IPrimary_Button1,
                    IPrimary_Button2, IPrimary_Button3, ISecondary_Button1, ISecondary_Button2, ISecondary_Button3,
                    ITertiary_Button1, ITertiary_Button2, ITertiary_Button3]
    radiovariables = [RPrimary, RSecondary, RTertiary, IPrimary, ISecondary, ITertiary]
    clearbuttons = [RPrimary_Clear, RSecondary_Clear, RTertiary_Clear, IPrimary_Clear, ISecondary_Clear,
                    ITertiary_Clear]

    globals().update(locals())


create_buttons_list()


def create_vendor_and_tax_entries():
    Company_Name = Label(Company_Screen, text='Company: ', font='verdana 12')
    Company_Name.grid(row=0, column=0)

    Tax_Num = Label(Company_Screen, text='Tax Num: ', font='verdana 12')
    Tax_Num.grid(row=1, column=0)

    Company_Entry = Entry(Company_Screen)
    Company_Entry.grid(row=0, column=1)

    Tax_Entry = Entry(Company_Screen)
    Tax_Entry.grid(row=1, column=1)

    globals().update(locals())


create_vendor_and_tax_entries()


def create_QButton():
    def provide_information():
        message = messagebox.showinfo('Federal Business Number [Tax Num]',
                                      'A Federal Business Number (BN) is a 9-digit '
                                      'number which Revenue Canada Agency assigns to '
                                      'a business such as a corporation, '
                                      'a sole proprietorship or a partnership in '
                                      'Canada.  Each corporation is assigned only '
                                      'one Business Number but multiple accounts can '
                                      'be opened up under this number.')

    QImage = PhotoImage(file='images/misc/question1.png')
    QButton = tk.Button(Company_Screen, image=QImage, bd=0)
    QButton.grid(row=1, column=2)
    QButton.configure(command=provide_information)

    globals().update(locals())


create_QButton()


def refresh():
    global result_set

    if result_set:
        for i, variable in enumerate(radiovariables, 2):
            variable.set(result_set[0][i])
    else:
        for variable in radiovariables:
            variable.set('')


def create_RButton():
    RImage = PhotoImage(file='images/misc/refresh.png')
    RButton = tk.Button(Company_Screen, image=RImage, command=refresh, bd=0)
    RButton.grid(row=0, column=2)

    globals().update(locals())


create_RButton()


def delete():
    global result_set
    proceed = messagebox.askyesno("Warning", "Information for account: {} "
                                             "will be permanently deleted. "
                                             "Are you sure you want to delete?".format(Tax_Entry.get()))

    if proceed:
        delete_entry(vendor_tax=Tax_Entry.get())
        result_set = []
        initiate()


def create_DButton():
    DImage = PhotoImage(file='images/misc/delete.png')
    DButton = tk.Button(Company_Screen, image=DImage, command=delete, bd=0)
    DButton.grid(row=0, column=3)

    globals().update(locals())


create_DButton()


def update():
    global result_set

    if Company_Entry.get().lower() == 'new company name':
        messagebox.showerror('Error', "Enter a company name in the entry box.")

    else:
        proceed = messagebox.askyesno("Warning", "Information may override existing "
                                                 "data. Are you sure you want to update?")

        new_vendor = Vendor(GST_HST_Number=Tax_Entry.get(),
                            Vendor_Name=Company_Entry.get().lower(),
                            Receipt_Format_1=RPrimary.get(),
                            Receipt_Format_2=RSecondary.get(),
                            Receipt_Format_3=RTertiary.get(),
                            Invoice_Format_1=IPrimary.get(),
                            Invoice_Format_2=ISecondary.get(),
                            Invoice_Format_3=ITertiary.get())

        if proceed:
            if not result_set:
                insert_entry(new_vendor=new_vendor)
                initiate()

            if result_set:
                delete_entry(vendor_tax=Tax_Entry.get())
                insert_entry(new_vendor)
                result_set = []
                initiate()


def create_Update_Button():
    Update_Button = Button(Company_Screen, text='Update', underline=0, command=update)
    Update_Button.grid(row=0, column=4)
    Update_Button.configure(width=8)

    globals().update(locals())


create_Update_Button()


def fill_in(num):
    global result_set
    try:
        int(num)
    except ValueError:
        messagebox.showerror(title='Error',
                             message='The tax number should be 9 digits long. Non-numerical values are not allowed.')
    if len(num) != 9:
        messagebox.showerror(title='Error',
                             message='The tax number should be 9 digits long. Non-numerical values are not allowed.')
    else:
        result_set = search_vendors_by_tax(num)

        # turning on buttons
        Tax_Entry.configure(state=DISABLED)
        Company_Entry.configure(state=NORMAL)
        Search_Button.configure(state=DISABLED)
        Update_Button.configure(state=NORMAL)
        RButton.configure(state=NORMAL)

        for button in radiobuttons:
            button.configure(state=NORMAL)
        for button in clearbuttons:
            button.configure(state=NORMAL)

        if not result_set:
            # for non-existent tax num, enter new company name in entry field
            Company_Entry.insert(0, 'new company name')
        else:
            DButton.configure(state=NORMAL)

            # set company name in entry
            Company_Entry.insert(0, str(result_set[0][1]))
            # setting radiovariables and turning on correct radio buttons
            for i, variable in enumerate(radiovariables, 2):
                variable.set(result_set[0][i])




def create_Search_Button():
    Search_Button = Button(Company_Screen, text='Search', underline=0, command=lambda: fill_in(num=Tax_Entry.get()))
    Search_Button.grid(row=1, column=4)
    Search_Button.configure(width=8)

    globals().update(locals())


create_Search_Button()


def initiate():
    refresh()

    Tax_Entry.configure(state=NORMAL)
    Tax_Entry.delete(0, END)

    Search_Button.configure(state=NORMAL)
    QButton.configure(state=NORMAL)
    Update_Button.configure(state=DISABLED)

    Company_Entry.delete(0, END)
    Company_Entry.configure(state=DISABLED)
    DButton.configure(state=DISABLED)

    for button in radiobuttons:
        button.configure(state=DISABLED)
    for button in clearbuttons:
        button.configure(state=DISABLED)
    for variable in radiovariables:
        variable.set('')


def create_cancel_button():
    CButton = Button(Company_Screen, text='Cancel', underline=0, command=initiate)
    CButton.grid(row=2, column=4)
    CButton.configure(width=8)


create_cancel_button()

initiate()

handler = RHandler()

mainloop()
