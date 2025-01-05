import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as tkmb
from tkcalendar import DateEntry
from datetime import datetime as dt
import os
import csv
from TERMINAL import JADWAL_BUS, TERMINALRIL

RIWAYAT_FILE = "riwayat.csv"

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Bubble Bus")
        self.root.configure(fg_color="#BDC4D4")
        self.data_list = []
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.login_form()

    def login_form(self):
        self.clear_root()
        ctk.CTkLabel(self.root, 
                     text="Login", 
                     text_color="#1C2E4A", 
                     font=('Cooper Black', 45, "bold")).place(relx=0.5, rely=0.17, anchor='n')

        Frame1 = ctk.CTkFrame(self.root,
                              fg_color="#F0F3FA")
        Frame1.place(relx=0.5, rely=0.45, anchor='center', relwidth=0.25, relheight=0.3)

        ctk.CTkLabel(Frame1, 
                     text="Email",
                     text_color="#1C2E4A",
                     font=('Cascadia Code SemiBold', 15, "bold")).pack(pady=20)
        self.email_entry = ctk.CTkEntry(Frame1, width=250, border_color="#1C2E4A", font=('Cascadia Code SemiBold', 15, "bold"), justify='center')
        self.email_entry.pack()

        ctk.CTkLabel(Frame1, 
                     text="Password",
                     text_color="#1C2E4A",
                     font=('Cascadia Code SemiBold', 15, "bold")).pack(pady=20)
        self.password_entry = ctk.CTkEntry(Frame1, show="*", width=250, border_color="#1C2E4A", font=('Cascadia Code SemiBold', 15, "bold"), justify='center')
        self.password_entry.pack()

        ctk.CTkButton(self.root, 
                      text="Login",  
                      hover_color="#52677D", 
                      font=('Happy Font TH', 13, "bold"), 
                      fg_color="#1C2E4A", 
                      command=self.login).place(relx=0.5, rely=0.65, anchor='n')

        ctk.CTkButton(self.root, 
                      text="Register", 
                      hover_color="#52677D", 
                      font=('Happy Font TH', 13, "bold"), 
                      fg_color="#1C2E4A", 
                      command=self.register_form).place(relx=0.5, rely=0.75, anchor='n')

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register_form(self):
        self.clear_root()

        ctk.CTkLabel(self.root, 
                     text="Register", 
                     text_color="#1C2E4A", 
                     font=('Cooper Black', 45, "bold")).place(relx=0.5, rely=0.12, anchor='n')

        frame2 = ctk.CTkFrame(self.root,
                        fg_color="#F0F3FA")
        frame2.place(relx=0.5, rely=0.45, anchor='center', relwidth=0.25, relheight=0.43)

        ctk.CTkLabel(frame2, 
                     text="Email",
                     text_color="#1C2E4A",
                     font=('Cascadia Code SemiBold', 15, "bold")).pack(pady=20)
        self.reg_email_entry = ctk.CTkEntry(frame2, width=250, border_color="#1C2E4A", font=('Cascadia Code SemiBold', 15, "bold"), justify='center')
        self.reg_email_entry.pack()

        ctk.CTkLabel(frame2, 
                     text="Password",
                     text_color="#1C2E4A",
                     font=('Cascadia Code SemiBold', 15, "bold")).pack(pady=20)
        self.reg_password_entry = ctk.CTkEntry(frame2, show="*", width=250, border_color="#1C2E4A", font=('Cascadia Code SemiBold', 15, "bold"), justify='center')
        self.reg_password_entry.pack()

        ctk.CTkLabel(frame2, text="Konfirmasi Password",
                     text_color="#1C2E4A",
                     font=('Cascadia Code SemiBold', 15, "bold")).pack(pady=20)
        self.reg_konfirmasi_password_entry = ctk.CTkEntry(frame2, show="*", width=250, border_color="#1C2E4A", font=('Cascadia Code SemiBold', 15, "bold"), justify='center')
        self.reg_konfirmasi_password_entry.pack()

        ctk.CTkButton(self.root, text="Register", 
                      hover_color="#52677D", 
                      font=('Happy Font TH', 13, "bold"), 
                      fg_color="#1C2E4A", 
                      command=self.proses_register).place(relx=0.5, rely=0.71, anchor='n')
        
        ctk.CTkButton(self.root, text="Kembali ke login", 
                      hover_color="#52677D", 
                      font=('Happy Font TH', 13, "bold"), 
                      fg_color="#1C2E4A", 
                      command=self.login_form).place(relx=0.5, rely=0.8, anchor='n')
        
    def proses_register(self):
        email = self.reg_email_entry.get()
        password = self.reg_password_entry.get()
        konfirmasi_password = self.reg_konfirmasi_password_entry.get()

        if not email or not password or not konfirmasi_password:
            tkmb.showwarning("Error", "Email dan password tidak boleh kosong!")
            return

        if not email.endswith("@gmail.com"):
            tkmb.showwarning("Register Gagal", "Email harus berakhiran @gmail.com")
            return

        if password != konfirmasi_password:
            tkmb.showwarning("Error", "Password dan konfirmasi password tidak cocok!")
            return

        if self.cek_akun1(email):
            tkmb.showwarning("Register Gagal", "Email telah digunakan.")
            return

        file_exists = os.path.exists("users.csv")
        with open("users.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists or os.stat("users.csv").st_size == 0:  
                writer.writerow(["email", "password"])  
            writer.writerow([email, password])  

            self.login_form()

    def cek_akun1(self, email):
        if not os.path.exists("users.csv"):
            return False
        with open("users.csv", mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                if row[0] == email:  
                    return True
        return False
    
    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            tkmb.showwarning("Error", "Email dan password tidak boleh kosong!")
            return
        
        if self.cek_akun(email, password):
            self.root.withdraw()
            self.button_formpemesanan(email)
        else:
            tkmb.showwarning("Login Gagal", "Email atau password salah!")

    def cek_akun(self, email, password):
        if not os.path.exists("users.csv"):
            return False
        with open("users.csv", mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                if row[0] == email and row[1] == password:  
                    return True

    def button_formpemesanan(self, email):
        self.root.withdraw()
        new_window=ctk.CTkToplevel(self.root)
        FormPemesanan(new_window, email)

class FormPemesanan:
    def __init__(self, root, email):
        self.root = root
        self.email = email
        self.root.title("Form Pemesanan Tiket - Bubble Bus")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.root.configure(fg_color="#BDC4D4")
        self.data_list = []

        ctk.CTkLabel(self.root, 
                     text="Pemesanan Tiket", 
                     text_color="#1C2E4A", 
                     font=('Cooper Black', 40, "bold")).pack(pady=40)

        self.frame = ctk.CTkFrame(self.root,
                                  fg_color="#F0F3FA", 
                                  corner_radius=15)
        self.frame.place(relx=0.5, rely=0.45, relwidth=0.5, relheight=0.6, anchor="center")

        self.frame1 = ctk.CTkFrame(self.frame,
                                  fg_color="#1C2E4A", 
                                  corner_radius=20)
        self.frame1.place(relx=0.05, rely=0.06, relwidth=0.5, relheight=0.86)

        self.frame2 = ctk.CTkFrame(self.frame,
                                  fg_color="#1C2E4A", 
                                  corner_radius=20)
        self.frame2.place(relx=0.6, rely=0.06, relwidth=0.35, relheight=0.3)

        self.frame21 = ctk.CTkFrame(self.frame2,
                                  fg_color="#1C2E4A", 
                                  corner_radius=20)
        self.frame21.place(relx=0.5, rely=0.5, anchor="center")

        self.frame3 = ctk.CTkFrame(self.frame,
                                  fg_color="#1C2E4A", 
                                  corner_radius=20)
        self.frame3.place(relx=0.6, rely=0.425, relwidth=0.35, relheight=0.3)

        self.frame31 = ctk.CTkFrame(self.frame3,
                                  fg_color="#1C2E4A", 
                                  corner_radius=20)
        self.frame31.place(relx=0.5, rely=0.5, anchor="center")

        self.frame4 = ctk.CTkFrame(self.frame,
                                  fg_color="#F0F3FA", 
                                  corner_radius=20)
        self.frame4.place(relx=0.6, rely=0.775, relwidth=0.35, relheight=0.15)

        ctk.CTkLabel(self.frame1,
                     text="Dari", 
                     text_color="#F0F3FA",
                     font=('Cascadia Code SemiBold', 15, "bold"),
                     fg_color="#1C2E4A").pack(pady=17)

        self.combobox_asal = ttk.Combobox(self.frame1, 
                                             font=("Cascadia Code SemiBold", 11), 
                                             width=30,
                                             justify='center',
                                             values=list(TERMINALRIL.keys()))
        self.combobox_asal.pack()
        self.combobox_asal.bind("<<ComboboxSelected>>", self.perbarui_terminal_asal)

        ctk.CTkLabel(self.frame1,
                     text="Terminal Keberangkatan",
                     text_color="#F0F3FA",
                     font=('Cascadia Code SemiBold', 15, "bold"),
                     fg_color="#1C2E4A").pack(pady=17)

        self.combobox_terminal_asal = ttk.Combobox(self.frame1, 
                                                      font=("Cascadia Code SemiBold", 11), 
                                                      width=30,
                                                      justify='center')
        self.combobox_terminal_asal.pack()

        ctk.CTkLabel(self.frame1,
                     text="Ke",
                     text_color= "#F0F3FA",
                     font=("Cascadia Code SemiBold", 14, "bold"),
                     fg_color="#1C2E4A").pack(pady=17)

        self.combobox_tujuan = ttk.Combobox(self.frame1, 
                                               font=("Cascadia Code SemiBold", 11), 
                                               width=30,
                                               justify='center')
        self.combobox_tujuan.pack()
        self.combobox_tujuan.bind("<<ComboboxSelected>>", self.perbarui_terminal_tujuan)

        ctk.CTkLabel(self.frame1,
                     text="Terminal Tujuan",
                     text_color="#F0F3FA",
                     font=("Cascadia Code SemiBold", 14, "bold"),
                     fg_color="#1C2E4A").pack(pady=17)

        self.combobox_terminal_tujuan = ttk.Combobox(self.frame1, 
                                                        font=("Cascadia Code SemiBold", 11), 
                                                        width=30,
                                                        justify='center')
        self.combobox_terminal_tujuan.pack()

        ctk.CTkLabel(self.frame21,
                     text="Tanggal",
                     text_color="#F0F3FA",
                     font=("Cascadia Code SemiBold", 14, "bold"),
                     fg_color="#1C2E4A").pack()

        self.cal = DateEntry(self.frame21, width=20, 
                             background="#1C2E4A", 
                             foreground='white', 
                             borderwidth=1, 
                             font=("Cascadia Code SemiBold", 11), justify="center")
        self.cal.pack(pady=17)

        ctk.CTkLabel(self.frame31,
                     text="Jumlah Penumpang",
                     text_color="#F0F3FA",
                     font=("Cascadia Code SemiBold", 14, "bold"),
                     fg_color="#1C2E4A").pack()

        self.spinner_penumpang = ttk.Spinbox(self.frame31, 
                                            from_=1, to=10, 
                                            font=("Cascadia Code SemiBold", 11), 
                                            width=20,
                                            justify="center")
        self.spinner_penumpang.pack(pady=17)
        self.spinner_penumpang.set(1)

        pesan1 = ctk.CTkButton(self.frame4, 
                               text="Tampilkan Bus",
                               hover_color="#52677D",
                               command=lambda:self.simpan_pemesanan(email), 
                               font=("Happy Font TH", 13, "bold"), 
                               fg_color="#1C2E4A")
        pesan1.place(relx=0.5, rely=0.5, anchor="center")

        pesan2 = ctk.CTkButton(self.root, 
                               text="Riwayat Pemesanan", 
                               hover_color="#52677D",
                               command=lambda:self.tampilkan_histori(email), 
                               font=("Happy Font TH", 13, "bold"), 
                               fg_color="#1C2E4A")
        pesan2.place(relx=0.5, rely=0.8, anchor='n')

        self.root.mainloop()

    def perbarui_terminal_asal(self, event=None): 
        kota_asal = self.combobox_asal.get() 
        if kota_asal in TERMINALRIL: 
            self.combobox_terminal_asal["values"]=TERMINALRIL[kota_asal] 
            self.combobox_terminal_asal.set("") 
            
        tujuan = [kota for kota in TERMINALRIL if kota != kota_asal] 
        self.combobox_tujuan["values"] = tujuan
        self.combobox_tujuan.set("")

    def perbarui_terminal_tujuan(self, event=None): 
        kota_tujuan = self.combobox_tujuan.get() 
        if kota_tujuan in TERMINALRIL: 
            self.combobox_terminal_tujuan["values"]=TERMINALRIL[kota_tujuan]
            self.combobox_terminal_tujuan.set("")

    def simpan_pemesanan(self, email):
        email = self.email
        kota_asal = self.combobox_asal.get()
        terminal_asal = self.combobox_terminal_asal.get()
        kota_tujuan = self.combobox_tujuan.get()
        terminal_tujuan = self.combobox_terminal_tujuan.get()
        tanggal = self.cal.get_date()
        jumlah_penumpang = int(self.spinner_penumpang.get())

        if not kota_asal or not terminal_asal or not kota_tujuan or not terminal_tujuan or not tanggal or not jumlah_penumpang:
            tkmb.showwarning("Error","Form Pemesanan Tiket tidak boleh ada yang kosong")
            return
        
        elif tanggal < dt.now().date():
            tkmb.showwarning("Error","Tanggal tidak boleh di masa lalu")
            return
        
        self.root.withdraw()
        new_window = ctk.CTkToplevel(self.root)
        JadwalBus(new_window, email, kota_asal, terminal_asal, kota_tujuan, terminal_tujuan, tanggal, jumlah_penumpang)

    def tampilkan_histori(self, email):
        self.root.withdraw()
        new_window = ctk.CTkToplevel(self.root)
        history(new_window, email)

class history:
    def __init__(self, root, email):
        self.root = root
        self.email = email

        self.root.title("Riwayat Pesanan - Bubble Bus")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.root.configure(fg_color="#BDC4D4")
        self.data_list = []

        ctk.CTkLabel(self.root, 
                    text="Riwayat Pesanan", 
                    text_color="#1C2E4A", 
                    font=('Cooper Black', 40, "bold")).pack(pady=20)
        
        self.data_list = self.cek_histori(RIWAYAT_FILE)
        self.tampilan_histori(email)

        button_back = ctk.CTkButton(self.root,
                                    text="Kembali",
                                    command=lambda: self.kembali_form(email),
                                    fg_color="#1C2E4A",
                                    font=("Happy Font TH", 13, "bold"),
                                    hover_color="#52677D")
        button_back.pack(pady=20)

    def cek_histori(self, email):
        data = []
        with open(email, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) 
    
            for row in reader:
                if len(row) >= 11:
                    if row[0] == self.email:
                        data.append(row)
        return data
    
    def tampilan_histori(self, email):
        for row in self.data_list:
            frame_riwayat = ctk.CTkFrame(self.root, fg_color="#1C2E4A")
            frame_riwayat.pack(pady=10, padx=350, fill="x")

            label_text = f"""
    Tanggal     : {row[1]}
    Dari        : {row[2]} ({row[3]})
    Ke          : {row[4]} ({row[5]})
    Penumpang   : {row[6]}
    Jam         : {row[7]} - {row[8]}
    Harga       : Rp.{row[9]} per penumpang
    Total Harga : Rp.{row[10]}
            """
            ctk.CTkLabel(frame_riwayat, 
                         text=label_text, 
                         fg_color="#1C2E4A", 
                         text_color="#F0F3FA",
                         font=("Cascadia Code SemiBold", 12, "bold"),
                         anchor="w",
                         justify="left").pack(side="left", pady=10, padx=20)  

    def kembali_form(self, email):
        self.root.withdraw()
        new_window=ctk.CTkToplevel(self.root)
        FormPemesanan(new_window, email)

class JadwalBus:
    def __init__(self, root, email, kota_asal, terminal_asal, kota_tujuan, terminal_tujuan, tanggal, jumlah_penumpang):
        self.root = root
        self.email = email
        self.kota_asal = kota_asal
        self.terminal_asal = terminal_asal
        self.kota_tujuan = kota_tujuan
        self.terminal_tujuan = terminal_tujuan
        self.tanggal = tanggal
        self.jumlah_penumpang = jumlah_penumpang
        self.setup_ui(email)

    def setup_ui(self, email):
        self.root.title("Jadwal Bus - Bubble Bus")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.root.configure(fg_color="#BDC4D4")

        label_title = ctk.CTkLabel(self.root,
                                   text="Jadwal Bus", 
                                   font=("Cooper Black", 40), text_color="#1C2E4A")
        label_title.pack(pady=60)

        frame = ctk.CTkFrame(self.root, fg_color="#BDC4D4")
        frame.place(relx=0.5, rely=0.4, relwidth=0.7, relheight=0.4, anchor="center")

        for jadwal in JADWAL_BUS:          
            if (jadwal["kota_asal"] == self.kota_asal and 
                jadwal["terminal_asal"] == self.terminal_asal and 
                jadwal["kota_tujuan"] == self.kota_tujuan and 
                jadwal["terminal_tujuan"] == self.terminal_tujuan):

                frame_bus = ctk.CTkFrame(frame, fg_color="#1C2E4A")
                frame_bus.pack(fill="x", padx=30, pady=10)

                label_info = ctk.CTkLabel(frame_bus,
                                        text=(
                                        f"{jadwal['kota_asal']} - {jadwal['kota_tujuan']}\n"
                                        f"{jadwal['jam_keberangkatan']} - {jadwal['jam_tiba']}\n"
                                        f"Rp.{jadwal['harga']}\n"
                                        f"{jadwal['terminal_asal']}- {jadwal['terminal_tujuan']}"),
                                        font=("Cascadia Code SemiBold", 15, "bold"),
                                        fg_color="#1C2E4A",
                                        text_color="#F0F3FA",
                                        justify="left") 
                label_info.pack(side="left", padx=20, pady=20)

                button_pilih = ctk.CTkButton(frame_bus,
                                            text="Pilih",
                                            command=lambda b=jadwal: self.pilih_bus(b['jam_keberangkatan'], b['jam_tiba'], b['harga']),
                                            text_color="#1C2E4A",
                                            fg_color="#F0F3FA",
                                            hover_color="#BDC4D4",
                                            font=("Happy Font TH", 13, "bold"))
                button_pilih.pack(side="right", padx=50)
        
        button_cetak = ctk.CTkButton(self.root,
                                    text="Kembali",
                                    command=lambda: self.kembali_ke_form_pemesanan(email),
                                    fg_color="#1C2E4A",
                                    font=("Happy Font TH", 13, "bold"),
                                    hover_color="#52677D")
        button_cetak.place(relx=0.5, rely=0.65, anchor='n')

    def pilih_bus(self, jam_keberangkatan, jam_tiba, harga):
        self.jam_keberangkatan = jam_keberangkatan
        self.jam_tiba = jam_tiba
        self.harga = harga
        self.buat_form_pemesanan(jam_keberangkatan, jam_tiba, harga)

    def buat_form_pemesanan(self, jam_keberangkatan, jam_tiba, harga):
        email = self.email
        kota_asal = self.kota_asal
        terminal_asal = self.terminal_asal
        kota_tujuan = self.kota_tujuan
        terminal_tujuan = self.terminal_tujuan
        tanggal = self.tanggal
        jumlah_penumpang = self.jumlah_penumpang
        jam_keberangkatan = self.jam_keberangkatan
        jam_tiba = self.jam_tiba
        harga = self.harga

        self.root.withdraw()
        new_window = ctk.CTkToplevel(self.root)
        Cetak_tiket(new_window, email, kota_asal, terminal_asal, kota_tujuan, terminal_tujuan, tanggal, jumlah_penumpang, jam_keberangkatan, jam_tiba, harga)

    def kembali_ke_form_pemesanan(self, email):
        self.root.withdraw()
        new_window=ctk.CTkToplevel(self.root)
        FormPemesanan(new_window, email)

class Cetak_tiket:
    def __init__(self, root, email, kota_asal, terminal_asal, kota_tujuan, terminal_tujuan, tanggal, jumlah_penumpang, jam_keberangkatan, jam_tiba, harga):
        self.root = root
        self.email = email
        self.kota_asal = kota_asal
        self.terminal_asal = terminal_asal
        self.kota_tujuan = kota_tujuan
        self.terminal_tujuan = terminal_tujuan
        self.tanggal = tanggal
        self.jumlah_penumpang = jumlah_penumpang
        self.jam_keberangkatan = jam_keberangkatan
        self.jam_tiba = jam_tiba
        self.harga = harga

        self.total_harga = self.harga * self.jumlah_penumpang

        self.setup_print(email, kota_asal, terminal_asal, kota_tujuan, terminal_tujuan, tanggal, jumlah_penumpang, jam_keberangkatan, jam_tiba, harga, self.total_harga)

    def setup_print(self, email, kota_asal, terminal_asal, kota_tujuan, terminal_tujuan, tanggal, jumlah_penumpang, jam_keberangkatan, jam_tiba, harga, total_harga):
        self.total_harga = total_harga
        self.root.title("Tiket - Bubble Bus")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.root.configure(fg_color="#BDC4D4")

        ctk.CTkLabel(self.root, 
                     text="Tiket", 
                     text_color="#1C2E4A", 
                     font=('Cooper Black', 40, "bold")).pack(pady=120)

        self.frame = ctk.CTkFrame(self.root,
                                  fg_color="#1C2E4A", 
                                  corner_radius=15)
        self.frame.place(relx=0.5, rely=0.45, relwidth=0.5, relheight=0.3, anchor="center")
        
        tiket_text = f"""
Email                     : {email}
Dari                      : {kota_asal} ({terminal_asal})
Ke                        : {kota_tujuan} ({terminal_tujuan})
Tanggal                   : {tanggal}
Jumlah Penumpang          : {jumlah_penumpang}
Harga Tiket Per penumpang : Rp.{harga}
Total harga tiket         : Rp.{total_harga}
Jam                       : {jam_keberangkatan} - {jam_tiba}
    """       
        tiket_label = ctk.CTkLabel(self.frame,
                                  text=tiket_text,
                                  fg_color="#1C2E4A",
                                  text_color="#F0F3FA",
                                  font=('Cascadia Code SemiBold', 15, "bold"),
                                  justify="left")
        tiket_label.place(relx=0.5, rely=0.5, anchor="center")

        button_ok = ctk.CTkButton(self.root,
                                text="Ok",
                                fg_color="#1C2E4A",
                                text_color="#F0F3FA",
                                font=('Cascadia Code SemiBold', 13, "bold"),
                                command=lambda: self.simpan_histori(email, tanggal, kota_asal, terminal_asal, kota_tujuan, terminal_tujuan, jumlah_penumpang, jam_keberangkatan, jam_tiba, harga, total_harga))
        button_ok.place(relx=0.5, rely=0.7, anchor="center")

    def simpan_histori(self, email, tanggal, kota_asal, terminal_asal, kota_tujuan, terminal_tujuan, jumlah_penumpang, jam_keberangkatan, jam_tiba, harga, total_harga):
        if not os.path.exists(RIWAYAT_FILE):
            return False

        with open(RIWAYAT_FILE, mode="a", newline="") as file: 
            writer = csv.writer(file) 
            writer.writerow([email, tanggal, kota_asal, terminal_asal, kota_tujuan, terminal_tujuan, jumlah_penumpang, jam_keberangkatan, jam_tiba, harga, total_harga])
            
        self.kembali(email)

    def kembali(self, email):
        self.root.withdraw()
        new_window=ctk.CTkToplevel(self.root)
        FormPemesanan(new_window, email)

if __name__ == "__main__":
    root = ctk.CTk()
    app = Login(root)
    root.mainloop()