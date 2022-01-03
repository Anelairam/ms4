var book_title = document.getElementsByClassName("title");
var login_tab = document.getElementById("login_tablink");
var signup_tab = document.getElementById("signup_tablink");
var tablinks = document.getElementsByClassName("tablinks");
var login = document.getElementById("login_container");
var signup = document.getElementById("signup_container");


for (var i=0; i<= book_title.length; i++){
    book_title[i].addEventListener("click", function(){
        this.nextElementSibling.classList.toggle("info_display");
    });
}

function activeTab(btn_name){
    
}