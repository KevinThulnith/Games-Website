let pass1 = document.getElementById("pas1");
let pass2 = document.getElementById("pas2");
let btt = document.getElementById("ok");
let bt1 = document.getElementById("bt1");

let bt2 = document.getElementById("bt2");
let baner = document.getElementById("banr");

pass2.addEventListener("input", () => {
  if (pass2.value == "" || pass2.value == pass1.value) {
    btt.disabled = false;
    baner.classList.add("hide");
  } else if (
    pass1.value.length <= pass2.value.length &&
    pass1.value != pass2.value
  ) {
    baner.classList.remove("hide");
    btt.disabled = true;
  } else if (pass2.value.length > 0) {
    btt.disabled = true;
    baner.classList.add("hide");
  }
});

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

showPassword(bt1, pass1);
showPassword(bt2, pass2);
