var dir = "stop";
var spd = 40;
const shift = 5;

function keyDownHandle(event) {
    switch (event.key) {
        case 'w':
            dir = "forward";
            break;
        case 's':
            dir = "backward";
            break;
        case 'd':
            dir = "right";
            break;
        case 'a':
            dir = "left";
            break;
        case 'ArrowUp':
            addAndConstrain(shift, 0, 100);
            return;
        case 'ArrowDown':
            addAndConstrain(-shift, 0, 100);
            return;
    }
    sendDirection();
}

function keyUpHandle(event) {
    dir = "stop";
    sendDirection();
}

function addAndConstrain(val, min, max) {
    spd += val;
    if (spd < min) spd = min;
    if (spd > max) spd = max;
    showOnLabel();
    sendSpeed();
}

function sendDirection() {
    var lbl = document.getElementById("label");
    lbl.innerHTML = "<strong>" + dir + "</strong>";
    let xhr = new XMLHttpRequest();
    xhr.open('GET', "Direction/" + dir, false);
    xhr.send();
}

function sendSpeed(){
    let xhr = new XMLHttpRequest();
    xhr.open('GET', "Speed/" + spd, false);
    xhr.send();
}

function showOnLabel() {
    var lblspd = document.getElementById("speed");
    lblspd.innerText = spd;
}

document.addEventListener('keyup', keyUpHandle);
document.addEventListener('keydown', keyDownHandle);
document.addEventListener('wheel', function(e){
    var shf = (e.deltaY > 0) ? -shift : shift;
    addAndConstrain(shf, 0, 100);
});