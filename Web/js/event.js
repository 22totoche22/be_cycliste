$(document).ready(function()
{
  /* $("section#contacter form").on("submit", function(event){

     event.preventDefault();
     var param=$(this).serialize();
     //alert(param);
     var file="python/ajax.py/insertComment"
     var dataTy="html"
     var callb=function(data)
     {
        $("div#infoComment").html(data);
     };
     send_request(file, param, dataTy, callb)

   });


   $("section#connecter form").on("submit", function(event){
     event.preventDefault();
     var param=$(this).serialize();
     var file="python/ajax.py/connexion"
     var dataTy="html"
     var callb=function(data)
     {
        location.href="index.html";
     };
     send_request(file, param, dataTy, callb)
   });*/


});

function send_request(file, param, dataTy, callb)
{
    $.ajax({
        type: "POST",
        dataType : dataTy,
     	url: file,
     	data: param 
	})
	.done(function(data) {
	    callb(data)
	})
      .fail(function(retour) {
         alert( "problème :" + retour );
	});
}