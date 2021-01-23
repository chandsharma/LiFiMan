import pexpect
import re
import eel

eel.init("web")

PROMPT=['# ', '>>> ', '> ', '\$ ']
@eel.expose
def escape_ansi(line):
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)
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
    return re[0]
@eel.expose
def wifi_status():
    term = pexpect.spawn('nmcli r wifi', encoding='utf-8')
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'enabled','disabled'])
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
    term = pexpect.spawn('nmcli -f in-use,bssid,ssid,mode,chan,rate,signal,bars,security d wifi list', encoding='utf-8',timeout=5)
    term.setwinsize(300,400)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF])
    p=term.before
    r = escape_ansi(line = p)
    re = []
    for dev in r.splitlines()[2:len(r.splitlines())-2]:
        if dev.split()[0] == '*': # AP SPEED ENCRYPRION SIGNAL ok mei ja ra tu kr le
            ssid = dev.split()[1]
            rhalf = dev.split(ssid)[1]
            name = rhalf[:len(rhalf)-rhalf[::-1].index('arfnI')-5]
            re.append(name+','+dev.split()[len(dev.split())-5:len(dev.split())-3][0]+' '+dev.split()[len(dev.split())-5:len(dev.split())-3][1]+','+dev.split()[len(dev.split())-1:][0]+','+dev.split()[len(dev.split())-3:len(dev.split())-2][0]+','+ssid+','+"yes")
        else:
            ssid = dev.split()[0]
            rhalf = dev.split(ssid)[1]
            name = rhalf[:len(rhalf)-rhalf[::-1].index('arfnI')-5]
            re.append(name+','+dev.split()[len(dev.split())-5:len(dev.split())-3][0]+' '+dev.split()[len(dev.split())-5:len(dev.split())-3][1]+','+dev.split()[len(dev.split())-1:][0]+','+dev.split()[len(dev.split())-3:len(dev.split())-2][0]+','+ssid+','+"no")

    return re
#disconnect network
@eel.expose
def disconnect(interface):
    command = 'nmcli device disconnect '+str(interface)
    term = pexpect.spawn(command, encoding='utf-8',timeout=5)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'successfully','failed'])
    p=term.before
    return ret

#autoconnect network
@eel.expose
def autoconnect(interface):
    command = 'nmcli device connect '+str(interface)
    term = pexpect.spawn(command, encoding='utf-8',timeout=8)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'successfully','Failed'])
    p=term.before

#set autoconnect ON
@eel.expose
def set_autoconnect():
    term = pexpect.spawn('nmcli device set wlan0 autoconnect on', encoding='utf-8',timeout=8)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF])
    p=term.before
    return ret

#rescan wifi
@eel.expose
def rescan():
    term = pexpect.spawn('nmcli d wifi rescan', encoding='utf-8',timeout=5)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF])
    p=term.before
    return ret

#connect save wifi
@eel.expose
def connect_saved_wifi():
    term = pexpect.spawn('nmcli d connect wlan0', encoding='utf-8',timeout=5)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'successfully','Failed'])
    p=term.before
    return ret

#Connect ti wifi
@eel.expose
def connect_hidden_wifi(ap,password):
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

    term = pexpect.spawn(command, encoding='utf-8',timeout=5)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'successfully','No Network','Secrets were required, but not provided.','No network'])
    p=term.before
    return ret

#Connect to ssid
@eel.expose
def connect_ssid(ap,password):
    if str(password)=="0":
        command = 'nmcli device wifi connect '+str(ap)
    else:
        command = 'nmcli device wifi connect '+str(ap)+' password '+str(password)
    term = pexpect.spawn(command, encoding='utf-8',timeout=5)
    ret = term.expect([pexpect.TIMEOUT,pexpect.EOF,'successfully','No Network','Secrets were required, but not provided.','No network'])
    p=term.before
    return ret

eel.start("home.html", cmdline_args=['--start-fullscreen'])
