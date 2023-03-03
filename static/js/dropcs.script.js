let cs = document.querySelector(".header-top__logo-2");
let dropcs = document.querySelector(".dropcs");
let backCs = document.querySelector(".dropcs__top-cross");
let search_friends = document.querySelector("#hello")


cs.onclick = function () {
  dropcs.style.top = "0px";
};

backCs.onclick = function () {
  dropcs.style.top = "-999px";
};

search_friends.oninput = function () {
  console.log('changing..............')
}