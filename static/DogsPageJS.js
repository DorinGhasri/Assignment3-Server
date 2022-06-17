var i = 0;
var txt ='Thank you! We will get back to you as soon as possible!';
var speed = 50;
let map;

if (document.getElementById("title")){
    const title = document.getElementById("title");
    title.addEventListener("mouseover", changeCream);
    title.addEventListener("mouseout", changeBlue);
}

function changeCream(){
  title.style.color = "rgb(252,236,228)";
}

function changeBlue(){
  title.style.color = "rgb(83, 138, 168)";
}




function myTyping(){
    if (i < txt.length) {
        document.getElementById("submitText").innerHTML += txt.charAt(i);
        i++;
        setTimeout(myTyping, speed);
    }
}


//pull the pathname from window location
const activePage = window.location.pathname;

/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/ 
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});
     

