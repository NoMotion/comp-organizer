// ==UserScript==
// @name         My Fancy New Userscript
// @namespace    http://your.homepage/
// @version      0.1
// @description  enter something useful
// @author       You
// @require     http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js
// @match        https://www.google.com/*
// @grant        none
// ==/UserScript==
/*! fixto - v0.4.0 - 2015-06-08
* http://github.com/bbarakaci/fixto/*/
var fixto=function(a,b,c){function f(){this._vendor=null}function j(){var a=!1,b=c.createElement("div"),d=c.createElement("div");b.appendChild(d),b.style[h]="translate(0)",b.style.marginTop="10px",b.style.visibility="hidden",d.style.position="fixed",d.style.top=0,c.body.appendChild(b);var e=d.getBoundingClientRect();return e.top>0&&(a=!0),c.body.removeChild(b),a}function o(b,c,d){this.child=b,this._$child=a(b),this.parent=c,this.options={className:"fixto-fixed",top:0},this._setOptions(d)}function p(a,b,c){o.call(this,a,b,c),this._replacer=new e.MimicNode(a),this._ghostNode=this._replacer.replacer,this._saveStyles(),this._saveViewportHeight(),this._proxied_onscroll=this._bind(this._onscroll,this),this._proxied_onresize=this._bind(this._onresize,this),this.start()}function q(a,b,c){o.call(this,a,b,c),this.start()}var d=function(){var a={getAll:function(a){return c.defaultView.getComputedStyle(a)},get:function(a,b){return this.getAll(a)[b]},toFloat:function(a){return parseFloat(a,10)||0},getFloat:function(a,b){return this.toFloat(this.get(a,b))},_getAllCurrentStyle:function(a){return a.currentStyle}};return c.documentElement.currentStyle&&(a.getAll=a._getAllCurrentStyle),a}(),e=function(){function b(a){this.element=a,this.replacer=c.createElement("div"),this.replacer.style.visibility="hidden",this.hide(),a.parentNode.insertBefore(this.replacer,a)}b.prototype={replace:function(){var a=this.replacer.style,b=d.getAll(this.element);a.width=this._width(),a.height=this._height(),a.marginTop=b.marginTop,a.marginBottom=b.marginBottom,a.marginLeft=b.marginLeft,a.marginRight=b.marginRight,a.cssFloat=b.cssFloat,a.styleFloat=b.styleFloat,a.position=b.position,a.top=b.top,a.right=b.right,a.bottom=b.bottom,a.left=b.left,a.display=b.display},hide:function(){this.replacer.style.display="none"},_width:function(){return this.element.getBoundingClientRect().width+"px"},_widthOffset:function(){return this.element.offsetWidth+"px"},_height:function(){return this.element.getBoundingClientRect().height+"px"},_heightOffset:function(){return this.element.offsetHeight+"px"},destroy:function(){a(this.replacer).remove();for(var b in this)this.hasOwnProperty(b)&&(this[b]=null)}};var e=c.documentElement.getBoundingClientRect();return e.width||(b.prototype._width=b.prototype._widthOffset,b.prototype._height=b.prototype._heightOffset),{MimicNode:b,computedStyle:d}}();f.prototype={_vendors:{webkit:{cssPrefix:"-webkit-",jsPrefix:"Webkit"},moz:{cssPrefix:"-moz-",jsPrefix:"Moz"},ms:{cssPrefix:"-ms-",jsPrefix:"ms"},opera:{cssPrefix:"-o-",jsPrefix:"O"}},_prefixJsProperty:function(a,b){return a.jsPrefix+b[0].toUpperCase()+b.substr(1)},_prefixValue:function(a,b){return a.cssPrefix+b},_valueSupported:function(a,b,c){try{return c.style[a]=b,c.style[a]===b}catch(d){return!1}},propertySupported:function(a){return c.documentElement.style[a]!==undefined},getJsProperty:function(a){if(this.propertySupported(a))return a;if(this._vendor)return this._prefixJsProperty(this._vendor,a);var b;for(var c in this._vendors){b=this._prefixJsProperty(this._vendors[c],a);if(this.propertySupported(b))return this._vendor=this._vendors[c],b}return null},getCssValue:function(a,b){var d=c.createElement("div"),e=this.getJsProperty(a);if(this._valueSupported(e,b,d))return b;var f;if(this._vendor){f=this._prefixValue(this._vendor,b);if(this._valueSupported(e,f,d))return f}for(var g in this._vendors){f=this._prefixValue(this._vendors[g],b);if(this._valueSupported(e,f,d))return this._vendor=this._vendors[g],f}return null}};var g=new f,h=g.getJsProperty("transform"),i,k=g.getCssValue("position","sticky"),l=g.getCssValue("position","fixed"),m=navigator.appName==="Microsoft Internet Explorer",n;m&&(n=parseFloat(navigator.appVersion.split("MSIE")[1])),o.prototype={_mindtop:function(){var a=0;if(this._$mind){var b,c,e;for(var f=0,g=this._$mind.length;f<g;f++){b=this._$mind[f],c=b.getBoundingClientRect();if(c.height)a+=c.height;else{var h=d.getAll(b);a+=b.offsetHeight+d.toFloat(h.marginTop)+d.toFloat(h.marginBottom)}}}return a},stop:function(){this._stop(),this._running=!1},start:function(){this._running||(this._start(),this._running=!0)},destroy:function(){this.stop(),this._destroy(),this._$child.removeData("fixto-instance");for(var a in this)this.hasOwnProperty(a)&&(this[a]=null)},_setOptions:function(b){a.extend(this.options,b),this.options.mind&&(this._$mind=a(this.options.mind)),this.options.zIndex&&(this.child.style.zIndex=this.options.zIndex)},setOptions:function(a){this._setOptions(a),this.refresh()},_stop:function(){},_start:function(){},_destroy:function(){},refresh:function(){}},p.prototype=new o,a.extend(p.prototype,{_bind:function(a,b){return function(){return a.call(b)}},_toresize:n===8?c.documentElement:b,_onscroll:function(){this._scrollTop=c.documentElement.scrollTop||c.body.scrollTop,this._parentBottom=this.parent.offsetHeight+this._fullOffset("offsetTop",this.parent),this.options.mindBottomPadding!==!1&&(this._parentBottom-=d.getFloat(this.parent,"paddingBottom"));if(!this.fixed){var a=d.getAll(this.child);this._scrollTop<this._parentBottom&&this._scrollTop>this._fullOffset("offsetTop",this.child)-this.options.top-this._mindtop()&&this._viewportHeight>this.child.offsetHeight+d.toFloat(a.marginTop)+d.toFloat(a.marginBottom)&&(this._fix(),this._adjust())}else{if(this._scrollTop>this._parentBottom||this._scrollTop<this._fullOffset("offsetTop",this._ghostNode)-this.options.top-this._mindtop()){this._unfix();return}this._adjust()}},_adjust:function(){var a=0,b=this._mindtop(),c=0,e=d.getAll(this.child),f=null;i&&(f=this._getContext(),f&&(a=Math.abs(f.getBoundingClientRect().top))),c=this._parentBottom-this._scrollTop-(this.child.offsetHeight+d.toFloat(e.marginBottom)+b+this.options.top),c>0&&(c=0),this.child.style.top=c+b+a+this.options.top-d.toFloat(e.marginTop)+"px"},_fullOffset:function(a,b,c){var d=b[a],e=b.offsetParent;while(e!==null&&e!==c)d=d+e[a],e=e.offsetParent;return d},_getContext:function(){var a,b=this.child,e=null,f;while(!e){a=b.parentNode;if(a===c.documentElement)return null;f=d.getAll(a);if(f[h]!=="none"){e=a;break}b=a}return e},_fix:function(){var a=this.child,b=a.style,e=d.getAll(a),f=a.getBoundingClientRect().left,g=e.width;this._saveStyles(),c.documentElement.currentStyle&&(g=a.offsetWidth-(d.toFloat(e.paddingLeft)+d.toFloat(e.paddingRight)+d.toFloat(e.borderLeftWidth)+d.toFloat(e.borderRightWidth))+"px");if(i){var h=this._getContext();h&&(f=a.getBoundingClientRect().left-h.getBoundingClientRect().left)}this._replacer.replace(),b.left=f-d.toFloat(e.marginLeft)+"px",b.width=g,b.position="fixed",b.top=this._mindtop()+this.options.top-d.toFloat(e.marginTop)+"px",this._$child.addClass(this.options.className),this.fixed=!0},_unfix:function(){var a=this.child.style;this._replacer.hide(),a.position=this._childOriginalPosition,a.top=this._childOriginalTop,a.width=this._childOriginalWidth,a.left=this._childOriginalLeft,this._$child.removeClass(this.options.className),this.fixed=!1},_saveStyles:function(){var a=this.child.style;this._childOriginalPosition=a.position,this._childOriginalTop=a.top,this._childOriginalWidth=a.width,this._childOriginalLeft=a.left},_onresize:function(){this.refresh()},_saveViewportHeight:function(){this._viewportHeight=b.innerHeight||c.documentElement.clientHeight},_stop:function(){this._unfix(),a(b).unbind("scroll",this._proxied_onscroll),a(this._toresize).unbind("resize",this._proxied_onresize)},_start:function(){this._onscroll(),a(b).bind("scroll",this._proxied_onscroll),a(this._toresize).bind("resize",this._proxied_onresize)},_destroy:function(){this._replacer.destroy()},refresh:function(){this._saveViewportHeight(),this._unfix(),this._onscroll()}}),q.prototype=new o,a.extend(q.prototype,{_start:function(){var a=d.getAll(this.child);this._childOriginalPosition=a.position,this._childOriginalTop=a.top,this.child.style.position=k,this.refresh()},_stop:function(){this.child.style.position=this._childOriginalPosition,this.child.style.top=this._childOriginalTop},refresh:function(){this.child.style.top=this._mindtop()+this.options.top+"px"}});var r=function(a,b,c){return k&&!c||k&&c&&c.useNativeSticky!==!1?new q(a,b,c):l?(i===undefined&&(i=j()),new p(a,b,c)):"Neither fixed nor sticky positioning supported"};return n<8&&(r=function(){return"not supported"}),a.fn.fixTo=function(b,c){var d=a(b),e=0;return this.each(function(){var f=a(this).data("fixto-instance");if(!f)a(this).data("fixto-instance",r(this,d[e],c));else{var g=b;f[g].call(f,c)}e++})},{FixToContainer:p,fixTo:r,computedStyle:d,mimicNode:e}}(window.jQuery,window,document);
//==================================
this.$ = this.jQuery = jQuery.noConflict(true);
$(document).ready(function(){ 
    var userdiv = $("<div id='user-div' />");
    userdiv.html("<input type='file' />");
    console.log("Log");
    $('#rcnt').append(userdiv);
    $(userdiv).fixTo($('#rcnt'));
});