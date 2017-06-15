function adding_whole_numbers() {
	// Adds two whole numbers
	var a = Math.floor(Math.random() * 101);
	var b = Math.floor(Math.random() * 101);
	
	qTitle = "What is...";
	qText = a.toString() + " + " + b.toString();
	correctAns = a + b;	
}

function adding_decimals() {
	adding_whole_numbers()
}