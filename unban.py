import smtplib
import getpass
import time
import re
import os
import random
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, Style, init

init(autoreset=True)

# ===== Tool login =====
tool_username = "admin"
tool_password = "admins"

# ===== Your personal Gmail credentials =====
your_email = "anonymoushosts3@gmail.com"
your_app_password = "Kibet44$$"

# ===== WhatsApp Business API credentials =====
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"
PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID_HERE"

# ===== WhatsApp support emails =====
support_emails = [
    "support@support.whatsapp.com",
    "web@support.whatsapp.com",
    "help@support.whatsapp.com",
    "appeals@support.whatsapp.com",
    "review@support.whatsapp.com"
] * 10

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def check_whatsapp_number(phone):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/contacts"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "blocking": "wait",
        "contacts": [phone],
        "force_check": True
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        for contact in data.get("contacts", []):
            status = contact.get("status")
            wa_id = contact.get("wa_id", "N/A")
            print(Fore.GREEN + f"\n✅ Number: {wa_id} is {status.upper()} on WhatsApp.\n")
        if not data.get("contacts"):
            print(Fore.RED + "\n❌ Number is not registered on WhatsApp.\n")
    else:
        print(Fore.RED + "\n⚠️ Failed to check number.\n")
        print(response.text)

# ===== Login screen =====
while True:
    banner_color = random.choice([Fore.GREEN, Fore.CYAN, Fore.MAGENTA])
    print(banner_color + "📲 Welcome to WhatsApp Unban Tool")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    username = input("👤 Enter Username: ")
    password = getpass.getpass("🔒 Enter Password: ")

    if username == tool_username and password == tool_password:
        print(Fore.GREEN + "\n✅ Login successful!")

        # Banner art
        print(banner_color + '''
⠀⠀⠀    ⣠⣶⣶⣶⣶
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣧
⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣠⣴⣶⣤⡀⠀
⠀⠀⠀⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦⠀⠀⠀⠀⣸⣿⣿⣿⣿⣷⠀
⠀⠀⠀⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀⠀⢀⣿⣿⣿⣿⡿⠋⠀
⠀⠀⠀⠀⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀
⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇⠀⠀⠀⠉⠛⣽⣿⣇⣀⣀⣀⠀
⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇⠀⠀⠀⠀⠀⠻⠿⠿⠛⠛⠛
''')
        typewriter(Fore.YELLOW + "This tool was made by Teddy Tech alone.\n", delay=0.06)
        break
    else:
        print(Fore.RED + "\n❌ Incorrect credentials, try again...")
        time.sleep(2)

# ===== Main Menu =====
while True:
    clear()
    menu_color = random.choice([Fore.BLUE, Fore.YELLOW, Fore.CYAN])
    print(menu_color + "🛠️ WhatsApp Unban Tool - Main Menu")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(menu_color + " [1] 📩 Unban Temporary")
    print(menu_color + " [2] 🚫 Unban Permanent")
    print(menu_color + " [3] 🔍 Check WhatsApp Number Status")
    print(menu_color + " [0] ❌ Exit")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    choice = input(Fore.WHITE + "\n📥 Select an option: ").strip()

    if choice in ["1", "2"]:
        unban_type = "Temporary" if choice == "1" else "Permanent"
        clear()
        print(menu_color + f"🔄 Unban {unban_type} Selected\n")

        while True:
            phone = input("📞 Enter WhatsApp number with country code (e.g., +254799963583): ").strip()
            if re.match(r"^\+\d{10,15}$", phone):
                break
            else:
                print(Fore.RED + "❌ Invalid format! Only numbers allowed with country code starting with +.")
                time.sleep(1)

        print(f"\n📝 Sending {unban_type} unban request for {phone}...")
        time.sleep(1)

        if unban_type == "Temporary":
            subject = "Humble Request for Temporary Lift of WhatsApp Account Ban"
            body = f"""

Dear WhatsApp Appeals Team,

I hope this message finds you well.

I am writing with deep respect and concern regarding the ban placed on my WhatsApp account associated with the phone number {phone}. I understand the importance of maintaining a safe and positive community, and I fully support your efforts.

However, I kindly believe this ban may have resulted from a misunderstanding or an unintentional error. WhatsApp is essential for my daily communication with family, friends, and work, and I am sincerely committed to following all community guidelines moving forward.

Phone Number: {phone}
WhatsApp Version: 2.25.21.82

I humbly request that you consider temporarily lifting the ban on my account to allow me the opportunity to demonstrate responsible use and compliance with your policies. If any issues remain, I would be grateful for guidance so I can fully address them.

Thank you very much for your understanding and consideration. I deeply appreciate your time and support.

With sincere gratitude.
"""
        else:
            subject = "Humble Request for Reconsideration of Permanent Ban on My WhatsApp Account"
            body = f"""
            
Dear WhatsApp Appeals Team,

I hope you are doing well.

I am reaching out with a heavy heart regarding the permanent ban on my WhatsApp account linked to the phone number {phone}. I was deeply saddened to learn about this restriction and genuinely believe there might have been a misunderstanding or an unintentional mistake on my part.

Phone Number: {phone}
WhatsApp Version: 2.25.21.82

WhatsApp is incredibly important to me—it connects me with my loved ones, friends, and colleagues daily. I truly respect the rules and community guidelines set forth by your team, and if I have unknowingly violated any, I sincerely apologize. Please know that it was never my intention to cause any harm or disruption.

I humbly ask for your kindness and understanding in reviewing my case. If given the chance, I commit to strictly adhering to all policies moving forward and ensuring that my usage aligns fully with your standards.

Thank you very much for your time, patience, and consideration. I would be extremely grateful for the opportunity to regain access to my account.

With sincere gratitude.
"""

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(your_email, your_app_password)

            for i, email in enumerate(support_emails, 1):
                msg = MIMEMultipart()
                msg['From'] = your_email
                msg['To'] = email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                server.send_message(msg)
                print(Fore.GREEN + f"   [{i}/50] Sent to {email}")
                time.sleep(0.2)

            server.quit()
            print(Fore.GREEN + f"\n🎉 SUCCESS: {unban_type} unban request submitted.")
            print("📡 Stay active while WhatsApp reviews your request.\n")

        except Exception as e:
            print(Fore.RED + "\n❌ Failed to send email:", e)
        input(Fore.CYAN + "\n🔁 Press Enter to return to menu...")

    elif choice == "3":
        clear()
        print(menu_color + "🔍 Check WhatsApp Number Status\n")
        phone = input("📞 Enter the WhatsApp number (e.g., +254799963583): ")
        print("\n⏳ Checking number...")
        time.sleep(1.5)
        check_whatsapp_number(phone)
        input(Fore.CYAN + "\n🔁 Press Enter to return to menu...")

    elif choice == "0":
        print(Fore.YELLOW + "\n👋 Goodbye!")
        break

    else:
        print(Fore.RED + "\n❌ Invalid choice.")
        time.sleep(2)
