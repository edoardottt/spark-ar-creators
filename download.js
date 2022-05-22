// spark-ar-creators
// > https://github.com/edoardottt/spark-ar-creators
// > edoardottt, edoardoottavianelli.it
//
// paste this on web console and execute the code.
var array = [];
var links = document.getElementsByTagName("a");
for (var i = 0; i < links.length; i++) {
	var sub = links[i].href;
	/*
	Here we check if the links we are collecting are proper ones
	or not.
	We want only the instagram profile links.
	So in this case the formats can be:
		- https://instagram.com/username
		- https://www.instagram.com/username
	The things flushed out in these checks are:
		- /s/ for stories
		- /a/ for effects/filters
		- /p/ for posts 
		- /a/r/ for effects/filters
		- /stories/ for stories
		- /explore/ for explore filters
	*/
	if (
		(sub.substring(0, 22) == "https://instagram.com/" ||
			sub.substring(0, 26) == "https://www.instagram.com/") &&
		!(sub.substring(0, 28) == "https://www.instagram.com/s/" ||
			sub.substring(0, 24) == "https://instagram.com/s/") &&
		!(sub.substring(0, 28) == "https://www.instagram.com/a/" ||
			sub.substring(0, 24) == "https://instagram.com/a/") &&
		!(sub.substring(0, 28) == "https://www.instagram.com/p/" ||
			sub.substring(0, 24) == "https://instagram.com/p/") &&
		!(sub.substring(0, 29) == "https://www.instagram.com/ar/" ||
			sub.substring(0, 25) == "https://instagram.com/ar/") &&
		!(sub.substring(0, 34) == "https://www.instagram.com/stories/" ||
			sub.substring(0, 30) == "https://instagram.com/stories/") &&
		!(sub.substring(0, 34) == "https://www.instagram.com/explore/" ||
			sub.substring(0, 30) == "https://instagram.com/explore/")
	) {
		array.push(sub);
	}
}
JSON.stringify(array)

// Then copy the result array and create a file called 'data.txt'.
// Clean the data with readTxtUsers.py.
// You will have the clean result list in usersTxt.txt
