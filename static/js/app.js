var App = {}

function questionSubmitted(question) {
  console.log("questionSubmmited called entry\n");
  console.log(App.questionSubmitted);
  if (typeof(App.questionSubmitted) === "function")
  {
    console.log("questionSubmmited called\n");
    App.questionSubmitted(question);
  }
}

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
        var qidelem = $("#quizid")[0];
        var qid = qidelem ? $(qidelem).val() : 0;
        var ans = f.find('input[name=ans]:radio:checked').val();
        if (ans == undefined) {
            e.preventDefault();
            return;
        }
        var url = "/answer/?question=" + question + "&ans=" + ans + "&qid=" + qid;
        var q = f.parent();
        q.load(url, function() {
            questionSubmitted(f);
        });
        q.hide();
        e.preventDefault();
    })
});
