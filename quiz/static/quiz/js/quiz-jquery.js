
/////////
//Total of an array
function add(a, b) {
    return a + b;
}

function getQuestion(num) {
	window[question_slug_list[num]]();
  
	$("#question_title").html('<h3>Q' + (num + 1) + '. ' + qTitle + '</h3>');
	$("#question_text").html('<h2>' + qText + '</h2>');
	$("#question_number").html('<h3>Score: ' + score.reduce(add, 0) + '/' + num);
	$("#answer").focus();
}

function getAns(num) {
  // Store answer to current question (REQUIRED?)
     ans.push(document.getElementById('answer').value);
    // Check if answer is correct
     if (ans[num] == correctAns) {
      score.push(1);
     }
     else {
       score.push(0);
     }
    var iter = num +1;

    $("#answer_box").html('<label for="answer">Answer:</label><input class="form-control" id="answer" type="text">');
	
	return iter;
}

function getScore(score) {
  $("#question_title").html('<h3>Final Score</h3>');
  
  var sum = score.reduce(add, 0);
  $("#question_text").html('<h2>' + sum + ' out of '+score.length+'</h2><br><br><br><br><br>');
  
  // Remove unwanted elements
  $('#next_question').remove();
  $('#answer_box').remove();
  $('#question_number').remove();
}

////////
$(document).ready(function() {
	
});