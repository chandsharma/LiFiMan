# **LIFIMAN**
### **LI**nux wi**FI MAN**ager
LIFIMAN is **Linux based Wi-Fi and Network Manager**. It has a **cool GUI** for User Friendly Access. It uses **Terminal Commands in Backend** to Manage Networks. It Allows you to manage and connect to network **WITHOUT CAPTIVE PORTAL**
Works on **Raspberry Pi**

## FEATURES
- Wired and Wireless Network Manager
- Wi-Fi Signal Indicator
- Wi-Fi Bandwidth (Speed) Display
- Wi-Fi Encryption Display
- Airplane Mode / Wi-Fi OFF Handling
- Auto-Connect to saved Networks
- DisConnect from current Network Button
- No Captive Portal
- Network Permission and Access remains UNCHANGED
- No ROOT (sudo) required
- PYTHON backend
- Works on Raspberry Pi

## USER INTERFACE
### ETHERNET / WIRED CONNECTION and Wi-Fi / WIRELESS CONNECTION MENU
 <p float="left">
<img src="https://github.com/chandsharma/LiFiMan/blob/main/Readme_resources/ethernet_menu.png" width="200px" height="300px">
<img src="https://github.com/chandsharma/LiFiMan/blob/main/Readme_resources/wifi_off_airplanemode.png" width="200px" height="300px">
  </p>
  
#### CONNECTED Wi-Fi / AVAILABLE NETWORKS / PASSWORD ENTRY FOR ENCRYPTED NETWORKS
  <p float="left">
  <img src="https://github.com/chandsharma/LiFiMan/blob/main/Readme_resources/wifi_main_connected.png" width="200px" height="300px">
  <img src="https://github.com/chandsharma/LiFiMan/blob/main/Readme_resources/signal_indicator.png" width="200px" height="300px">
  <img src="https://github.com/chandsharma/LiFiMan/blob/main/Readme_resources/encryption_password.png" width="200px" height="300px">
  </p>
  
## INSTALLATION AND REQUIREMENTS
Uses `nmcli` terminal tool. *If your system do not have `nmcli` pre-installed follow [this gist](https://gist.github.com/jjsanderson/ab2407ab5fd07feb2bc5e681b14a537a) to install.*

Type `nmcli d wifi list` in terminal to check if it is installed. *Note: If wifi network is available in range and you can't find any wifi name on terminal screen. Follow [this gist](https://gist.github.com/jjsanderson/ab2407ab5fd07feb2bc5e681b14a537a) to setup.* Functionalities remains unchainged for a common user.
- Clone this Repo
- `pip install eel` Refrence at [EEL PyPi Page](https://pypi.org/project/Eel/#:~:text=Eel%20is%20a%20little%20Python,from%20Javascript%2C%20and%20vice%20versa.)
- [Python3](https://www.python.org/) Required
- `pip install pexpect`
- `pip install re`

## RUN
`python3 lifiman.py`

## DEVs
[@chandsharma](https://github.com/chandsharma)
[@TheLazarus](https://github.com/TheLazarus)

## Contribution
Project is open for contribution. Any type of contribution is welcome.
*TO MAKE IT COOL / ADD MORE FEATURES / CONTRIBUTE / REMOVE BUGS FEEL FREE TO MAKE A PULL REQUEST :)*
