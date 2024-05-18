import shutil
import os
import sys

if not sys.executable.endswith("pythonw.exe"):
    raise OSError("Yönetici olarak çalıştırmalısın.")

# Hosts yedekler.
bak_file = 'C:\\Windows\\System32\\drivers\\etc\\hosts.bak'
shutil.copyfile('C:\\Windows\\System32\\drivers\\etc\\hosts', bak_file)

# Boş hosts oluşturur.
with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'w') as file:
    file.write('# Varsayılan hosts dosyası\n')
    file.write('# Bu dosya otomatik olarak sıfırlandı\n')

print('Hosts dosyası sıfırlandı.')