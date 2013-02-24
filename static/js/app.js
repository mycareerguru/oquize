$(document).ready(function() {

    $(".search-query").keydown(function(e) {
        if (e.which == 13) {
            query = $(".search-query").val();
            console.log(query);
            url = "/search/?query=" + encodeURIComponent(query);
            console.log(url);
            $("#container").load(url, function() {
                $("#container").children().first().before("<h3>Search result for " + $(".search-query").val() + "</h3>")
                console.log("AJAX success");
            });
            console.log("Enter button pressed", "value of search is ", $(".search-query").val());
            e.preventDefault();
        }
    })
})


