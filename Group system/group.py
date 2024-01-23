from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import datetime
import time

class GroupManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("GROUP Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="GROUP MANAGEMENT SYSTEM", bd=15, relief=RIDGE, bg='white', fg="darkgreen", font=("times new roman", 50, "bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)

        img1 = Image.open("images/image1.jpg")
        img1 = img1.resize((120, 120))  # Corrected attribute
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_img = Label(self.root, image=self.photoimg1, borderwidth=0)
        lbl_img.place(x=90, y=10)

        # =============DataFrame=================
        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=120, width=1530, height=450)

        self.DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Group Information", fg="darkgreen", font=("arial", 12, "bold"))
        self.DataFrameLeft.place(x=0, y=5, width=900, height=370)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Group Add Information", fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameRight.place(x=910, y=0, width=540, height=370)

        # ==================buttons Frame======================
        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=520, width=1530, height=65)

        # ===================Main Button ======================
        btnAddDate = Button(ButtonFrame, text="AddData", font=("arial", 12, "bold"), bg="darkgreen", fg="white")
        btnAddDate.grid(row=0, column=0)

        btnUpdateMed = Button(ButtonFrame, text="UPDATE", font=("arial", 13, "bold"), width=14, bg="darkgreen", fg="white")
        btnUpdateMed.grid(row=0, column=1)

        btnDeleteMed = Button(ButtonFrame, text="DELETE", font=("arial", 13, "bold"), width=14, bg="red", fg="white")
        btnDeleteMed.grid(row=0, column=2)

        btnRestMed = Button(ButtonFrame, text="RESET", font=("arial", 13, "bold"), width=14, bg="darkgreen", fg="white")
        btnRestMed.grid(row=0, column=3)

        btnExitMed = Button(ButtonFrame, text="EXIT", font=("arial", 13, "bold"), width=14, bg="darkgreen", fg="white")
        btnExitMed.grid(row=0, column=4)

        # =============Search ===============
        lblSearch = Label(ButtonFrame, font=("arial", 17, "bold"), text="Search By", padx=2, bg="red", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)

        serch_combo = ttk.Combobox(ButtonFrame, width=12, font=("arial", 17, "bold"), state="readonly")
        serch_combo["values"] = ("Ref", "Group Name", "Group No")
        serch_combo.grid(row=0, column=6)
        serch_combo.current(0)

        txtSerch = Entry(ButtonFrame, bd=3, relief=RIDGE, width=12, font=("arial", 17, "bold"))
        txtSerch.grid(row=0, column=7)

        searchBtn = Button(ButtonFrame, text="SEARCH", font=("arial", 13, "bold"), width=13, bg="darkgreen", fg="white")
        searchBtn.grid(row=0, column=8)

        showAll = Button(ButtonFrame, text="SHOW ALL", font=("arial", 13, "bold"), width=13, bg="darkgreen", fg="white")
        showAll.grid(row=0, column=9)

        # =============Group Information =================
        lblGroupName = Label(self.DataFrameLeft, font=("arial", 12, "bold"), text="Group Name:", padx=2, pady=6)
        lblGroupName.grid(row=3, column=0, sticky=W)
        self.txtGroupName = Entry(self.DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        self.txtGroupName.grid(row=3, column=1)

        lblGroupCount = Label(self.DataFrameLeft, font=("arial", 12, "bold"), text="Group Count:", padx=2, pady=6)
        lblGroupCount.grid(row=4, column=0, sticky=W)
        self.txtGroupCount = Entry(self.DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        self.txtGroupCount.grid(row=4, column=1)

        #====================Images on group information ====================
        lblhome = Label(self.DataFrameLeft, font=("arial", 15, "bold"), text="Smart Groups, Smarter Management:", padx=2, pady=6, bg="white", fg="red", width=37)
        lblhome.place(x=410, y=140)

        img2=Image.open("images/download.jpg")
        img2=img2.resize((150,135))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img=Label(self.root, image=self.photoimg2, borderwidth=0)
        lbl_img.place(x=770, y=330)

        img3 = Image.open("images/63e2e74675de8b1c29acdc2a_team-meeting-games.jpg")
        img3 = img3.resize((150, 135))  # Corrected attribute
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img=Label(self.root, image=self.photoimg3, borderwidth=0)
        lbl_img.place(x=620, y=330)

        img4 = Image.open("images/images.jpg")
        img4 = img4.resize((150, 135))  # Corrected attribute
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lbl_img=Label(self.root, image=self.photoimg4, borderwidth=0)
        lbl_img.place(x=475, y=330)


        # =============Add Group Information =================
        lblGroupNumber = Label(DataFrameRight, font=("arial", 12, "bold"), text="Group Number:", padx=2, pady=6)
        lblGroupNumber.grid(row=0, column=0, sticky=W)
        self.txtGroupNumber = Entry(DataFrameRight, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        self.txtGroupNumber.grid(row=0, column=1)

        lblCurrentDate = Label(DataFrameRight, font=("arial", 12, "bold"), text="Date:", padx=2, pady=6)
        lblCurrentDate.grid(row=1, column=0, sticky=W)
        self.txtCurrentDate = Entry(DataFrameRight, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        self.txtCurrentDate.grid(row=1, column=1)
        self.txtCurrentDate.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Insert current date

        lblCurrentTime = Label(DataFrameRight, font=("arial", 12, "bold"), text="Time:", padx=2, pady=6)
        lblCurrentTime.grid(row=2, column=0, sticky=W)
        self.txtCurrentTime = Entry(DataFrameRight, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        self.txtCurrentTime.grid(row=2, column=1)
        self.update_current_time()  # Update the current time
        self.root.after(1000, self.update_time_periodically)  # Schedule the update every 1000 milliseconds

         #====================DataFrameRight=====================
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Group Add Information",fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        # =============Add Group Information =================
        lblGroupNumber = Label(DataFrameRight, font=("arial", 12, "bold"), text="Group Number:", padx=2, pady=6)
        lblGroupNumber.grid(row=0, column=0, sticky=W)
        self.txtGroupNumber = Entry(DataFrameRight, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        self.txtGroupNumber.grid(row=0, column=1)

        lblCurrentDate = Label(DataFrameRight, font=("arial", 12, "bold"), text="Date:", padx=2, pady=6)
        lblCurrentDate.grid(row=1, column=0, sticky=W)
        self.txtCurrentDate = Entry(DataFrameRight, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        self.txtCurrentDate.grid(row=1, column=1)
        self.txtCurrentDate.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Insert current date

        lblCurrentTime = Label(DataFrameRight, font=("arial", 12, "bold"), text="Time:", padx=2, pady=6)
        lblCurrentTime.grid(row=2, column=0, sticky=W)
        self.txtCurrentTime = Entry(DataFrameRight, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        self.txtCurrentTime.grid(row=2, column=1)

        # Update the current time periodically
        self.update_time_periodically()

        img5=Image.open("images/image2.png")
        img5=img5.resize((200,145))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lbl_img=Label(self.root, image=self.photoimg5, borderwidth=0)
        lbl_img.place(x=960, y=330)

        img6=Image.open("images/download (1).jpg")
        img6=img6.resize((200,145))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        lbl_img=Label(self.root, image=self.photoimg6, borderwidth=0)
        lbl_img.place(x=1270, y=330)

         #=======================Add group members========================

        btnAddMembers = Button(self.DataFrameLeft, text="Add Group Members", font=("arial", 12, "bold"), command=self.add_group_members)
        btnAddMembers.grid(row=5, column=0, columnspan=2, pady=10)

        self.group_members_entries = []  # To store dynamically created entry widgets

    def add_group_members(self):
        try:
            group_count = int(self.txtGroupCount.get())
            if 4 <= group_count <= 6:
                # Hide existing entry widgets and labels
                for label, entry in self.group_members_entries:
                    label.grid_forget()
                    entry.grid_forget()

                # Clear the list
                self.group_members_entries = []

                # Create entry widgets and labels for group members
                for i in range(group_count):
                    lblMemberName = Label(self.DataFrameLeft, font=("arial", 12, "bold"), text=f"Member {i + 1}:", padx=2, pady=6)
                    lblMemberName.grid(row=i + 6, column=0, sticky=W)
                    entryMemberName = Entry(self.DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
                    entryMemberName.grid(row=i + 6, column=1)
                    self.group_members_entries.append((lblMemberName, entryMemberName))

                # Update last_group_count
                self.last_group_count = group_count
            else:
                messagebox.showerror("Error", "Group count should be between 4 and 6")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for Group Count")

    def update_current_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.txtCurrentTime.delete(0, END)
        self.txtCurrentTime.insert(0, current_time)

    def update_time_periodically(self):
        self.update_current_time()
        self.root.after(1000, self.update_time_periodically)


        Framedeatils=Frame(self.root,bd=15,relief=RIDGE)
        Framedeatils.place(x=0,y=580,width=1530,height=210)

        #=================Main Table & scrollbar=====================
        Table_frame = Frame(Framedeatils, bd=15, relief=RIDGE, padx=20)
        Table_frame.place(x=0,y=1,width=1500,height=180)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("Group No","Date","Group Name","Group Count","Time","Member 1","Member 2","Member 3","Member 4","Member 5","Member 6"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("Group No",text="Group No")
        self.pharmacy_table.heading("Date",text="Date")
        self.pharmacy_table.heading("Group Name",text="Group Name")
        self.pharmacy_table.heading("Group Count",text="Group Count")
        self.pharmacy_table.heading("Time",text="Time")
        self.pharmacy_table.heading("Member 1",text="Member 1")
        self.pharmacy_table.heading("Member 2",text="Member 2")
        self.pharmacy_table.heading("Member 3",text="Member 3")
        self.pharmacy_table.heading("Member 4",text="Member 4")
        self.pharmacy_table.heading("Member 5",text="Member 5")
        self.pharmacy_table.heading("Member 6",text="Member 6")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("Group No",width=100)
        self.pharmacy_table.column("Date",width=100)
        self.pharmacy_table.column("Group Name",width=100)
        self.pharmacy_table.column("Group Count",width=100)
        self.pharmacy_table.column("Time",width=100)
        self.pharmacy_table.column("Member 1",width=100)
        self.pharmacy_table.column("Member 2",width=100)
        self.pharmacy_table.column("Member 3",width=100)
        self.pharmacy_table.column("Member 4",width=100)
        self.pharmacy_table.column("Member 5",width=100)
        self.pharmacy_table.column("Member 6",width=100)

    def AddData(self):
        group_no = self.txtGroupNumber.get()
        date = self.txtCurrentDate.get()
        time = self.txtCurrentTime.get()
        group_name = self.txtGroupName.get()
        group_member_count = self.txtGroupCount.get()
        member_names = [entry[1].get() for entry in self.group_members_entries]

        if not all([group_no, date, time, group_name, group_member_count] + member_names):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        data_tuple = (group_no, date, group_name, group_member_count, time) + tuple(member_names)
        self.pharmacy_table.insert('', "end", values=data_tuple)

        # Clear the entry fields after adding data
        self.txtGroupNumber.delete(0, END)
        self.txtGroupName.delete(0, END)
        self.txtGroupCount.delete(0, END)
        self.txtCurrentDate.delete(0, END)
        self.txtCurrentDate.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.txtCurrentTime.delete(0, END)

        for entry in self.group_members_entries:
            entry[1].delete(0, END)




if __name__ == "__main__":
    root = Tk()
    obj = GroupManagementSystem(root)
    root.mainloop()
