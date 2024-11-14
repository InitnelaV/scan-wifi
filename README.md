Specific for Windows, this script include the netsh wlan show 

<img width="464" alt="image" src="https://github.com/user-attachments/assets/8ed04234-209e-4d33-bc71-5841c8f658af">

Equals to this command directly in cmd
<img width="351" alt="image" src="https://github.com/user-attachments/assets/39b4cb16-26f3-4498-9d5d-bbd8b012cddf">

Note: You may change the decode "cp850" in "utf-8" : cp850 is the decode use for the french version of Windows
networks_output = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True).decode("utf-8")

The result :
<img width="880" alt="image" src="https://github.com/user-attachments/assets/0466e986-4657-46af-96b2-6a222c34a0b3">

Enjoy Yourself ;)
