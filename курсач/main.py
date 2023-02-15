
import eel
import psutil as psu
from datetime import timedelta
from time import time
from gpiozero import CPUTemperature

@eel.expose
def get_cpu_info():
    info = {
        "Uptime": f"{timedelta(seconds=time()-psu.boot_time())}",
        "CPU in use": f"{psu.cpu_percent(interval=.1)}",
        "Time on CPU": f"{timedelta(seconds=psu.cpu_times().system+psu.cpu_times().user)}",
        "Memory in use": f"{psu.virtual_memory().percent}",
        "Disk free": f"{psu.disk_usage('/').free/(1024**3):,.1f} GB",
    }
    return info

eel.init("web")
eel.start("main.html", size=(620, 620))


