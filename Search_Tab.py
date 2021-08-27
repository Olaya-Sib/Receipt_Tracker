import tkinter
import tkinter.ttk as ttk
import sqlite3
from Database_Functions import get_vendors, search_vendors


class UpdatingEntryBox(ttk.Entry):

    def set_completion_list(self, vendors_list, my_listbox):
        self._vendors_list = sorted(vendors_list, key=str.lower)
        self._values = list(set(self._vendors_list))
        if my_listbox:
            self._attached_listbox = my_listbox
        self.bind('<KeyRelease>', self.update_list_box)
        self.bind('<Tab>', self.tab_handler)

    def update_list_box(self, event):
        self.set_completion_list(vendors_list=sorted(list(set(get_vendors()))), my_listbox=0)
        field_string = self.get().lower()
        self._attached_listbox.delete(0, tkinter.END)

        for unique_vendor in self._values:
            if field_string in unique_vendor:
                self._attached_listbox.insert(tkinter.END, str(unique_vendor))

    def tab_handler(self, event):
        if self._attached_listbox.size() == 1:
            self.delete(0, tkinter.END)
            self.insert(0, self._attached_listbox.get(0))


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("400x250")

    Listbox_SubFrame = tkinter.Frame(root)
    Listbox_Scrollbar = tkinter.Scrollbar(Listbox_SubFrame, orient=tkinter.VERTICAL)

    listbox = tkinter.Listbox(Listbox_SubFrame, yscrollcommand=Listbox_Scrollbar)
    listbox.grid(row=0, column=0, columnspan=1, ipadx=40, sticky=tkinter.W)
    listbox.configure(height=10)

    Listbox_Scrollbar.config(command=listbox.yview)
    Listbox_Scrollbar.grid(sticky=tkinter.E, row=0, column=1)

    Listbox_SubFrame.grid(row=1, column=1)

    Search_Label = tkinter.Label(root, text="Search Vendor", font='Helvetica 12 bold')
    Search_Label.grid(row=0, column=0, padx=10)

    Close_Matches = tkinter.Label(root, text="Close Queries", font='Helvetica 12')
    Close_Matches.grid(row=1, column=0, sticky=tkinter.N)

    Entry_Box = UpdatingEntryBox(root)
    Entry_Box.set_completion_list(vendors_list=sorted(list(set(get_vendors()))), my_listbox=listbox)
    Entry_Box.grid(row=0, column=1, sticky=tkinter.W)
    Entry_Box.configure(width=20)
    Entry_Box.focus_set()

    Search_Button = tkinter.Button(root, text="Search", underline=0,
                                   command=lambda: SelectedSearch(Entry_Box=Entry_Box))
    Search_Button.grid(row=0, column=1, padx=10, sticky=tkinter.E)

    Select_Button = tkinter.Button(root, text="Select", underline=0, command=lambda: SelectedQuery(List_Box=listbox))
    Select_Button.grid(row=2, column=1)

    root.mainloop()
