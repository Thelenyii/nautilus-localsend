# Nautilus LocalSend Extension

Integration for sending files with **LocalSend** directly from the Nautilus context menu.

Інтеграція для надсилання файлів за допомогою **LocalSend** безпосередньо з контекстного меню Nautilus.

![Screenshot](https://github.com/user-attachments/assets/b73b3a9c-b4f9-4a81-bfc9-20af5e117aea)

---

## 🛠 Installation / Встановлення

### 1. Install dependencies / Встановлення залежностей

**Arch Linux / Manjaro:**
```bash
sudo pacman -S python-nautilus
```

### 2. Install the plugin / Встановлення плагіна

Run the following commands to install the extension for your user:
```bash
mkdir -p ~/.local/share/nautilus-python/extensions/
git clone [https://github.com/Thelenyii/nautilus-localsend.git](https://github.com/Thelenyii/nautilus-localsend.git)
cd nautilus-localsend
cp nautilus-localsend.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

#### 🚀 Usage / Використання

  1. Open Nautilus.
  2. Right-click on any file or folder (or the background).
  3.  Select "Надіслати через LocalSend".
  4.  Відкрийте Nautilus.
  5.  Натисніть правою кнопкою миші на файл, папку або пусте місце.
  6.  Оберіть "Надіслати через LocalSend".
