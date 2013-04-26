
/*   Class for managing quize state */
function QuizeState(id, total, time) {
    var self = this;
    self.id = id;
    self.totalQuestions = total;
    self.answered = 0;
    self.time = time;

    self.start = function() {
	$("#countdown").countdown({
            until: "+" + self.time + "m",
            format: "hh:mm:ss",
	    onExpiry : self.stop
        });
    };
    
    self.stop = function() {
	window.location = "/quiz/" + self.id;
    };
    return this;
}

QuizeState.prototype.questionAnswered = function(q) {
    this.answered += 1;
    var perc = (this.answered / this.totalQuestions) * 100;
    $("#progress .bar").css({
        'width' : perc + "%",
    });
    if (this.answered === this.totalQuestions) {
        window.location.href = "/quiz/" + this.id;
    }
    var next = $(".question")[this.answered];
    $(next).show();
    // $("#totalA").html(this.answered);
}

App.questionSubmitted = function(q) {
    App.quize.questionAnswered(q);
}

$(function() {
   $(".question").hide();
   $(".question").first().show();

    $("#endTest").click(function() {
	App.quize.stop();
    });
});
