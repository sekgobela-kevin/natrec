// Function to set a session cookie
function setSessionCookie(name, value) {
    document.cookie = name + "=" + value + "; path=/";
}

// Function to get the value of a session cookie
function getSessionCookie(name) {
    var cookieName = name + "=";
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.indexOf(cookieName) === 0) {
            return cookie.substring(cookieName.length, cookie.length);
        }
    }
    return null;
}

// Function to delete a session cookie
function deleteSessionCookie(name) {
    document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}