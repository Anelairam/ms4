var book_title = document.getElementsByClassName("title");
var tablink = document.getElementsByClassName("tablinks");
var login = document.getElementById("login_container");
var signup = document.getElementById("signup_container");


for (var i=0; i<= book_title.length; i++){
    book_title[i].addEventListener("click", function(){
        this.nextElementSibling.classList.toggle("info_display");
    });
}

for (var i=0; i<= tablink.length; i++){
    tablink[i].addEventListener("click", function(){
        if (i == 0){
            login.style.display = "block";
        }
    });
}