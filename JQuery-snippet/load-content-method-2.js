$(document).ready(function(){
    $("#loader").click(function(){

        $("#container").load("/jquery-load-shopping-basket/",
        function(e){

            $(this).find("#empty-basket-search")
            .keypress(function(e){
                $("#single-label").text("You've clicked: ".concat(e.keyCode))
            })                            


      })
    })


})

