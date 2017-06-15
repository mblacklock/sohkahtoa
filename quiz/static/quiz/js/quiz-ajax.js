// Set up student answer array
var ans = [];
// Set up score array
var score = [];
// Question list
var question_slug_list = [];
var subtopic_list = [];
var level_list = [];
// Question variables
var qTitle, qText, correctAns;


function getQuestionList(callback) {
	// Get question slug and populate question list based on instances
	var subtopic = $("#subtopic-title").attr("data-subtopic");
	$.get('/quiz/question_list/', {subtopic: subtopic}, callback);	
}

function postScores(){
	var csrftoken = Cookies.get('csrftoken');
	$.post('/quiz/update_scores/', {
		question_list: question_slug_list,
		subtopic_list: subtopic_list,
		level_list: level_list,
		score_list: score,
		csrfmiddlewaretoken: csrftoken
		}, function(data){
	});
}
	

$(document).ready(function() {

	getQuestionList(function(response) {
		
		// Everything else is placed inside as it requires question_slug_list
		$.each(response , function(i, val) {
			var j = 0;
			while (j < response[i].instances) {
				question_slug_list.push(response[i].slug);
				subtopic_list.push(response[i].subtopic);
				level_list.push(response[i].level);
				j++;
			}						
		});
		
		// Initialise Q number
		var n = 0;
		//Load first question
		getQuestion(n);
		// Next Question button click
		$("#next_question").off('click').click(function(){
			n = getAns(n);

			if (n <= question_slug_list.length - 1) {
				// Get next question
				getQuestion(n);
			}
			else {
				// If last question, display score
				getScore(score);
				console.log(score)
				postScores();
			}
		//
		});
		//////////////////////
	});
});