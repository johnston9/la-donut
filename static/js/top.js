/*-----return to top function-----*/

const topbutton = document.getElementById("topbut");

topbutton.addEventListener("click", poptop);

window.onscroll = function () {
	buttonDisplay();
};

function buttonDisplay() {
	if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
		topbutton.style.display = "block";
	} else {
		topbutton.style.display = "none";
	}
}

function poptop() {
	document.body.scrollTop = 0;
	document.documentElement.scrollTop = 0;
}