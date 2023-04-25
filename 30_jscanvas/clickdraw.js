//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

//var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circ";
        bToggler.innerHTML = "circ";
    }
    else {
        mode = "rect";
        bToggler.innerHTML = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX
    var mouseY = e.offsetY
    console.log("mouseclick registered at ", mouseX, mouseY);

    ctx.fillStyle = "red";
    ctx.fillRect(mouseX, mouseY, 120,240);
}

var drawCircle = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "red";
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
}

var draw = function(e) {
    if (mode == "rect" || bToggler.innerHTML == "rect|circ") {
        drawRect(e);
    }
    else {
        drawCircle(e);
    }
}

var wipeCanvas = function() {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);