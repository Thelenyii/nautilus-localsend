import os
import subprocess
from urllib.parse import unquote, urlparse
import gi

try:
    gi.require_version('Nautilus', '4.0')
except ValueError:
    try:
        gi.require_version('Nautilus', '3.0')
    except ValueError:
        pass

from gi.repository import Nautilus, GObject

class LocalSendExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()

    def _send_to_localsend(self, menu, files):
        file_paths = []
        for file in files:
            path = unquote(urlparse(file.get_uri()).path)
            if path.startswith('/'):
                file_paths.append(path)

        # Відредагуйте команду для запуску LocalSend, якщо у вас вона відрізняється
        command = [
            ['localsend', *file_paths],
        ]

        success = False
        for cmd in command:
            try:
                # Перевіряємо, чи встановлено LocalSend
                subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                success = True
                break # Якщо запустилося, зупиняємо цикл
            except FileNotFoundError:
                continue
            except Exception:
                continue

        if not success:
            # Виводимо сповіщення в системі, якщо команда не спрацювала
            subprocess.run(['notify-send', 'Помилка LocalSend', 'Не вдалося знайти встановлений LocalSend'])

    def get_file_items(self, *args):
        files = args[-1]
        if not files:
            return
        
        item = Nautilus.MenuItem(
            name="LocalSend::SendFiles",
            label="Надіслати через LocalSend",
            tip="Надіслати вибрані об'єкти через LocalSend"
        )
        item.connect("activate", self._send_to_localsend, files)
        return [item]

    def get_background_items(self, *args):
        file = args[-1]
        item = Nautilus.MenuItem(
            name="LocalSend::SendCurrentDir",
            label="Надіслати все через LocalSend",
            tip="Надіслати поточну директорію через LocalSend"
        )
        item.connect("activate", self._send_to_localsend, [file])
        return [item]
