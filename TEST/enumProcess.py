import wmi
c = wmi.WMI ()
procDofus = []

for process in c.Win32_Process ():
  if process.Name == 'Dofus.exe':
    procDofus.append(process.ProcessId)
    procDofus.append(process.Name)

print procDofus