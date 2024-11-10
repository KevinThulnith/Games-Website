import { content } from "/static/js/content.js";
// import { rndword } from "/static/HM-words.js";

let box = document.querySelector(".box");

for (let info of content) {
  let co = document.createElement("div");
  co.classList.add("content");
  co.id = info["name"];
  let bo = document.createElement("div");
  bo.classList.add("info");
  let hdgn = document.createElement("h2");
  hdgn.innerHTML = info["name"];
  let para = document.createElement("p");
  para.innerHTML = info["about"];
  bo.appendChild(hdgn);
  bo.appendChild(para);
  let pic = document.createElement("img");
  pic.src = info["pick"];
  co.appendChild(pic);
  co.appendChild(bo);
  box.appendChild(co);
}

let slidebar = document.getElementById("p2");

//form slide bar
slidebar.innerHTML += "<button>&lt;</button>";
for (let a = 0; a < content.length; a++) {
  let element = content[a];
  let link = document.createElement("a");
  if (a == 0) {
    link.classList.add("ear");
  }
  link.href = "#" + element["name"];
  slidebar.appendChild(link);
}
slidebar.innerHTML += "<button>&gt;</button>";
//end slide bar

let cnt = 0;

let links = document.querySelector("#p2").querySelectorAll("a");
box.addEventListener("scroll", () => {
  for (let b = 0; b < content.length; b++) {
    const element = content[b];
    if (box.scrollLeft == element["pstn"]) {
      cnt = b;
      links[b].classList.add("ear");
    } else {
      links[b].classList.remove("ear");
    }
  }
});

let btts = document.querySelectorAll("button");

btts[0].addEventListener("click", () => {
  if (cnt > 0) {
    cnt--;
    setnumber();
  }
});

btts[1].addEventListener("click", () => {
  if (cnt < 10) {
    cnt++;
    setnumber();
  }
});

function setnumber() {
  box.scrollLeft = content[cnt]["pstn"];
}
