var book_title = document.getElementsByClassName("title");
var login_tab = document.getElementById("login_tablink");
var signup_tab = document.getElementById("signup_tablink");
var tablinks = document.getElementsByClassName("tablinks");
var tabcontent = document.getElementsByClassName("tabcontent");
var login = document.getElementById("login_container");
var signup = document.getElementById("singup_container");

// Toggles the booking info from title to full text
for (var i=0; i<= book_title.length; i++){
    book_title[i].addEventListener("click", function(){
        this.nextElementSibling.classList.toggle("info_display");
    });
}

// Tab animation and active effect on Login and Signup tab bar
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

// Disables past dates in form
function todayDate(){
    var date_field = document.getElementById("date_item");
    var today = new Date();
    var month = today.getMonth() +1; 
    var year = today.getUTCFullYear(); 
    var tdate = today.getDate();
    if (month < 10){
        month = "0" + month;
    }
    if(tdate < 10){
      tdate = "0" + tdate;
    }
    console.log(month, tdate);
    var minDate = year + "-" + month + "-" + tdate;
    console.log(minDate);
    date_field.setAttribute("min", minDate);
}