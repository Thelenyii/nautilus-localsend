# Nautilus LocalSend Extension

Integration for sending files with **LocalSend** directly from the Nautilus context menu.

Інтеграція для надсилання файлів за допомогою **LocalSend** безпосередньо з контекстного меню Nautilus.

![Screenshot](https://github.com/user-attachments/assets/b73b3a9c-b4f9-4a81-bfc9-20af5e117aea)

---

## 🛠 Installation / Встановлення

### 1. Install dependencies / Встановлення залежностей

**Arch Linux / Manjaro:**
```sudo pacman -S python-nautilus```

**Ubuntu / Debian / Linux Mint:**
```sudo apt install python3-nautilus```

**Fedora:**
```sudo dnf install nautilus-python```

### 2. Install the plugin / Встановлення плагіна

Run the following commands to install the extension for your user:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions/
git clone [https://github.com/raitxrc/nautilus-localsend.git](https://github.com/raitxrc/nautilus-localsend.git)
cd nautilus-localsend
cp nautilus-localsend.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

---

### 🚀 Usage / Використання
  
  1. Open Nautilus / Відкрийте Nautilus.
  2. Right-click on any file or folder (or the background) / Натисніть правою кнопкою миші на файл, папку або пусте місце.
  3.  Select "Надіслати через LocalSend" / Оберіть "Надіслати через LocalSend".
