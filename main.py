import subprocess, requests, time, os

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('YOUR HWID LIST HERE')
 
try:
    if hwid in r.text:
        pass
    else:
        print('[ERROR] Your HWID is not recognized!')
        print(f'HWID: {hwid}') 
        time.sleep(10)
        os._exit()
except:
    print('[ERROR] Failed to fetch HWID')
    time.sleep(10) 
    os._exit() 
    
os.system('title HWID Authenticator')

print('Complete')
input()
