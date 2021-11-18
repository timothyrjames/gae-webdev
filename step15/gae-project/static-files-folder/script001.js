function createXmlHttp() {
    let xmlhttp = new XMLHttpRequest();
    if (!(xmlhttp)) {
        alert("Your browser does not support AJAX!");
    }
    return xmlhttp;
}


// this function converts a simple key-value object to a parameter string.
// we use this function from sendJsonRequest.
function objectToParameters(obj) {
    let text = '';
    for (let i in obj) {
        // encodeURIComponent is a built-in function that escapes to URL-safe values
        text += encodeURIComponent(i) + '=' + encodeURIComponent(obj[i]) + '&';
    }
    return text;
}


// this function uses an XMLHttpRequest to send a POST request to the server.
// we use this function from sendJsonRequest.
function postParameters(xmlHttp, targetUrl, parameters) {
    if (xmlHttp) {
        xmlHttp.open("POST", targetUrl, true); // XMLHttpRequest.open(method, url, async)
        let contentType = "application/x-www-form-urlencoded";
        xmlHttp.setRequestHeader("Content-type", contentType);
        xmlHttp.send(parameters);
    }
}


// this function is called from the application code; it takes a key-value
// object to represent the HTTP parameters, a URL to send the request, and
// the callbackFunction is called with the JSON response from the server.
function sendJsonRequest(parameterObject, targetUrl, callbackFunction) {
    let xmlHttp = createXmlHttp();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4) {
            console.log(xmlHttp.responseText);
            let myObject = JSON.parse(xmlHttp.responseText);
            callbackFunction(myObject, targetUrl, parameterObject);
        }
    }
    postParameters(xmlHttp, targetUrl, objectToParameters(parameterObject));
}


// This can load data from the server using a simple GET request.
function getData(targetUrl, callbackFunction) {
    let xmlHttp = createXmlHttp();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4) {
            // note that you can check xmlHttp.status here for the HTTP response code
            try {
                let myObject = JSON.parse(xmlHttp.responseText);
                callbackFunction(myObject, targetUrl);
            } catch (exc) {
                console.log("There was a problem at the server.");
            }
        }
    }
    xmlHttp.open("GET", targetUrl, true);
    xmlHttp.send();
}
