var book_title = document.getElementsByClassName("title");
var login_tab = document.getElementById("login_tablink");
var signup_tab = document.getElementById("signup_tablink");
var tablinks = document.getElementsByClassName("tablinks");
var tabcontent = document.getElementsByClassName("tabcontent");
var login = document.getElementById("login_container");
var signup = document.getElementById("singup_container");


for (var i=0; i<= book_title.length; i++){
    book_title[i].addEventListener("click", function(){
        this.nextElementSibling.classList.toggle("info_display");
    });
}

function activeTab(btn_name){
    for (var i=0; i<tablinks.length; i++){
        tablinks[i].classList.remove("active");
        tabcontent[i].style.display = "none";
    }
    if (btn_name == "login"){
        login_tab.classList.add("active");
        login.style.display = "block";
    }
    else if (btn_name == "signup"){
        signup_tab.classList.add("active");
        signup.style.display = "block";
    }
}