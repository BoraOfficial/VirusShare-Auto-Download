import os
if os.name != "nt":
    exit()
import time

# PUT THIS SCRIPT IN WHERE YOU WANT THE FILES TO BE!!!!
stageone = 0


def second():	
  stagetwo = 10
  while stagetwo < 100:
    print(f'Requested to download the file VirusShare_000{stagetwo}.md5')
    os.system(f'powershell.exe -Command Invoke-WebRequest https://virusshare.com/hashfiles/VirusShare_000{stagetwo}.md5 -OutFile hash000{stagetwo}.txt')
    time.sleep(1)
    stagetwo += 1
    if stagetwo == 99:
      print(f'Requested to download the file VirusShare_00099.md5')
      third()
      break

def third():
  stagethree = 100
  while stagethree < 394:
    print(f'Requested to download the file VirusShare_00{stagethree}.md5')
    os.system(f'powershell.exe -Command "Invoke-WebRequest https://virusshare.com/hashfiles/VirusShare_00{stagethree}.md5 -OutFile hash00{stagethree}.txt')
    time.sleep(1)
    stagethree += 1
    if stagethree == 393:
      print(f'Requested to download the file VirusShare_00393.md5')
      os.system(f'powershell.exe -Command Invoke-WebRequest https://virusshare.com/hashfiles/VirusShare_00393.md5 -OutFile hash00393.txt')
      print(f'Final file is getting downloaded\nRequested to download the file VirusShare_00394.md5')
      os.system(f'powershell.exe -Command "Invoke-WebRequest https://virusshare.com/hashfiles/VirusShare_00394.md5 -OutFile hash00394.txt')
      print("Downloaded all of the files have a nice day!")
      time.sleep(10)
      break

while stageone < 10:
  print(f'Requested to download the file VirusShare_0000{stageone}.md5'),
  os.system(f'powershell.exe -Command "Invoke-WebRequest https://virusshare.com/hashfiles/VirusShare_0000{stageone}.md5 -OutFile hash0000{stageone}.txt')
  # Comment time.sleep(1) if you want to get the job done faster(ALERT: if your computer is not very fast do not comment it! you might get a BSOD!!!!)
  time.sleep(1)
  stageone += 1
  if stageone == 9:
    print(f'Requested to download the file VirusShare_00009.md5')
    os.system(f'powershell.exe -Command Invoke-WebRequest https://virusshare.com/hashfiles/VirusShare_0000{stageone}.md5 -OutFile hash00009.txt')
    second()
    break




    
