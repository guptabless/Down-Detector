import urllib.request

print("-----------------------------------------------")
print("Down Detector")
print("Code By : NG")
print("Usage: python downornot.py and then provide the URL")
print("Please provide the full URL including http:// or https://")
print("-----------------------------------------------")

a = input("Please Enter the URL of the Website to Check\n")
try:
    response_code = urllib.request.urlopen(a).getcode()
    if response_code == 200:
        print("Its Just You ! "+a+ " UP for everyone else")
except:
    print("Its not just you ! "+a+ " is down for everyone else")
