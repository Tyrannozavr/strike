let cs = document.querySelector(".header-top__logo-2");
let dropcs = document.querySelector(".dropcs");
let backCs = document.querySelector(".dropcs__top-cross");

cs.onclick = function () {
  dropcs.style.top = "0px";
};

backCs.onclick = function () {
  dropcs.style.top = "-999px";
};