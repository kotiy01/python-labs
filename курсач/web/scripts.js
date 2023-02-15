const circle1 = document.querySelector(".progress-ring__circle1");
const radius1 = circle1.r.baseVal.value;
const circumference1 = 2 * Math.PI * radius1;

circle1.style.strokeDasharray = `${circumference1} ${circumference1}`;
circle1.style.strokeDashoffset = circumference1;

function setProgress1(percent) {
    const offset = circumference1 - circumference1 * percent / 100;
    circle1.style.strokeDashoffset = offset;
}

const circle2 = document.querySelector(".progress-ring__circle2");
const radius2 = circle2.r.baseVal.value;
const circumference2 = 2 * Math.PI * radius2;

circle2.style.strokeDasharray = `${circumference2} ${circumference2}`;
circle2.style.strokeDashoffset = circumference2;

function setProgress2(percent) {
    const offset = circumference2 - circumference2 * percent / 100;
    circle2.style.strokeDashoffset = offset;
}

let cpu_percent = 0;
let memory_percent = 0;
let uptime = 0;
let diskFree = 0;
let timeOnCPU = 0;

function changeFill(info, circleClass, color) {
    document.getElementById(info).style.fill = color;
    document.querySelector(circleClass).style.stroke = color;
}

async function display_cpu_info() {
    let res = await eel.get_cpu_info()();
    cpu_percent = res["CPU in use"];
    memory_percent = res["Memory in use"];
    uptime = res["Uptime"];
    timeOnCPU = res["Time on CPU"];
    diskFree = res["Disk free"];
    if (Number(cpu_percent) <= 25) {
        changeFill("info1", ".progress-ring__circle1", "#00FA9A")
    } else if (Number(cpu_percent) > 25 && Number(cpu_percent) <= 50) {
        changeFill("info1", ".progress-ring__circle1", "#ADFF2F")
    } else if (Number(cpu_percent) > 50 && Number(cpu_percent) <= 75) {
        changeFill("info1", ".progress-ring__circle1", "#F4A460")
    } else {
        changeFill("info1", ".progress-ring__circle1", "#FF6347")
    }

    if (Number(memory_percent) <= 25) {
        changeFill("info2", ".progress-ring__circle2", "#00FA9A")
    } else if (Number(memory_percent) > 25 && Number(memory_percent) <= 50) {
        changeFill("info2", ".progress-ring__circle2", "#ADFF2F")
    } else if (Number(memory_percent) > 50 && Number(memory_percent) <= 75) {
        changeFill("info2", ".progress-ring__circle2", "#F4A460")
    } else {
        changeFill("info2", ".progress-ring__circle2", "#FF6347")
    }
    document.getElementById("cpu-info").innerHTML = cpu_percent;
    setProgress1(cpu_percent);
    document.getElementById("memory-info").innerHTML = memory_percent;
    setProgress2(memory_percent);
    document.getElementById("disk-free").innerHTML = diskFree;
    document.getElementById("uptime").innerHTML = uptime;
    document.getElementById("time-on-cpu").innerHTML = timeOnCPU;
    
}

setInterval(display_cpu_info, 500);