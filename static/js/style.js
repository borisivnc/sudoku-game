
$(document).ready(function() {
    var pathname = window.location.pathname,
    pages = ['play-sudoku'];

    $('.navbar-nav .nav-item a').each(function(i) {
     if (pathname.includes(pages[i])){
        $(this).css("font-weight","bold")
        $(this).css("color","black")
     }
    });
});
