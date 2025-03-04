$(document).ready( function () {

  console.log('Sanity Check!');

  function loading() {
    
   $(".loading").toggleClass("hidden");
   $("form").hide(); 

  }

  $("form").on("submit", loading);
  

} )
