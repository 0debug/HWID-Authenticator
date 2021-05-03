import subprocess, requests, time, os

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('your url here')
 
try:
    if hwid in r.text:
        pass
    else:
        print('[ERROR] HWID Not recognized!')
        print(f'HWID: {hwid}') 
        time.sleep(5)
        os._exit()
except:
    print('[ERROR] Failed to connect to the database')
    time.sleep(5) 
    os._exit() 
    
os.system('title HWID Authentication')

print('Welcome')
input()
