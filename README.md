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

## Встановлення плагіна
```
git clone https://github.com/Thelenyii/nautilus-localsend.git
cd nautilus-localsend
mv nautilus-localsend.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```
