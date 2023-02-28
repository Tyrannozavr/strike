let success = document.querySelector(".success");
let copy = document.querySelectorAll(".csdm__cart-link__copy");
let backSuccess = document.querySelector(".success__cross");

copy.forEach((el) => {
  el.onclick = function () {
    success.style.top = "60px";
  };
});
// copy.onclick = function(){
//     success.style.top = '800px';
// };
backSuccess.onclick = function () {
  success.style.top = "-999px";
};

const swiper = new Swiper(".swiper", {
  // Optional parameters
  direction: "horizontal",
  loop: true,
  speed: 1000,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  mouseshell: true,
  slidesPerView: 1,
  // effect: 'fade',
  autoplay: {
    delay: 2000,
    disableOnInteraction: false,
    transition: 100,
  },
  on: {
    init() {
      this.el.addEventListener("mouseenter", () => {
        this.autoplay.stop();
      });

      this.el.addEventListener("mouseleave", () => {
        this.autoplay.start();
      });
    },
  },
});
