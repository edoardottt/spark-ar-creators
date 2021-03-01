// paste this on web console
var array = [];
var links = document.getElementsByTagName("a");
for(var i=0; i<links.length; i++) {
    var sub = links[i].href.substring(23,27);
    if (sub == "user") {
    	var user = links[i].href.substring(28);
    	array.push(user);
    }
}
JSON.stringify(array)
