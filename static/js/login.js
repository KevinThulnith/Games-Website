let frmsts = document.getElementById("status"); // status input
let usrnme = document.getElementById("usnme"); // wrong username span
let paswrd = document.getElementById("pass"); // wrong password span
let usnme = document.getElementById("username"); //username field
let pass = document.getElementById("pass1"); //password field
let btt1 = document.getElementById("bt2"); // password show button

if (eval(frmsts.value) == 1) {
  usrnme.classList.remove("hide");
  hideBanner(usnme, usrnme);
} else if (eval(frmsts.value) == 2) {
  paswrd.classList.remove("hide");
  hideBanner(pass, paswrd);
}

function hideBanner(fld, bnr) {
  let t = 0;
  fld.addEventListener("input", () => {
    t++;
    if (t > 2) {
      bnr.classList.add("hide");
    }
  });
}

function showPassword(ele, fld) {
  ele.addEventListener("click", () => {
    ele.querySelector("img").classList.toggle("hide");
    if (fld.type == "password") {
      fld.type = "text";
    } else {
      fld.type = "password";
    }
  });
}

showPassword(btt1, pass);
