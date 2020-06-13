import urllib.request
import bcolors
import sys, argparse

def banner():
    print("""

            ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗░░░░░░░█████╗░██████╗░░░░░░░███╗░░██╗░█████╗░████████╗
            ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║░░░░░░██╔══██╗██╔══██╗░░░░░░████╗░██║██╔══██╗╚══██╔══╝
            ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║█████╗██║░░██║██████╔╝█████╗██╔██╗██║██║░░██║░░░██║░░░
            ██║░░██║██║░░██║░░████╔═████║░██║╚████║╚════╝██║░░██║██╔══██╗╚════╝██║╚████║██║░░██║░░░██║░░░
            ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║░░░░░░╚█████╔╝██║░░██║░░░░░░██║░╚███║╚█████╔╝░░░██║░░░
            ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝░░░░░░░╚════╝░╚═╝░░╚═╝░░░░░░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░
                                                                                               Code by NG          
          """)
if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] == '-u'):
        try:
            input_url = sys.argv[2]

            parser = argparse.ArgumentParser()
            parser.add_argument("-u", required=True)
            args = parser.parse_args()

            print(bcolors.BITALIC + "Checking for Website is up or down")

            try:
                response_code = urllib.request.urlopen(input_url).getcode()
                if response_code == 200:
                    print(bcolors.OKMSG + "Its Just You ! " + input_url + " UP for everyone else")
            except:
                print(bcolors.OKMSG + "Its not just you ! " + input_url + " is down for everyone else")
        except:
            print(
                'Please enter python downornot.py -u < URL with (http:// or https://s) which you want to check is Up or Down >')

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: hidden.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-u URL,   --URL valid URL')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from -u or -h, with a valid URL')
