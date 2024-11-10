let tble = document.getElementById("table");
let btt1 = document.getElementById("lt");
let btt2 = document.getElementById("gt");
let pic = document.getElementById("prfl");
let ols = document.querySelector("ol");
let slide = document.getElementById("mygames");
let nmbr = 0;
let pos = 0;
let pos2 = 0;
let chn = 719;
let bcn = 250;

function btteff(f) {
  if (f == 1 && nmbr < 3) {
    nmbr++;
    pos += chn;
    pos2 += bcn;
  } else if (f != 1 && nmbr > 0) {
    nmbr--;
    pos -= chn;
    pos2 -= bcn;
  }
  tble.scrollLeft = pos;
  slide.scrollLeft = pos2;
}

btt1.addEventListener("click", () => {
  btteff(2);
});

btt2.addEventListener("click", () => {
  btteff(1);
});

pic.addEventListener("click", () => {
  ols.classList.toggle("pop");
});
