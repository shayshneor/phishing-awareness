import time
import os
import platform
import webbrowser

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def prank():
    clear()
    print("Initializing...")
    time.sleep(1.5)
    print("Downloading payload...")
    time.sleep(2)
    print("Bypassing antivirus...")
    time.sleep(1.5)
    print("Injecting backdoor...")
    time.sleep(2)
    clear()
    print("\033[91m[!] אתה קורבן לפישינג!\033[0m 😂")
    print("""
    אל דאגה, הכל בצחוק. הקובץ הזה הוא הדגמה בלבד.
    
    אם הרצת את הקובץ בלי לחשוב פעמיים,
    עכשיו אתה יודע למה לא להפעיל קבצים ממקור לא מזוהה 😉

    📚 תלמד להבא לבדוק לפני שאתה לוחץ על משהו!

    """)
    # פותח GIF עם meme
    gif_path = os.path.join("assets", "gotcha.gif")
    webbrowser.open("https://media.giphy.com/media/3ohzdYJK1wAdPWVk88/giphy.gif")  # לינק הומריסטי
    time.sleep(5)

if __name__ == "__main__":
    prank()
