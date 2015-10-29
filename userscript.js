// ==UserScript==
// @name         My Fancy New Userscript
// @namespace    http://your.homepage/
// @version      0.1
// @description  enter something useful
// @author       You
// @require      http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js
// @require      https://github.com/garand/sticky/blob/master/jquery.sticky.js
// @match        http://hayageek.com/greasemonkey-tutorial/
// @grant        none
// ==/UserScript==

this.$ = this.jQuery = jQuery.noConflict(true);
$(document).ready(function()
{
    var overlay = document.createElement("INPUT");
    overlay.setAttribute("type","file");
    var s = document.createElement("script");
    s.type = "text/javascript";
    s.src = "http://somedomain.com/somescript";
    $("head").append(s);
});