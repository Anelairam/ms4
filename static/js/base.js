var book_title = document.getElementsByClassName("title");

// Toggles the booking info from title to full text
for (var i=0; i<= book_title.length; i++){
    book_title[i].addEventListener("click", function(){
        this.nextElementSibling.classList.toggle("info_display");
    });
}
