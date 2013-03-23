$(document).ready(function() {

    $(".search-query").keydown(function(e) {
        if (e.which == 13) {
            query = $(".search-query").val();
            console.log(query);
            url = "/search/?query=" + encodeURIComponent(query);
            console.log(url);
            $("#container").load(url, function() {
                //$("#container").children().first().before("<h3>Search result for " + $(".search-query").val() + "</h3>")
                console.log("AJAX success");
            });
            console.log("Enter button pressed", "value of search is ", $(".search-query").val());
            e.preventDefault();
        }
    })
    
    $(".question button").click(function(e) {
        console.log(e.target);
        var f = $(e.target).parent();
        var question = f.find('input[name=question]').val();
        var ans = f.find('input[name=ans]:radio:checked').val();
        var url = "/answer/?question=" + question + "&ans=" + ans;
        var q = f.parent();
        q.load(url);
        q.hide();
        e.preventDefault();
    })

});

var click_handler = function(e) {
    alert("You pressed me")
    var f = e.target.parent();
    var question = f.find('input[name=question]').val();
    var ans = f.find('input[name=ans]:radio:checked').val();
    url = "/answer/?question=" + question + "?ans=" + ans;
    f.parent.load(url);
    e.preventDefault();
}
