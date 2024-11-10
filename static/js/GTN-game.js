let headers = document.querySelector(".window3").querySelectorAll("header"); //win or loose banners
let numBtt = document.querySelector(".window1").querySelectorAll("button"); //range button
let container = document.querySelector(".container"); //game window
let lives = [5, document.getElementById("lives")]; //update lives banner
let window3 = document.querySelector(".window3"); // window 3
let tiles = document.querySelectorAll(".tile"); // get number tiles
let frms = document.querySelector(".loost");
let frm = document.querySelector(".wnst");
let score1 = document.getElementById("scr1");
let score2 = document.getElementById("scr2");

let gmaests = eval(document.getElementById("status").value);

let randomValues = [null, null]; // set essential values
let rndist = []; //random number list
let mode = null; //game mode

function setMode(k) {
  mode = k;
  Senses();
  container.scrollTop = 600;
}

numBtt.forEach((btt) => {
  "Get input Values";
  btt.addEventListener("click", () => {
    let k = eval(btt.innerHTML);
    setMode(k);
  });
});

if (gmaests) {
  setMode(gmaests);
}

function Senses() {
  "Set value according to input values";
  randomValues[0] = Math.floor(Math.random() * mode);
  randomValues[1] = Math.floor(Math.random() * 16);
  makePad(mode);
  lives[1].innerHTML = lives[0];
}

function makePad(m) {
  "set values to pad";
  for (let g = 0; g < tiles.length; g++) {
    if (g == randomValues[1]) {
      tiles[g].querySelector(".num").innerHTML = randomValues[0];
    } else {
      s = Math.floor(Math.random() * m);
      while (s == randomValues[0] || rndist.indexOf(s) >= 0 || s == 0) {
        s = Math.floor(Math.random() * m);
      }
      rndist.push(s);
      tiles[g].querySelector(".num").innerHTML = s;
    }
  }
}

tiles.forEach((tile) => {
  tile.addEventListener("click", () => {
    if (eval(tile.id) == randomValues[1]) {
      WinGame();
    } else {
      LostGame(tile);
    }
  });
});

function fast() {
  window3.classList.remove("pop");
}

function WinGame() {
  fast();
  headers[0].classList.remove("pop");
  frm.classList.remove("pop");
  frms.classList.add("pop");
  score1.value = 10;
  score2.value = 10 + "/" + mode;
}

function LostGame(f) {
  f.classList.add("lght");
  lives[0] -= 1;
  lives[1].innerHTML = lives[0];
  if (lives[0] == 0) {
    fast();
    headers[1].classList.remove("pop");
    frms.classList.remove("pop");
  }
}

function Clear() {
  tiles.forEach((tile) => {
    tile.classList.remove("lght");
  });
  headers.forEach((hdr) => {
    hdr.classList.add("pop");
  });
  window3.classList.add("pop");
  lives[0] = 5;
  randomValues = [null, null];
  rndist = [];
}

function GoToMenu() {
  Clear();
  container.scrollTop = 0;
  mode = null;
}

function Restart() {
  Clear();
  Senses();
}
