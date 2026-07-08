import os
import http.server
import socketserver
import webbrowser  # เพิ่มไลบรารีสำหรับเปิดเบราว์เซอร์อัตโนมัติ
import threading

# 1. โค้ด HTML สำหรับหน้าเว็บของคุณพีร (เวอร์ชันแมตช์ชื่อไฟล์ profile.jpg.png)
html_content = """<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Peera Phonkhuntod - Profile</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f4f8;
            color: #333;
            margin: 0;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .profile-card {
            background: #ffffff;
            max-width: 500px;
            width: 100%;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            overflow: hidden;
            text-align: center;
            border-top: 8px solid #ff4757; /* ปรับเป็นสีแดงชมพูให้เข้ากับจริตตัวมารดา */
        }
        .avatar-container {
            margin-top: 35px;
            position: relative;
            display: inline-block;
        }
        .profile-img {
            width: 160px;
            height: 220px;
            object-fit: cover; /* ครอบรูปให้ได้สัดส่วนพอดีกรอบ */
            border-radius: 12px;
            border: 4px solid #fff;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        .name {
            font-size: 1.6rem;
            color: #1a1a1a;
            margin: 15px 0 5px 0;
            font-weight: 700;
        }
        .subtitle {
            color: #ff4757;
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 20px;
        }
        /* โซนคำคม Gen Z สุดจึ้ง */
        .quote-box {
            background: linear-gradient(135deg, #ff4757, #ff6b81);
            margin: 0 30px 25px 30px;
            padding: 15px;
            border-radius: 12px;
            font-style: italic;
            font-weight: 700;
            font-size: 1rem;
            color: #fff;
            box-shadow: 0 6px 12px rgba(255, 71, 87, 0.25);
            line-height: 1.4;
        }
        .info-box {
            text-align: left;
            padding: 0 30px;
            margin-bottom: 30px;
        }
        .info-item {
            background: #f8fafc;
            padding: 12px 15px;
            border-radius: 8px;
            margin-bottom: 10px;
            border-left: 4px solid #ff4757;
        }
        .info-label {
            font-size: 0.85rem;
            color: #64748b;
            text-transform: uppercase;
            font-weight: bold;
            display: block;
        }
        .info-value {
            font-size: 1rem;
            color: #334155;
            margin-top: 2px;
        }
        .btn-link {
            display: block;
            background: #1e293b;
            color: #ffffff;
            padding: 14px;
            text-decoration: none;
            font-weight: 600;
            transition: background 0.2s;
            border-bottom-left-radius: 16px;
            border-bottom-right-radius: 16px;
        }
        .btn-link:hover {
            background: #ff4757;
        }
    </style>
</head>
<body>

    <div class="profile-card">
        <div class="avatar-container">
            <img src="Me.png" alt="นายพีร โพนขุนทด" class="profile-img"> </div>
        
        <div class="name">นายพีร โพนขุนทด</div>
        <div class="subtitle">Gen Z ตัวตึงแห่ง MtET @KMUTNB</div>

        <div class="quote-box">
            "งานไม่เคยเท แต่คะแนนเกือบเทกระจาด! จริตตัวพ่อ ขาดทุนย่อยยับ แต่เรื่อง MtET บอกเลยว่าสู้ตายค่ะคุณน้า สภาพพพ! 💅✨"
        </div>
        
        <div class="info-box">
            <div class="info-item">
                <span class="info-label">มหาวิทยาลัย</span>
                <div class="info-value">มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ</div>
            </div>
            <div class="info-item">
                <span class="info-label">ภาควิชา/สาขา</span>
                <div class="info-value">เทคโนโลยีวิศวกรรมเครื่องกลแมคคาทรอนิกส์ (MtET)</div>
            </div>
        </div>

        <a href="https://www.kmutnb.ac.th" target="_blank" class="btn-link">Let's Go To KMUTNB 🚀</a>
    </div>

</body>
</html>
"""

# 2. สร้างไฟล์ index.html อัตโนมัติ
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

PORT = 8888
Handler = http.server.SimpleHTTPRequestHandler

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")

print(f"กำลังเปิด Private Server ที่ http://localhost:{PORT}")
print("หน้าเว็บควรจะเปิดขึ้นมาอัตโนมัติ... ถ้าไม่เปิด ให้เข้าคอมพิวเตอร์ไปที่ http://localhost:8888")
print("กด Ctrl + C ใน Terminal เพื่อปิดเซิร์ฟเวอร์")

# สั่งให้เด้งหน้าเว็บหลังจากเริ่มรันเซิร์ฟเวอร์ไปแล้ว 0.5 วินาที
threading.Timer(0.5, open_browser).start()

# 4. รันเซิร์ฟเวอร์
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()