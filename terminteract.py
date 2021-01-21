import pexpect
import re
import eel

eel.init("web")

PROMPT=['# ', '>>> ', '> ', '\$ ']

#Remove escape
@eel.expose
def escape_ansi(line):
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)

# #Device and Connection State
# @eel.expose
# def dev_con_state():
#     term = pexpect.spawn('nmcli d', encoding='utf-8')
#     term.setwinsize(300,400)
#     ret = term.expect([pexpect.TIMEOUT,pexpect.EOF])
#     p=term.before
#     r = escape_ansi(line = p)
#     re = []
#     for dev in r.splitlines()[1:]:
#         # DEVICE TYPE STATE CONNECTION
#         re.append(dev.split()[1]+','+dev.split()[2]+','+dev.split()[3]) #dev.split()[0],
#     return re

@eel.expose
def ethernet_state():
    term = pexpect.spawn('nmcli d', encoding='utf-8')
    term.setwinsize(300,400)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF])
    p=term.before
    r = escape_ansi(line = p)
    re = []
    for dev in r.splitlines()[1:]:
        # DEVICE TYPE STATE CONNECTION
        if dev.split()[1] == 'ethernet':
            re.append(dev.split()[1]+','+dev.split()[2]+','+dev.split(dev.split()[2])[1]) #dev.split()[0],
    return re[0]

@eel.expose
def wifi_state():
    term = pexpect.spawn('nmcli d', encoding='utf-8')
    term.setwinsize(300,400)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF])
    p=term.before
    r = escape_ansi(line = p)
    re = []
    for dev in r.splitlines()[1:]:
        # DEVICE TYPE STATE CONNECTION
        if dev.split()[1] == 'wifi':
            re.append(dev.split()[1]+','+dev.split()[2]+','+dev.split(dev.split()[2])[1])
            #print(re)
    return re[0]

# #Connection State
# @eel.expose
# def con_state(device):
#     term = pexpect.spawn('nmcli d', encoding='utf-8')
#     term.setwinsize(300,400)
#     ret = term.expect([pexpect.TIMEOUT,pexpect.EOF])
#     p=term.before
#     r = escape_ansi(line = p)
#     for dev in r.splitlines()[1:]:
#         if dev.split()[0] == 'wlan0' and device == 'wifi':
#             print(dev.split()[2],dev.split(dev.split()[2])[1])
#             return dev.split()[2],dev.split(dev.split()[2])[1]
#         if dev.split()[0] == 'eth0' and device == 'ethernet':
#             print(dev.split()[2],dev.split(dev.split()[2])[1])
#             return dev.split()[2],dev.split(dev.split()[2])[1]



#wifi device status
@eel.expose
def wifi_status():
    term = pexpect.spawn('nmcli r wifi', encoding='utf-8')
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'enabled','disabled'])
    print(ret)
    return str(ret)

@eel.expose
def wifi_on():
    fir = pexpect.spawn('nmcli r wifi on', encoding='utf-8')
    re = fir.expect([pexpect.TIMEOUT,pexpect.EOF])
    if re == 1:
        return 1
    elif re ==0:
        return -1

#list available wifi networks
@eel.expose
def list_available_wifi():
    term = pexpect.spawn('nmcli d wifi list', encoding='utf-8',timeout=5)
    term.setwinsize(300,400)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF])
    p=term.before
    #print(p.split(),ret)
    #print(escape_ansi(line = p).splitlines()[2].split())
    r = escape_ansi(line = p)
    re = []
    for dev in r.splitlines()[2:len(r.splitlines())-2]:
        # IN-USE BSSID SSID MODE CHAN RATE SIGNAL(SIGNAL 0-100) BARS SECURITY
        # ENCRYPRION TYPE "OPEN" is denote by "--"
        #print(dev)
        if dev.split()[0] == '*': # AP SPEED ENCRYPRION SIGNAL ok mei ja ra tu kr le
            ssid = dev.split()[1]
            rhalf = dev.split(ssid)[1]
            name = rhalf[:len(rhalf)-rhalf[::-1].index('arfnI')-5]
            #print(dev.split()[2:len(dev.split())-7],dev.split()[len(dev.split())-5:len(dev.split())-3],dev.split()[len(dev.split())-1:],dev.split()[len(dev.split())-3:len(dev.split())-2])
            #print(name,dev.split()[len(dev.split())-5:len(dev.split())-3],dev.split()[len(dev.split())-1:],dev.split()[len(dev.split())-3:len(dev.split())-2])
            re.append(name+','+dev.split()[len(dev.split())-5:len(dev.split())-3][0]+' '+dev.split()[len(dev.split())-5:len(dev.split())-3][1]+','+dev.split()[len(dev.split())-1:][0]+','+dev.split()[len(dev.split())-3:len(dev.split())-2][0]+','+ssid+','+"yes")
            #re.append(dev.split()[2:len(dev.split())-7]+','+dev.split()[len(dev.split())-5:len(dev.split())-3]+','+dev.split()[len(dev.split())-1:]+','+dev.split()[len(dev.split())-3:len(dev.split())-2])
        else:
            ssid = dev.split()[0]
            rhalf = dev.split(ssid)[1]
            name = rhalf[:len(rhalf)-rhalf[::-1].index('arfnI')-5]
            #print(dev.split()[1:len(dev.split())-7],dev.split()[len(dev.split())-5:len(dev.split())-3],dev.split()[len(dev.split())-1:],dev.split()[len(dev.split())-3:len(dev.split())-2])
            #print(name,dev.split()[len(dev.split())-5:len(dev.split())-3],dev.split()[len(dev.split())-1:],dev.split()[len(dev.split())-3:len(dev.split())-2])
            re.append(name+','+dev.split()[len(dev.split())-5:len(dev.split())-3][0]+' '+dev.split()[len(dev.split())-5:len(dev.split())-3][1]+','+dev.split()[len(dev.split())-1:][0]+','+dev.split()[len(dev.split())-3:len(dev.split())-2][0]+','+ssid+','+"no")

            #re.append(dev.split()[1:len(dev.split())-7]+','+dev.split()[len(dev.split())-5:len(dev.split())-3]+','+dev.split()[len(dev.split())-1:]+','+dev.split()[len(dev.split())-3:len(dev.split())-2])
        #print(dev.split()[0],dev.split()[1],dev.split()[2:len(dev.split())-7],dev.split()[len(dev.split())-7:len(dev.split())])
    print(re)
    return re
#disconnect network
@eel.expose
def disconnect(interface):
    command = 'nmcli device disconnect '+str(interface)
    term = pexpect.spawn(command, encoding='utf-8',timeout=5)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'successfully','failed'])
    p=term.before
    print(p,ret)
    return ret

#autoconnect network
@eel.expose
def autoconnect(interface):
    command = 'nmcli device connect '+str(interface)
    term = pexpect.spawn(command, encoding='utf-8',timeout=8)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'successfully','Failed'])
    p=term.before
    print(p,ret)

#set autoconnect ON
@eel.expose
def set_autoconnect():
    term = pexpect.spawn('nmcli device set wlan0 autoconnect on', encoding='utf-8',timeout=8)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF])
    p=term.before
    print(p,ret)
    return ret

#rescan wifi
@eel.expose
def rescan():
    term = pexpect.spawn('nmcli d wifi rescan', encoding='utf-8',timeout=5)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF])
    p=term.before
    #print(p,ret)
    return ret

#connect save wifi
@eel.expose
def connect_saved_wifi():
    term = pexpect.spawn('nmcli d connect wlan0', encoding='utf-8',timeout=5)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'successfully','Failed'])
    p=term.before
    print(p,ret)
    return ret

#Connect ti wifi
@eel.expose
def connect_wifi(ap,password):
    if '\\' in str(ap) or '"' in str(ap) or '!' in str(ap) or '&' in str(ap) or '(' in str(ap) or ')' in str(ap):
        ap = str(ap).replace('\\', '\\\\')
        ap = str(ap).replace('"', '\\"')
        ap = str(ap).replace('!', '\!')
        ap = str(ap).replace('\&', '\&')
        ap = str(ap).replace('(', '\(')
        ap = str(ap).replace(')', '\)')
    if ' ' in str(ap):
        ap = str(ap).replace(' ', '\ ')

    if str(password)=="0":
        command = 'nmcli device wifi connect '+str(ap)
    else:
        command = 'nmcli device wifi connect '+str(ap)+' password '+str(password)
    print(command)
    term = pexpect.spawn(command, encoding='utf-8',timeout=5)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'successfully','No Network','Secrets were required, but not provided.','No network'])
    p=term.before
    print(p,ret)
    return ret

#Connect to ssid
@eel.expose
def connect_ssid(ap,password):
    if str(password)=="0":
        command = 'nmcli device wifi connect '+str(ap)
    else:
        command = 'nmcli device wifi connect '+str(ap)+' password '+str(password)
    print(command)
    term = pexpect.spawn(command, encoding='utf-8',timeout=5)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'successfully','No Network','Secrets were required, but not provided.','No network'])
    p=term.before
    print(p,ret)
    return ret
#print(rescan())
#print(dev_con_state())
#wifi_state()
#wifi_status()
###print(wifi_status())
#print(list_available_wifi())
#disconnect('wlan0')
#autoconnect('wlan0')
#set_autoconnect()
#connect_wifi(' - : ; \  /* *:" ? !#  & (() |©','00000000')
#con_state('ethernet')
#connect_saved_wifi()
eel.start("home.html", cmdline_args=['--start-fullscreen'])
#print('infra'[::-1].index('arfni'),'infra'[len('infra')-'infra'[::-1].index('arfni')-5:])
