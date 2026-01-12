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

        commands = [
            ['localsend', *file_paths],
            ['flatpak', 'run', 'org.localsend.localsend_app', *file_paths]
        ]

        success = False
        for cmd in commands:
            try:
                subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                success = True
                break 
            except FileNotFoundError:
                continue
            except Exception:
                continue

        if not success:
            subprocess.run(['notify-send', 'Помилка LocalSend', 'Не вдалося знайти встановлений LocalSend'])

    def get_file_items(self, *args):
        files = args[-1]
        if not files:
            return        

        count = len(files)
        if count > 1:
            label = f"Надіслати {count} файлів через LocalSend"
        else:
            label = "Надіслати через LocalSend"
        
        item = Nautilus.MenuItem(
            name="LocalSend::SendFiles",
            label=label,
            tip="Надіслати вибрані об'єкти через LocalSend"
        )
        item.connect("activate", self._send_to_localsend, files)
        return [item]

    def get_background_items(self, *args):
        file = args[-1]
        item = Nautilus.MenuItem(
            name="LocalSend::SendCurrentDir",
            label="Надіслати все з цієї теки через LocalSend",
            tip="Надіслати поточну директорію через LocalSend"
        )
        item.connect("activate", self._send_to_localsend, [file])
        return [item]
