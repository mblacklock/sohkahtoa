var level;
var realWorld;
var topicQuiz;
var subtopic;
var highestLevel;
// Initialise Q number
var n = 0;
// Set up student answer array
var ans = [];
// Set up score array
var score = [];
// Question list
var question_slug_list = [];
var subtopic_list = [];
var subtopic_slug = [];
var level_list = [];
// Question variables
var qTitle, qText, correctAns;
	

$(document).ready(function() {
	
	subtopic = $("#subtopic-title").attr("data-subtopic");
	getActiveLevels(function(response){
		initScreen(response);
	});

	$(document).on("click", '#level-btn', function(event){
		level = $(this).val();
		
		getQuestionList(function(response) {
			console.log(response.length);
			if (response.length==0){
				noQuestions();
			} else {
				// Everything else is placed inside as it requires question_slug_list
				$.each(response , function(i, val) {
					question_slug_list.push(response[i].slug);
					subtopic_list.push(response[i].subtopic);
					subtopic_slug.push(response[i].subtopic_slug);
					level_list.push(response[i].level);						
				});
				console.log(subtopic_slug);
				console.log(level_list);
				
				// set up html
				setupQuiz();
				// Next Question button click
				$(document).on("click", '#next-question', function(event){
					n = getAns(n);

					if (n <= question_slug_list.length - 1) {
						// Get next question
						getQuestion(n);
					}
					else {
						// If last question, display score
						getScore(score);
						console.log(score)
						//postScores();
					}
				//
				});
				
				// Retry button click
				$(document).on("click", '#retry-button', function(event){
					setupQuiz();
				});
				//////////////////////
			};
		});
	});
});