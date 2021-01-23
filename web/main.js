function callback(calue){
  document.querySelector(".loader").style.display = "none";
  document.querySelector(".status__header").style.display = "block";
  // console.log(calue);
  document.querySelector(".status.ethernet").style.pointerEvents ="auto";
  document.querySelector(".status.ethernet").style.opacity = 1;
  let ethConfig = calue.split(",");
  // console.log(ethConfig);
  if (ethConfig[1] === "unavailable"){
    // console.log("not available");
    document.getElementById("ethustat").innerHTML = "UNAVAILABLE";
    document.getElementById("ethuname").innerHTML = "NOT CONNECTED";
  }
  else{
    document.getElementById("ethustat").innerHTML = `${ethConfig[1].toUpperCase()}`;
    document.getElementById("ethuname").innerHTML = `${ethConfig[2]}`;
  }
}


function wifiDevices(devices) {
  // console.log(devices)
  document.querySelector(".lfoader").style.display = "none";
  document.querySelector(".lstatus__header").style.display = "block";
  document.getElementsByClassName("lstatus__header")[0].innerHTML = '';
  let id = 'a';
  devices.forEach(index => {
    createCard(index,id);

id = id+1;
  })
}
function createCard(index,id) {

  let mainContainer = document.createElement("div");
  let cour = document.createElement("div");
  let connectOverlay = document.createElement("div");

  let courPreview = document.createElement("div");
  let wifiName = document.createElement("h5");
  let courInfo = document.createElement("div");
  let progContainer = document.createElement("div");
  let prog = document.createElement("div");

  let progText = document.createElement("span");
  let lin = document.createElement("div");
  let intspedd = document.createElement("h4");
  let span = document.createElement("span");
  let encryption = document.createElement("h4");

index = index.split(",");
    mainContainer.classList.add("cour-container");
    cour.classList.add("cour");
    connectOverlay.classList.add("connectOverlay");
    connectOverlay.classList.add(id); //a
    connectOverlay.classList.add(index[4]); //ssid
    connectOverlay.classList.add(index[5]); //yes
    wifiName.classList.add(id);
    courPreview.classList.add("cour-preview");
    courInfo.classList.add("cour-info");
    progContainer.classList.add("prog-container");
    prog.classList.add("prog");
    prog.classList.add(id);
    progText.classList.add("prog-text");
    lin.classList.add("lin");
    intspedd.classList.add("intspedd")

  mainContainer.appendChild(cour);
  cour.appendChild(courPreview);
  cour.appendChild(connectOverlay);
  courPreview.appendChild(wifiName);
  cour.appendChild(courInfo);
  courInfo.appendChild(progContainer);
  progContainer.appendChild(prog);
  progContainer.appendChild(progText);
  courInfo.appendChild(lin);
  lin.appendChild(intspedd);
  lin.appendChild(span);
  lin.appendChild(encryption);
let progStyle = document.createElement("style");
progStyle.innerHTML = `.prog.${id}::after {
	border-radius: 3px;
	background-color: #4EAB19;
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	height: 5px;
	width: ${index[3]}%;
}`;
document.head.appendChild(progStyle);
wifiName.innerHTML = index[0];
intspedd.innerHTML = index[1];
if(index[2] == "--"){
  encryption.innerHTML = "Open";
  connectOverlay.classList.add("Open");
}
else {
  encryption.innerHTML = index[2];
  connectOverlay.classList.add(index[2]);
}
progText.innerHTML = index[3];
document.getElementsByClassName("lstatus__header")[0].appendChild(mainContainer);

connectOverlay.addEventListener("click", function(event) {
  document.getElementById("netnamenet").style.display = "none";
//console.log(event);
// console.log(event.srcElement.className.split(" ")[2]);
// console.log(event.srcElement.className.split(" ")[3]);
if(event.srcElement.className.split(" ")[3] === "yes")
{
  // console.log("already connected");
  feedback("Already Connected");
}
else{
if(event.srcElement.className.split(" ")[4] === "Open"){
  // console.log("open network");
  feedback("Connecting");
  eel.connect_ssid(event.srcElement.className.split(" ")[2],0)(conres);
}
else{

  document.querySelector(".wrapper").style.display="none";
  document.querySelector(".newover").style.display="block";
  document.getElementById("user").innerHTML = event.srcElement.className.split(" ")[2];
  document.getElementById("user").value = event.srcElement.className.split(" ")[2];
}
}
})
}
function conres(v){
  // console.log(v);
  if(v === 2){
    feedback("Connected Successfully")
  }
  else if(v === 3 || v === 5 ){
    feedback("Network Error");
  }
  else if (v === 4){
    feedback("Wrong Password");
  }
  else{
    feedback("PLEASE REFRESH");
  }
  eel.wifi_state()(calling);
manageContent("WI-FI");
eel.list_available_wifi()(wifiDevices);
}
function connectssid(){
  document.querySelector(".wrapper").style.display="flex";
  document.querySelector(".newover").style.display="none";
  let ssid = document.getElementById("user").value;
  let pass = document.getElementById("pass").value;
  // console.log(ssid,pass);
  eel.connect_ssid(ssid,pass)(conres);
  document.getElementById("user").value = '';
  document.getElementById("pass").value = '';
  document.getElementById("user").innerHTML = '';
  document.getElementById("pass").innerHTML = '';
}

function closepass(){
  document.querySelector(".wrapper").style.display="flex";
  document.querySelector(".newover").style.display="none";
}


function dummy(varu){
  //
}
function calling(value){

  // console.log(value.split(',')[1],"happy");
  document.querySelector(".shtn").style.display = "none";
  document.querySelector(".status.wifi .status__header").style.display = "flex";
  if(value.split(',')[1] === "disconnected" ){
    document.querySelector(".shtn").style.display = "block";
  }
  else if(value.split(',')[1] === "unavailable" ){
      document.querySelector(".status.wifi .status__header").style.display = "none";
    eel.autoconnect('wlan0')(dummy);
    eel.wifi_state()(calling);
    document.getElementById("winame").innerHTML = "NO Wi-Fi NETWORK AVAILABLE";
  }
  else if(value.split(',')[1] === "connecting" ){
    document.querySelector(".status.wifi .status__header").style.display = "block";
    //
    //feedback("CONNECTING");
    document.querySelector(".status__header").style.display = "block";
  document.querySelector(".status.wifi").style.pointerEvents ="auto";
  document.querySelector(".status.wifi").style.opacity = 1;
  let wifiConfig = value.split(",");
  // console.log(wifiConfig);
  document.getElementById("wistat").innerHTML = ` ${wifiConfig[1].toUpperCase()}`;
  document.getElementById("winame").innerHTML = ` ${wifiConfig[2]}`;
  // console.log(wifiConfig[2]);
  eel.wifi_state()(calling);
  }
  else{
    feedback("CONNECTED");
    document.querySelector(".status.wifi .status__header").style.display = "block";
  document.querySelector(".btn").style.display = "block";
    document.querySelector(".status__header").style.display = "block";
  document.querySelector(".status.wifi").style.pointerEvents ="auto";
  document.querySelector(".status.wifi").style.opacity = 1;
  let wifiConfig = value.split(",");
  // console.log(wifiConfig);
  document.getElementById("wistat").innerHTML = ` ${wifiConfig[1].toUpperCase()}`;
  document.getElementById("winame").innerHTML = ` ${wifiConfig[2]}`;
  // console.log(wifiConfig[2]);
}

}
function autoconnect(){
  document.querySelector(".status__header").style.display = "none";
  document.querySelector(".lfoader").style.display = "block";
  // console.log("autoconnect");
  eel.autoconnect('wlan0')(dummy);
  eel.wifi_state()(calling);
  document.querySelector(".lfoader").style.display = "none";

}
function dish (va){
  if (va === 3){
    feedback('FAILED TO DISCONNECT');
  }
  else if(va === 2){
    feedback('DISCONNECTED SUCCESSFULLY');
    document.querySelector(".btn").style.display = "none";
    eel.wifi_state()(calling);
  }
  else {
    feedback('PLEASE REFRESH');
    document.querySelector(".btn").style.display = "none";
    eel.wifi_state()(calling);
  }
}
function disconnect(){
  document.querySelector(".status__header").style.display = "none";
  document.querySelector(".loader").style.display = "block";
  eel.disconnect('wlan0')(dish);
    eel.wifi_state()(calling);
}
function wufu(vi){
  eel.wifi_status()(wifistatuscall);
  eel.wifi_state()(calling);

}
function wifion(){
  eel.wifi_on()(wufu);
  manageContent("WI-FI");
  document.querySelector(".status__header").style.display = "block";
}
function wifistatuscall(value){
  // console.log(value);

  //value = 3;
  document.querySelector(".btn").style.display = "none";
  document.querySelector(".status__header").style.display = "block";

  if (value == 3){
    manageContent("WI-FI");
    document.querySelector(".btn").style.display = "none";
    document.getElementById("wifiConnect").style.display="auto";
    document.querySelector(".status.wifi .status__header").style.display = "none";
    feedback("NO WIFI CONNECTION");
    document.getElementById("wifiConnect").style.display="block";
  }
  else if (value == 0 ){

      manageContent("WI-FI");
    document.getElementById("wifiConnect").style.display="none";
    document.querySelector(".status__header").style.display = "none";
    document.querySelector(".lfoader").style.display = "block";
    eel.list_available_wifi()(wifiDevices);
    feedback("CONNECTED");


  }
  else{
      manageContent("WI-FI");
    document.getElementById("wifiConnect").style.display="none";
    feedback("CONNECTED");
    document.querySelector(".status__header").style.display = "none";
    document.querySelector(".lfoader").style.display = "block";
    eel.list_available_wifi()(wifiDevices);
  }
}
eel.ethernet_state()(callback);
eel.wifi_state()(calling);
const menu = ["WI-FI", "ETHERNET"];

function feedback(text) {
  document.querySelector("#feedback").classList.add("feedbackAnim");
  setTimeout(() => {
    document.querySelector("#feedback").classList.remove("feedbackAnim")
  }, 2000);
  document.querySelector("#feedback").innerHTML = text;
}

const manageContent = (option) => {
  // console.log("CLicked");
  if(option === "WI-FI") {
    eel.wifi_state()(calling);
    document.querySelector(".status.ethernet").style.display = "none";
    document.querySelector(".status.wifi").style.display = "flex";
    document.querySelector(".fus").style.borderRadius ="10px 10px 0px 0px";
    document.querySelector(".fus").style.backgroundColor = "rgba(0,0,0,0.4)";
    document.querySelector(".hus").style.borderRadius ="0px";
    document.querySelector(".hus").style.backgroundColor = "rgba(0,0,0,0)";
    document.getElementById('wifiButton').style.fontWeight = "normal";
    document.getElementById('ethernetButton').style.fontWeight = "bold";
    document.getElementById('wifiButton').style.letterSpacing = "5";
    document.getElementById('ethernetButton').style.letterSpacing = "3";
}
else {
  eel.ethernet_state()(callback);
  document.querySelector(".status.ethernet").style.display = "flex";
  document.querySelector(".status.wifi").style.display = "none";
  document.querySelector(".hus").style.borderRadius ="10px 10px 0px 0px";
  document.querySelector(".hus").style.backgroundColor = "rgba(0,0,0,0.4)";
  document.querySelector(".fus").style.borderRadius ="0px";
  document.querySelector(".fus").style.backgroundColor = "rgba(0,0,0,0)";
  document.getElementById('wifiButton').style.fontWeight = "bold";
  document.getElementById('ethernetButton').style.fontWeight = "normal";
  document.getElementById('wifiButton').style.letterSpacing = "3";
  document.getElementById('ethernetButton').style.letterSpacing = "5";
}
}
document.getElementById("wifiButton").addEventListener("click", function() {
  document.querySelector(".lstatus__header").style.display = "none";
  document.querySelector(".status__header").style.display = "none";
  document.querySelector(".loader").style.display = "block";
  let devicesList = document.getElementById("devices");
  if (devicesList) {
   while (devicesList.firstChild) {
     devicesList.removeChild(devicesList.firstChild);
   }
 }

  eel.wifi_status()(wifistatuscall);
});
document.getElementById("wifiConnect").addEventListener("click",function(){
  wifion();
});
document.getElementById("ethernetButton").addEventListener("click", function() {
  document.querySelector(".status__header").style.display = "none";
  document.querySelector(".loader").style.display = "block";
  manageContent("ETHERNET");
});

document.getElementById("refbut").addEventListener("click",function(){
  // console.log("refresh");
  window.location.href="home.html";
});

function wind(){
  // console.log("working");
}
