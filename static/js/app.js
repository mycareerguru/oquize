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


    /* register a click handler with jquery,
     * when user clicks a submit button for a question
     * this function will get called
     * Argument e is set to the button element clicked */
    var buttonClickedFunction = function(e) {
        console.log(e.target);
        // get the area of question for which submit button is
        // clicked.
        var f = $(e.target).parent().prev().parent();
        /* question id is stored in a hidden input filed with name
         * question. */
        var question = f.find('input[name=question]').val();
        /* quize id is stored in a global element whose id is
         * quizid */
        var qidelem = $("#quizid")[0];
        /* If quize is active then only qidelem is valid else
         * set qid to 0 */
        var qid = qidelem ? $(qidelem).val() : 0;
        
        /* If user have not clicked any answer then don't submi
         * it to the server */
        var ans = f.find('input[name=ans]:radio:checked').val();
        if (ans == undefined) {
            e.preventDefault();
            return;
        }
        var url = "/answer/?question=" + question + "&ans=" + ans + "&qid=" + qid;
	var q = f;
	$.ajax({
	    url: '/answer/',
	    data: {
		question: question,
		ans: ans,
		qid: qid
	    },
	    success: function() {
		q.hide();
		questionSubmitted(f);
	    }
	})
        e.preventDefault();
    };

    var likeUnlikClicked = function(e) {
	console.log(e.target);
	var type = $(e.target).attr("class");
	var f = $(e.target).parents()[2];
	var q_id = $(f).find('input[name=question]').val();
	if (type === "icon-thumbs-up") {
	    App.likeQuestion(f, q_id);
	    console.log("Thumbs up clicked " + q_id);
	} else if (type === "icon-thumbs-down") {
	    App.unlikeQuestion(f, q_id);
	    console.log("thumbs down clicked" + q_id);
	}
    };

    var closeClicked = function(e) {
	console.log("close clicked");
	var f = $(e.target).parents()[1];
	var q_id = $(f).find('input[name=question]').val();
	App.closeQuestion(f, q_id);
    };

    var registerCallbacks = function() {
        $(".question button").click(buttonClickedFunction);
        $(".question i").click(likeUnlikClicked);
        $(".question .header label").click(closeClicked);
    };

  /* register a function, which is called when user enter
   * data into search box, if user presses enter then
   * submit search query to server, and display the result
   * after menu bar */
    $(".search-query").keydown(function(e) {
        if (e.which == 13) {
            query = $(".search-query").val();
            console.log(query);
            url = "/search/?query=" + encodeURIComponent(query);
            console.log(url);
            $("#container").load(url, function() {
                //$("#container").children().first().before("<h3>Search result for " + $(".search-query").val() + "</h3>")
                console.log("AJAX success");
                registerCallbacks();
            });
            console.log("Enter button pressed", "value of search is ", $(".search-query").val());
            e.preventDefault();
        }
    })
    
    registerCallbacks();
});

App.likeQuestion = function(f, id) {
    $.ajax({
	'url' : '/like',
	data: {
	    id: id
	},
	success : function(data) {
	    $(f).find(".like").html(data);
	    console.log("ok");
	}
    });
};


App.unlikeQuestion = function(f, id) {
    $.ajax({
	'url' : '/unlike',
	data: {
	    id: id
	},
	success : function(data) {
	    $(f).find(".unlike").html(data);
	    console.log("ok");
	}
    });
};

App.closeQuestion = function(el, id) {
    $.ajax({
	url: '/qclose',
	data: {
	    id : id
	},
	success: function() {
	    $(el).hide();
	}
    });	
};

