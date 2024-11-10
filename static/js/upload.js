let input = document.getElementById("image_input");
let inputDisplay = document.querySelector(".image");
let imageInput = "";

input.addEventListener("change", function () {
  const render = new FileReader();
  render.addEventListener("load", () => {
    imageInput = render.result;
    inputDisplay.style.backgroundImage = "url(" + imageInput + ")";
  });
  render.readAsDataURL(this.files[0]);
});
