let success = document.querySelector(".success");
let copy = document.querySelectorAll(".lobby-cart__link__copy");
let backSuccess = document.querySelector(".success__cross");

copy.forEach((el) => {
    el.onclick = function () {
    success.style.top = "30px";
    };
});
// copy.onclick = function(){
//     success.style.top = '800px';
// };
backSuccess.onclick = function () {
    success.style.top = "-999px";
};