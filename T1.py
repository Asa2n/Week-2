import customtkinter as ctk

# ตั้งค่าธีมการแสดงผล (System = ตามโหมดของคอมพิวเตอร์, Dark = โหมดมืด, Light = โหมดสว่าง)
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ตั้งค่าหน้าต่างโปรแกรม
        self.title("เครื่องคิดเลข มินิมอล")
        self.geometry("360x520")
        self.resizable(False, False)
        self.configure(fg_color=("#F0F4F8", "#1E1E24"))  # สีพื้นหลัง (Light, Dark)

        self.expression = ""

        # หน้าจอแสดงผล
        self.display = ctk.CTkEntry(
            self, 
            placeholder_text="0", 
            justify="right", 
            font=("Segoe UI", 32, "bold"),
            height=70,
            border_width=0,
            corner_radius=15,
            fg_color=("#FFFFFF", "#2A2A35"),
            text_color=("#333333", "#FFFFFF")
        )
        self.display.pack(padx=20, pady=(25, 15), fill="x")

        # ส่วนพื้นที่วางปุ่ม (Grid Layout)
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # กำหนดโครงสร้างคอลัมน์ (4 คอลัมน์)
        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1, pad=12)
        for i in range(5):
            self.buttons_frame.grid_rowconfigure(i, weight=1, pad=12)

        # รายชื่อปุ่มและพิกัดบน Grid
        buttons = [
            ('C', 0, 0, 'clear'),   ('/', 0, 1, 'operator'), ('*', 0, 2, 'operator'), ('DEL', 0, 3, 'operator'),
            ('7', 1, 0, 'number'),  ('8', 1, 1, 'number'),   ('9', 1, 2, 'number'),   ('-', 1, 3, 'operator'),
            ('4', 2, 0, 'number'),  ('5', 2, 1, 'number'),   ('6', 2, 2, 'number'),   ('+', 2, 3, 'operator'),
            ('1', 3, 0, 'number'),  ('2', 3, 1, 'number'),   ('3', 3, 2, 'number'),   ('=', 3, 3, 'equal'),
            ('0', 4, 0, 'number'),  ('.', 4, 1, 'number')
        ]

        # สร้างและจัดวางปุ่มลงบนหน้าจอ
        for text, row, col, btn_type in buttons:
            self.create_button(text, row, col, btn_type)

    def create_button(self, text, row, col, btn_type):
        # ตั้งค่าสีปุ่มตามประเภทการใช้งานเพื่อความสวยงาม
        if btn_type == 'number':
            fg_color = ("#FFFFFF", "#2A2A35")
            text_color = ("#495057", "#E0E0E0")
            hover_color = ("#E9ECEF", "#3A3A4A")
        elif btn_type == 'operator':
            fg_color = ("#E3F2FD", "#2B3A4A")
            text_color = ("#1E88E5", "#64B5F6")
            hover_color = ("#D0E7FF", "#3B4E66")
        elif btn_type == 'clear':
            fg_color = ("#FFEBEE", "#422525")
            text_color = ("#E53935", "#FF8A80")
            hover_color = ("#FFCDD2", "#5A3333")
        elif btn_type == 'equal':
            fg_color = ("#4FACFE", "#00F2FE")
            text_color = "#FFFFFF"
            hover_color = ("#00F2FE", "#4FACFE")

        # ควบคุมขนาดการขยายตัวของปุ่มเครื่องหมายเท่ากับ (=) ให้ยาวลงมาด้านล่าง
        rowspan = 2 if text == '=' else 1

        btn = ctk.CTkButton(
            self.buttons_frame, 
            text=text, 
            font=("Segoe UI", 20, "bold"),
            fg_color=fg_color,
            text_color=text_color,
            hover_color=hover_color,
            corner_radius=18,
            border_width=0,
            command=lambda t=text: self.on_button_click(t)
        )
        btn.grid(row=row, column=col, rowspan=rowspan, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, char):
        # ล้างหน้าจอ
        if char == 'C':
            self.expression = ""
        # ลบทีละตัวอักษร
        elif char == 'DEL':
            self.expression = self.expression[:-1]
        # คำนวณผลลัพธ์
        elif char == '=':
            try:
                # ตรวจสอบการหารด้วยศูนย์ก่อนคำนวณ
                if '/0' in self.expression:
                    self.expression = "Error (Div by 0)"
                else:
                    # คำนวณผลลัพธ์และปัดเศษทศนิยมให้ดูง่าย
                    result = eval(self.expression)
                    if isinstance(result, float) and result.is_integer():
                        result = int(result)
                    self.expression = str(result)
            except Exception:
                self.expression = "Error"
        # ต่อข้อความตัวเลขหรือเครื่องหมาย
        else:
            if self.expression in ["Error", "Error (Div by 0)"]:
                self.expression = ""
            self.expression += str(char)

        # อัปเดตตัวเลขบนหน้าจอ
        self.display.delete(0, ctk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()