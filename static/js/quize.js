
/*   Class for managing quize state */
function QuizeState(id, total) {
    this.id = id;
    this.totalQuestions = total;
    this.answered = 0;
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
});
