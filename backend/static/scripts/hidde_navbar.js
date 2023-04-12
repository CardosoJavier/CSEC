
const navbar = document.querySelector('.navbar');
const originalOffsetTop = navbar.offsetTop;

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
if (window.pageYOffset >= originalOffsetTop + 50) {
    navbar.style.display = "none";
} else {
    navbar.style.display = "block";
}

if (window.pageYOffset <= originalOffsetTop) {
    navbar.style.display = "block";
}
}
