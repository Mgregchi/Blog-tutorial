
$(document).ready(function(){
    $("#loader").click(function(){

        $("#container").load("/jquery-load-shopping-basket/",
        function(e){
            //Mix
            $("empty-basket-search")
            .prevObject[0]
            .getElementById("empty-basket-search")
            .addEventListner("keypress",
            function(e){
                $("#single-label").text("You've clicked: ".concat(e.keyCode))
            })

    })
    })


})
