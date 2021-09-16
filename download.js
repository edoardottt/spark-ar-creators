// paste this on web console
var array = [];
var links = document.getElementsByTagName("a");
for (var i = 0; i < links.length; i++) {
    var sub = links[i].href;
    if (sub.substring(0, 22) == "https://instagram.com/" || sub.substring(0,25) == "https://www.instagram.com/") {
        array.push(sub);
    }
}
JSON.stringify(array)

