from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymongo
from bson.objectid import ObjectId

MONGO_URI = "mongodb://127.0.0.1:27017/laburs"   # <-- aapka URI

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.title('employee management system')
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg='white')

        # ---------------- Variables ----------------
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_marital = StringVar()
        self.var_doj = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_salary = StringVar()
        self.var_dob = StringVar()

        # Search vars
        self.var_com_search = StringVar()
        self.var_search_text = StringVar()

        # ---------------- MongoDB Connection ----------------
        try:
            self.client = pymongo.MongoClient(MONGO_URI)
            # If you provided DB in URI, it's okay; else explicitly use 'laburs'
            self.db = self.client['laburs']
            self.collection = self.db['employees']
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not connect to MongoDB:\n{e}")
            raise

        # ---------------- Title ----------------
        lbl_title = Label(self.root, text='employee management system',
                          font=('times new roman', 37, 'bold'),
                          fg='darkblue', bg='white')
        lbl_title.place(x=0, y=0, width=1530, height=50)

        # ---------------- Image frame ----------------
        img_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_Frame.place(x=0, y=50, width=1530, height=160)

        # Safe image loading (if image missing, skip)
        try:
            img1 = Image.open('college/im1.png').resize((540,160), Image.LANCZOS)
            self.photo1 = ImageTk.PhotoImage(img1)
            Label(img_Frame, image=self.photo1).place(x=0, y=0, width=540, height=160)
        except Exception:
            pass
        try:
            img2 = Image.open('college/kk.png').resize((540,160), Image.LANCZOS)
            self.photo2 = ImageTk.PhotoImage(img2)
            Label(img_Frame, image=self.photo2).place(x=540, y=0, width=540, height=160)
        except Exception:
            pass
        try:
            img3 = Image.open('college/im3.png').resize((540,160), Image.LANCZOS)
            self.photo3 = ImageTk.PhotoImage(img3)
            Label(img_Frame, image=self.photo3).place(x=1080, y=0, width=540, height=160)
        except Exception:
            pass

        # ---------------- Main frame ----------------
        main_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        main_Frame.place(x=10, y=220, width=1500, height=560)

        # Upper Frame (form)
        upper_Frame = LabelFrame(main_Frame, bd=2, relief=RIDGE, bg='white',
                                 text='employee information', font=('times new roman', 11, 'bold'), fg='red')
        upper_Frame.place(x=10, y=10, width=1480, height=290)

        # --- form fields (using same layout as aapne diya) ---
        Label(upper_Frame, text="Department", font=("arial", 11, "bold"), bg="white").grid(row=0, column=0, padx=2, sticky=W)
        ttk.Entry(upper_Frame, textvariable=self.var_dep, width=22, font=("arial", 11, "bold")).grid(row=0, column=1, padx=2, pady=7)

        Label(upper_Frame, text="Name:", font=("arial", 12, "bold"), bg="white").grid(row=0, column=2, padx=2, pady=7, sticky=W)
        ttk.Entry(upper_Frame, textvariable=self.var_name, width=22, font=("arial", 12, "bold")).grid(row=0, column=3, padx=2, pady=7)

        Label(upper_Frame, text="Designation", font=("arial", 12, "bold"), bg="white").grid(row=1, column=0, padx=2, pady=7, sticky=W)
        ttk.Entry(upper_Frame, textvariable=self.var_designation, width=22, font=("arial", 11, "bold")).grid(row=1, column=1, padx=2, pady=7, sticky=W)

        Label(upper_Frame, text="Email", font=("arial", 12, "bold"), bg="white").grid(row=1, column=2, padx=2, pady=7, sticky=W)
        ttk.Entry(upper_Frame, textvariable=self.var_email, width=22, font=("arial", 11, "bold")).grid(row=1, column=3, padx=2, pady=7)

        Label(upper_Frame, text="Address", font=("arial", 12, "bold"), bg="white").grid(row=2, column=0, padx=2, pady=7, sticky=W)
        ttk.Entry(upper_Frame, textvariable=self.var_address, width=22, font=("arial", 11, "bold")).grid(row=2, column=1, padx=2, pady=7)

        Label(upper_Frame, text="Marital Status", font=("arial", 12, "bold"), bg="white").grid(row=2, column=2, padx=2, pady=7, sticky=W)
        combo_marital = ttk.Combobox(upper_Frame, textvariable=self.var_marital, width=20, font=("arial", 11, "bold"), state="readonly")
        combo_marital['values'] = ("Single", "Married", "Divorced", "Widowed")
        combo_marital.grid(row=2, column=3, padx=2, pady=7)

        Label(upper_Frame, text="Date of Joining", font=("arial", 12, "bold"), bg="white").grid(row=3, column=0, padx=2, pady=7, sticky=W)
        ttk.Entry(upper_Frame, textvariable=self.var_doj, width=22, font=("arial", 11, "bold")).grid(row=3, column=1, padx=2, pady=7)

        Label(upper_Frame, text="Gender", font=("arial", 12, "bold"), bg="white").grid(row=3, column=2, padx=2, pady=7, sticky=W)
        gender_frame = Frame(upper_Frame, bg="white")
        gender_frame.grid(row=3, column=3, padx=2, pady=7, sticky=W)
        Radiobutton(gender_frame, text="Male", variable=self.var_gender, value="Male", font=("arial", 11), bg="white").grid(row=0, column=0, padx=5)
        Radiobutton(gender_frame, text="Female", variable=self.var_gender, value="Female", font=("arial", 11), bg="white").grid(row=0, column=1, padx=5)

        Label(upper_Frame, text="Phone Number", font=("arial", 12, "bold"), bg="white").grid(row=4, column=2, padx=2, pady=7, sticky=W)
        ttk.Entry(upper_Frame, textvariable=self.var_phone, width=22, font=("arial", 11, "bold")).grid(row=4, column=3, padx=2, pady=7)

        Label(upper_Frame, text="Country", font=("arial", 12, "bold"), bg="white").grid(row=5, column=0, padx=2, pady=7, sticky=W)
        combo_country = ttk.Combobox(upper_Frame, textvariable=self.var_country, width=20, font=("arial", 11, "bold"), state="readonly")
        combo_country['values'] = ("USA", "Canada", "UK", "Australia", "India", "Others")
        combo_country.grid(row=5, column=1, padx=2, pady=7)

        Label(upper_Frame, text="Select ID Proof", font=("arial", 12, "bold"), bg="white").grid(row=2, column=4, padx=2, pady=7, sticky=W)
        combo_id_proof = ttk.Combobox(upper_Frame, textvariable=self.var_idproofcomb, width=20, font=("arial", 11, "bold"), state="readonly")
        combo_id_proof['values'] = ("Pan Card", "Driver's License", "Adhar Card", "Voter ID")
        combo_id_proof.grid(row=2, column=5, padx=2, pady=7)

        Label(upper_Frame, text="ID Proof Number", font=("arial", 12, "bold"), bg="white").grid(row=3, column=4, padx=2, pady=7, sticky=W)
        ttk.Entry(upper_Frame, textvariable=self.var_idproof, width=22, font=("arial", 11, "bold")).grid(row=3, column=5, padx=2, pady=7)

        Label(upper_Frame, text="Salary", font=("arial", 12, "bold"), bg="white").grid(row=5, column=2, padx=2, pady=7, sticky=W)
        ttk.Entry(upper_Frame, textvariable=self.var_salary, width=22, font=("arial", 11, "bold")).grid(row=5, column=3, padx=2, pady=7)

        Label(upper_Frame, text="Date of Birth", font=("arial", 12, "bold"), bg="white").grid(row=6, column=0, padx=2, pady=7, sticky=W)
        ttk.Entry(upper_Frame, textvariable=self.var_dob, width=22, font=("arial", 11, "bold")).grid(row=6, column=1, padx=2, pady=7)

        # image 4 (mask)
        try:
            img_mask = Image.open('college/img4.png').resize((220,220), Image.LANCZOS)
            self.photomask = ImageTk.PhotoImage(img_mask)
            Label(upper_Frame, image=self.photomask).place(x=1000, y=0, width=178, height=220)
        except Exception:
            pass

        # button frame
        button_Frame = Frame(upper_Frame, bd=2, relief=RIDGE, bg='white')
        button_Frame.place(x=1170, y=10, width=170, height=210)

        Button(button_Frame, text="Save", command=self.add_employee, font=("arial",11,"bold"), width=16, bg='red', fg='white').grid(row=0, column=0, padx=1, pady=3)
        Button(button_Frame, text="Update", command=self.update_employee, font=("arial",11,"bold"), width=16, bg='red', fg='white').grid(row=1, column=0, padx=1, pady=3)
        Button(button_Frame, text="Delete", command=self.delete_employee, font=("arial",11,"bold"), width=16, bg='red', fg='white').grid(row=2, column=0, padx=1, pady=3)
        Button(button_Frame, text="Clear", command=self.clear_fields, font=("arial",11,"bold"), width=16, bg='red', fg='white').grid(row=3, column=0, padx=1, pady=3)

        # ---------------- Down frame (table + search) ----------------
        down_Frame = LabelFrame(main_Frame, bd=2, relief=RIDGE, bg='white',
                                text='employee information table', font=('times new roman', 11, 'bold'), fg='red')
        down_Frame.place(x=10, y=300, width=1480, height=260)

        # Search frame
        search_Frame = LabelFrame(down_Frame, bd=2, relief=RIDGE, bg='white',
                                  text='search employe information', font=('times new roman', 11, 'bold'), fg='black')
        search_Frame.place(x=0, y=0, width=1470, height=60)

        Label(search_Frame, text="Search By", font=("arial",11,"bold"), fg='white', bg="red").grid(row=0, column=0, sticky=W, padx=5)
        com_txt_search = ttk.Combobox(search_Frame, textvariable=self.var_com_search, state="readonly", font=("arial",12,"bold"), width=18)
        com_txt_search['values'] = ("select option", "phone", "id_proof", "name", "dep")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        ttk.Entry(search_Frame, textvariable=self.var_search_text, width=22, font=("arial",11,"bold")).grid(row=0, column=3, padx=5)
        Button(search_Frame, text="Search", command=self.search_data, font=("arial",11,"bold"), width=14, fg="red", bg="black").grid(row=0, column=7, padx=5)
        Button(search_Frame, text="Show All", command=self.fetch_data, font=("arial",11,"bold"), width=14, fg="red", bg="black").grid(row=0, column=4, padx=5)

        # Table frame
        table_Frame = Frame(down_Frame, bd=3, relief=RIDGE)
        table_Frame.place(x=0, y=60, width=1470, height=170)

        scroll_x = ttk.Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_Frame, orient=VERTICAL)

        columns = ('dep', 'name', 'degi', 'email', 'address', 'merried', 'dob', 'doj',
                   'idproofcomb', 'idproof', 'gender', 'phone', 'country', 'salary')

        self.employee_table = ttk.Treeview(table_Frame, columns=columns, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, show='headings')

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        # headings
        self.employee_table.heading('dep', text="Department")
        self.employee_table.heading('name', text="Name")
        self.employee_table.heading('degi', text="Degignition")
        self.employee_table.heading('email', text="Email")
        self.employee_table.heading('address', text="Address")
        self.employee_table.heading('merried', text="Married Status")
        self.employee_table.heading('dob', text="DOb")
        self.employee_table.heading('doj', text="DOJ")
        self.employee_table.heading('idproofcomb', text="ID Type")
        self.employee_table.heading('idproof', text="ID Proof")
        self.employee_table.heading('gender', text="Gander")
        self.employee_table.heading('phone', text="Phone")
        self.employee_table.heading('country', text="Country")
        self.employee_table.heading('salary', text="Salary")

        for col in columns:
            self.employee_table.column(col, width=100)

        self.employee_table.pack(fill=BOTH, expand=1)

        # bind select
        self.employee_table.bind("<ButtonRelease-1>", self.get_cursor)

        # load data initially
        self.fetch_data()

    # ---------------- Functions ----------------
    def add_employee(self):
        if self.var_name.get().strip() == "" or self.var_phone.get().strip() == "":
            messagebox.showerror("Error", "Name and Phone required!")
            return
        data = {
            "dep": self.var_dep.get().strip(),
            "name": self.var_name.get().strip(),
            "designation": self.var_designation.get().strip(),
            "email": self.var_email.get().strip(),
            "address": self.var_address.get().strip(),
            "marital": self.var_marital.get().strip(),
            "dob": self.var_dob.get().strip(),
            "doj": self.var_doj.get().strip(),
            "idproofcomb": self.var_idproofcomb.get().strip(),
            "idproof": self.var_idproof.get().strip(),
            "gender": self.var_gender.get().strip(),
            "phone": self.var_phone.get().strip(),
            "country": self.var_country.get().strip(),
            "salary": self.var_salary.get().strip()
        }
        try:
            self.collection.insert_one(data)
            messagebox.showinfo("Success", "Employee added successfully!")
            self.fetch_data()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add employee:\n{e}")

    def fetch_data(self):
        try:
            records = self.collection.find()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in records:
                iid = str(row.get("_id"))
                self.employee_table.insert("", END, iid=iid, values=(
                    row.get("dep", ""), row.get("name", ""), row.get("designation", ""), row.get("email", ""),
                    row.get("address", ""), row.get("marital", ""), row.get("dob", ""), row.get("doj", ""),
                    row.get("idproofcomb", ""), row.get("idproof", ""), row.get("gender", ""),
                    row.get("phone", ""), row.get("country", ""), row.get("salary", "")
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data:\n{e}")

    def get_cursor(self, event=None):
        selected_iid = self.employee_table.focus()
        if not selected_iid:
            return
        try:
            doc = self.collection.find_one({"_id": ObjectId(selected_iid)})
            if doc:
                self.var_dep.set(doc.get("dep", ""))
                self.var_name.set(doc.get("name", ""))
                self.var_designation.set(doc.get("designation", ""))
                self.var_email.set(doc.get("email", ""))
                self.var_address.set(doc.get("address", ""))
                self.var_marital.set(doc.get("marital", ""))
                self.var_dob.set(doc.get("dob", ""))
                self.var_doj.set(doc.get("doj", ""))
                self.var_idproofcomb.set(doc.get("idproofcomb", ""))
                self.var_idproof.set(doc.get("idproof", ""))
                self.var_gender.set(doc.get("gender", ""))
                self.var_phone.set(doc.get("phone", ""))
                self.var_country.set(doc.get("country", ""))
                self.var_salary.set(doc.get("salary", ""))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load record:\n{e}")

    def update_employee(self):
        selected_iid = self.employee_table.focus()
        if not selected_iid:
            messagebox.showerror("Error", "Select a record to update!")
            return
        new_data = {
            "dep": self.var_dep.get().strip(),
            "name": self.var_name.get().strip(),
            "designation": self.var_designation.get().strip(),
            "email": self.var_email.get().strip(),
            "address": self.var_address.get().strip(),
            "marital": self.var_marital.get().strip(),
            "dob": self.var_dob.get().strip(),
            "doj": self.var_doj.get().strip(),
            "idproofcomb": self.var_idproofcomb.get().strip(),
            "idproof": self.var_idproof.get().strip(),
            "gender": self.var_gender.get().strip(),
            "phone": self.var_phone.get().strip(),
            "country": self.var_country.get().strip(),
            "salary": self.var_salary.get().strip()
        }
        try:
            self.collection.update_one({"_id": ObjectId(selected_iid)}, {"$set": new_data})
            messagebox.showinfo("Success", "Employee updated successfully!")
            self.fetch_data()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update:\n{e}")

    def delete_employee(self):
        selected_iid = self.employee_table.focus()
        if not selected_iid:
            messagebox.showerror("Error", "Select a record to delete!")
            return
        ans = messagebox.askyesno("Confirm", "Are you sure you want to delete this record?")
        if ans:
            try:
                self.collection.delete_one({"_id": ObjectId(selected_iid)})
                messagebox.showinfo("Success", "Employee deleted successfully!")
                self.fetch_data()
                self.clear_fields()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete:\n{e}")

    def clear_fields(self):
        self.var_dep.set("")
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_marital.set("")
        self.var_doj.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_idproofcomb.set("")
        self.var_idproof.set("")
        self.var_salary.set("")
        self.var_dob.set("")
        self.var_com_search.set("select option")
        self.var_search_text.set("")

    def search_data(self):
        key = self.var_com_search.get()
        txt = self.var_search_text.get().strip()
        if key == "select option" or txt == "":
            messagebox.showerror("Error", "Select search option and enter search text")
            return

        query = {}
        if key == "phone":
            query = {"phone": txt}
        elif key == "id_proof" or key == "idproof":
            query = {"idproof": txt}
        elif key == "name":
            query = {"name": {"$regex": txt, "$options": "i"}}
        elif key == "dep":
            query = {"dep": {"$regex": txt, "$options": "i"}}
        else:
            messagebox.showerror("Error", "Unsupported search key")
            return

        try:
            records = self.collection.find(query)
            self.employee_table.delete(*self.employee_table.get_children())
            count = 0
            for row in records:
                count += 1
                iid = str(row.get("_id"))
                self.employee_table.insert("", END, iid=iid, values=(
                    row.get("dep", ""), row.get("name", ""), row.get("designation", ""), row.get("email", ""),
                    row.get("address", ""), row.get("marital", ""), row.get("dob", ""), row.get("doj", ""),
                    row.get("idproofcomb", ""), row.get("idproof", ""), row.get("gender", ""),
                    row.get("phone", ""), row.get("country", ""), row.get("salary", "")
                ))
            if count == 0:
                messagebox.showinfo("Result", "No records found")
        except Exception as e:
            messagebox.showerror("Error", f"Search failed:\n{e}")


if __name__ == '__main__':
    root = Tk()
    obj = Employee(root)
    root.mainloop()
