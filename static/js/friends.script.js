let btn1 = document.querySelector(".list__user-friends");
let friends = document.querySelector(".list__friends-content");
let back1 = document.querySelector(".list__friends-content__cross");
let btn2 = document.querySelector(".list__user-search");
let search = document.querySelector(".list__friends-search");
let back2 = document.querySelector(".list__friends-search__cross");

btn1.onclick = function () {
    friends.style.right = "-20px";
};

back1.onclick = function () {
    friends.style.right = "-999px";
};

btn2.onclick = function () {
    search.style.right = "-20px";
};

back2.onclick = function () {
    search.style.right = "-999px";
};
