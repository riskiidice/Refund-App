$(document).ready(function(){
   $('#id_student_id').focus(function(){
       openWindow("http://etctutor.com/images/example.jpg");
   });
})

function openWindow(url) {
    window.open(url, "_blank", "toolbar=yes, scrollbars=yes, resizable=yes, top=600, left=600, width=600, height=400");
}
