// copies the css text stored on each button to the clipboard
var copyButtons = document.querySelectorAll(".copy-button");

copyButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    var cssText = button.getAttribute("data-css");
    navigator.clipboard.writeText(cssText);

    var originalLabel = button.textContent;
    button.textContent = "COPIED";

    setTimeout(function () {
      button.textContent = originalLabel;
    }, 1200);
  });
});
