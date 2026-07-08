import tkinter as tk
from tkinter import messagebox
import random

# กำหนดตัวเลือก
choices = ["ค้อน", "กระดาษ", "กรรไกร"]
emojis = {"ค้อน": "✊", "กระดาษ": "✋", "กรรไกร": "✌️"}

# ตัวแปรเก็บคะแนน
player_score = 0
computer_score = 0

def play(player_choice):
    global player_score, computer_score
    
    # บอตสุ่มเลือก
    computer_choice = random.choice(choices)
    
    # อัปเดตการแสดงผลการเลือก (โชว์อิโมจิใหญ่ ๆ)
    lbl_player_pick.config(text=f"{emojis[player_choice]}\n{player_choice}")
    lbl_bot_pick.config(text=f"{emojis[computer_choice]}\n{computer_choice}")
    
    # ตรวจสอบผลลัพธ์
    if player_choice == computer_choice:
        result_text = "💥 เสมอจ้า! 💥"
        lbl_result.config(fg="#ffc107", bg="#2b2b2b")  # สีเหลืองนีออน
    elif (player_choice == "ค้อน" and computer_choice == "กรรไกร") or \
         (player_choice == "กระดาษ" and computer_choice == "ค้อน") or \
         (player_choice == "กรรไกร" and computer_choice == "กระดาษ"):
        result_text = "🔥 คุณชนะรอบนี้! 🔥"
        player_score += 1
        lbl_result.config(fg="#00ff66", bg="#1a3a20")  # สีเขียวนีออน ชนะ
    else:
        result_text = "💀 บอตชนะรอบนี้! 💀"
        computer_score += 1
        lbl_result.config(fg="#ff3333", bg="#3a1a1a")  # สีแดงนีออน แพ้
        
    # อัปเดตข้อความผลลัพธ์และคะแนนบนหน้าจอ
    lbl_result.config(text=result_text)
    lbl_score.config(text=f"{player_score}   VS   {computer_score}")
    
    # เช็กผู้ชนะระบบ 2 ใน 3
    if player_score == 2:
        messagebox.showinfo("VICTORY!", "🏆 ยินดีด้วย!! คุณคือแชมป์เปี้ยน 🏆")
        reset_game()
    elif computer_score == 2:
        messagebox.showinfo("GAME OVER", "💀 พ่ายแพ้! บอตครองเมือง ไว้มาแก้ตัวใหม่นะ 💀")
        reset_game()

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    lbl_score.config(text="0   VS   0")
    lbl_player_pick.config(text="❓\nรอเลือก...")
    lbl_bot_pick.config(text="❓\nรอเลือก...")
    lbl_result.config(text="ใครได้ 2 คะแนนก่อน ชนะเลิศ!", fg="#00ffff", bg="#1f1f1f")

# --- สร้างหน้าต่างโปรแกรมหลัก ---
window = tk.Tk()
window.title("ROCK PAPER SCISSORS - ESPORTS EDITION")
window.geometry("450x600")
window.configure(bg="#121212")  # พื้นหลังสีดำเข้มแบบเกมมิ่ง

# หัวข้อหลักสไตล์นีออน
lbl_title = tk.Label(window, text="ROCK PAPER SCISSORS", font=("Impact", 24), bg="#121212", fg="#00ffff")
lbl_title.pack(pady=15)

lbl_subtitle = tk.Label(window, text="🏆 MATCH 2 IN 3 🏆", font=("Helvetica", 10, "bold"), bg="#121212", fg="#ff007f")
lbl_subtitle.pack()

# เฟรมกระดานคะแนนและการเลือก (แบ่งซ้าย-ขวา)
frame_board = tk.Frame(window, bg="#1a1a1a", bd=2, relief="groove")
frame_board.pack(pady=20, padx=20, fill="x")

# ฝั่งผู้เล่น
frame_player = tk.Frame(frame_board, bg="#1a1a1a")
frame_player.grid(row=0, column=0, padx=30, pady=15)
tk.Label(frame_player, text="YOU (PLAYER)", font=("Helvetica", 11, "bold"), bg="#1a1a1a", fg="#00ff66").pack()
lbl_player_pick = tk.Label(frame_player, text="❓\nรอเลือก...", font=("Helvetica", 16), bg="#1a1a1a", fg="#ffffff")
lbl_player_pick.pack(pady=10)

# คะแนนตรงกลาง
frame_score = tk.Frame(frame_board, bg="#1a1a1a")
frame_score.grid(row=0, column=1, padx=10)
tk.Label(frame_score, text="SCORE", font=("Helvetica", 9, "bold"), bg="#1a1a1a", fg="#888888").pack()
lbl_score = tk.Label(frame_score, text="0   VS   0", font=("Impact", 24), bg="#1a1a1a", fg="#ffffff")
lbl_score.pack()

# ฝั่งบอต
frame_bot = tk.Frame(frame_board, bg="#1a1a1a")
frame_bot.grid(row=0, column=2, padx=30, pady=15)
tk.Label(frame_bot, text="BOT (COM)", font=("Helvetica", 11, "bold"), bg="#1a1a1a", fg="#ff3333").pack()
lbl_bot_pick = tk.Label(frame_bot, text="❓\nรอเลือก...", font=("Helvetica", 16), bg="#1a1a1a", fg="#ffffff")
lbl_bot_pick.pack(pady=10)

# กล่องแสดงผลแพ้ชนะในรอบนั้น ๆ (สไตล์แถบสถานะเกม)
lbl_result = tk.Label(window, text="ใครได้ 2 คะแนนก่อน ชนะเลิศ!", font=("Helvetica", 12, "bold"), bg="#1f1f1f", fg="#00ffff", width=38, height=2, bd=1, relief="solid")
lbl_result.pack(pady=15)

# ข้อความแนะนำ
tk.Label(window, text="CHOOSE YOUR WEAPON", font=("Helvetica", 10, "bold"), bg="#121212", fg="#888888").pack(pady=5)

# เฟรมสำหรับจัดวางปุ่มกดขนาดใหญ่
frame_buttons = tk.Frame(window, bg="#121212")
frame_buttons.pack(pady=10)

# ตกแต่งปุ่มกดให้ใหญ่และมีสีสันแบบปุ่มกดเกมตู้ (Arcade)
btn_rock = tk.Button(frame_buttons, text="✊\nค้อน", font=("Helvetica", 14, "bold"), width=7, height=2, bg="#ffc107", fg="black", activebackground="#ffdb66", cursor="hand2", command=lambda: play("ค้อน"))
btn_rock.grid(row=0, column=0, padx=10)

btn_paper = tk.Button(frame_buttons, text="✋\nกระดาษ", font=("Helvetica", 14, "bold"), width=7, height=2, bg="#28a745", fg="white", activebackground="#4cd16b", cursor="hand2", command=lambda: play("กระดาษ"))
btn_paper.grid(row=0, column=1, padx=10)

btn_scissors = tk.Button(frame_buttons, text="✌️\nกรรไกร", font=("Helvetica", 14, "bold"), width=7, height=2, bg="#dc3545", fg="white", activebackground="#ff6675", cursor="hand2", command=lambda: play("กรรไกร"))
btn_scissors.grid(row=0, column=2, padx=10)

# ปุ่มเริ่มเกมใหม่แบบมินิมอลด้านล่าง
btn_reset = tk.Button(window, text="🔄 RESET MATCH", font=("Helvetica", 10, "bold"), bg="#333333", fg="#aaaaaa", activebackground="#444444", activeforeground="#ffffff", bd=0, padx=15, pady=5, cursor="hand2", command=reset_game)
btn_reset.pack(pady=25)

# รันหน้าต่างโปรแกรม
window.mainloop()