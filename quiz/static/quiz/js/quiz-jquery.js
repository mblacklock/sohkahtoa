
/////////
//Total of an array
function add(a, b) {
    return a + b;
}

function initScreen(response) {
	highestLevel = response.level;
	console.log('level ' + highestLevel)
	realWorld = $("#subtopic-title").attr("data-realWorld");
	topicQuiz = $("#subtopic-title").attr("data-topicQuiz");
	
	if(realWorld == 'False') {
		$("#level-text").html('<h2>Choose the level of questions:</h3>');
		if(highestLevel == '1'){	
			$("#question-text").html('<button id="level-btn" class="btn btn-primary" value="1">Level 1</button>' +
									 '<button id="level-btn" class="btn btn-primary" value="2" disabled>Level 2</button>');
		} else if(highestLevel == '2'){	
			$("#question-text").html('<button id="level-btn" class="btn btn-primary" value="1">Level 1</button>' +
									 '<button id="level-btn" class="btn btn-primary" value="2">Level 2</button>');
		};
		if(topicQuiz == 'True'){
			if(highestLevel == '3') {
				$("#question-text").append('<button id="level-btn" class="btn btn-primary" value="3">Level 3</button>');
			} else {
				$("#question-text").append('<button id="level-btn" class="btn btn-primary" value="3" disabled>Level 3</button>');
			};
		};
		// if level is not active, deactivate button
	} else {
		$("#question-text").html('<button id="level-btn" class="btn btn-primary" value="3">Begin Quiz</button>');
	};
}

function getActiveLevels(callback) {	
	$.get('/quiz/active_levels/', {subtopic: subtopic}, callback);	
}

function getQuestionList(callback) {
	// Get question slug and populate question list based on instances
	$.get('/quiz/question_list/', {subtopic: subtopic, topicQuiz: topicQuiz, level: level}, callback);	
}

function setupQuiz() {
	ans = [];
	score = [];
	$("#answer-box").html('<label for="answer">Answer:</label><input class="form-control" id="answer" type="text">');
	$("#button").html('<button id="next-question" class="btn btn-primary">Next Question</button>');
	n = 0;
	//Load first question
	getQuestion(n);	
}

function getQuestion(num) {
	window[question_slug_list[num]]();
  
	$("#level-text").html('<h3>Level ' + level_list[num] + '</h3>');
	$("#question_title").html('<h3>Q' + (num + 1) + '. ' + qTitle + '</h3>');
	$("#question-text").html('<h2>' + qText + '</h2>');
	$("#out-of").html('<h3>Score: ' + score.reduce(add, 0) + '/' + num);
	$("#answer").focus();
}

function getAns(num) {
     ans.push(document.getElementById('answer').value);
    // Check if answer is correct
     if (ans[num] == correctAns) {
      score.push(1);
     }
     else {
       score.push(0);
     }
    var iter = num +1;

	document.getElementById('answer').value = '';	
		
	return iter;
}

function getScore(score) {
  $("#question_title").html('<h3>Summary</h3>');
  
  var sum = score.reduce(add, 0);
	htmltext = '<h2> Score: ' + sum + ' out of '+score.length+'</h2>';
	score.forEach(function(e,i) {
		if (e==1) {
			htmltext += 'Q'+(i+1)+' - '+ans[i]+' - '+'Level '+level_list[i]+
				'  <span class="glyphicon glyphicon-ok" aria-hidden="true"></span>1 <br><br>'
		} else {
			htmltext += 'Q'+(i+1)+' - '+ans[i]+' - '+'Level '+level_list[i]+'  <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>0' +
				' <a href="../'+subtopic_slug[i]+'">'+subtopic_list[i]+'</a><br><br>'
		};
	});
	
	$("#question-text").html(htmltext);
	// Remove unwanted elements
	$('#next_question').remove();
	$('#button').html('<button id="retry-button" class="btn btn-primary"><span class="glyphicon glyphicon-repeat"></span> Retry Quiz</button>');
	$('#answer-box').html('');
	$('#out-of').html('');
	$('#level-text').html('');
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

function noQuestions(){
	$("#level-text").html('Error: No questions found.');
}

////////
$(document).ready(function() {
	
});