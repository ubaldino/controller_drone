// Copyright 2009 FriendFeed
//
// Licensed under the Apache License, Version 2.0 (the "License"); you may
// not use this file except in compliance with the License. You may obtain
// a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations
// under the License.

/*
let static = nipplejs.create({
    zone: document.getElementById( 'joystick_right' ),
    //zone: document.getElementById( 'joystick_right' ),
    mode: 'static',
    position: {left: '50%', top: '50%'},
    color: 'red'
});
*/
var options = {
    zone: document.getElementById( 'joystick_right' )
};
var manager = nipplejs.create( options );

/*
var seekbar = new Seekbar.Seekbar({
    renderTo: "#seekbar-container",
    minValue: 0,
    maxValue: 100,
    barSize: 4,
    needleSize: 0.8,
    valueListener: function (value) {
        /*
        valor_vel = ( Math.round( value ) / 20.0 ) + 4.5 ;
        this.setValue( value );
        document.getElementById( "pn_velocidad" ).innerHTML = valor_vel;
        * /
        var data = new FormData();
        data.append( "type" , "all" );
        data.append( "vel" , value );

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener( "readystatechange" , function () {
            if ( this.readyState === this.DONE ) {
                console.log( this.responseText );
            }
        });

        xhr.open( "POST", "/control/action/all" );
        xhr.send( data );

    },
    value: 0
});


switch_on_off = document.querySelector( ".switch label input" );

switch_on_off.addEventListener( 'change' , function( evt ){
    console.log( this.checked );

    var data = new FormData();
    data.append( "type" , "command" );
    if ( this.checked == true )
        data.append( "value" , "on" );
    else
        data.append( "value" , "off" );

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener( "readystatechange" , function () {
        if ( this.readyState === this.DONE ) {
            console.log( this.responseText );
        }
    });

    xhr.open( "POST", "/control/action/on_off" );
    xhr.send( data );

});




var updater = {
    errorSleepTime: 500,
    cursor: null,

    poll: function() {
        var args = {"_xsrf": getCookie("_xsrf")};
        if (updater.cursor) args.cursor = updater.cursor;
        $.ajax({url: "/a/message/updates", type: "POST", dataType: "text",
                data: $.param(args), success: updater.onSuccess,
                error: updater.onError});
    },

    onSuccess: function(response) {
        try {
            updater.newMessages(eval("(" + response + ")"));
        } catch (e) {
            updater.onError();
            return;
        }
        updater.errorSleepTime = 500;
        window.setTimeout(updater.poll, 0);
    },

    onError: function(response) {
        updater.errorSleepTime *= 2;
        console.log("Poll error; sleeping for", updater.errorSleepTime, "ms");
        window.setTimeout(updater.poll, updater.errorSleepTime);
    },

    newMessages: function(response) {
        if (!response.messages) return;
        updater.cursor = response.cursor;
        var messages = response.messages;
        updater.cursor = messages[messages.length - 1].id;
        console.log(messages.length, "new messages, cursor:", updater.cursor);
        for (var i = 0; i < messages.length; i++) {
            updater.showMessage(messages[i]);
        }
    },

    showMessage: function(message) {
        var existing = $("#m" + message.id);
        if (existing.length > 0) return;
        var node = $(message.html);
        node.hide();
        $("#inbox").append(node);
        node.slideDown();
    }
};



*/





/*
$(document).ready(function() {






    if (!window.console) window.console = {};
    if (!window.console.log) window.console.log = function() {};

    $("#messageform").live("submit", function() {
        newMessage($(this));
        return false;
    });
    $("#messageform").live("keypress", function(e) {
        if (e.keyCode == 13) {
            newMessage($(this));
            return false;
        }
    });
    $("#message").select();
    updater.poll();


    $("#slider").slider({
        min: 0,
        max: 100,
        step: 1,
        change: showValue
    });

    $( "#slider" ).bind( 'change' , function(){
        window.test = this;
        console.log( this );
    });

    $("#update").click(function () {
        $("#slider").slider("option", "value", $("#seekTo").val());
    });

    function showValue(event, ui) {
        $("#val").html(ui.value);
    }



});

function newMessage(form) {
    var message = form.formToDict();
    console.log( message );
    var disabled = form.find("input[type=submit]");
    disabled.disable();
    $.postJSON("/a/message/new", message, function(response) {
        updater.showMessage(response);
        if (message.id) {
            form.parent().remove();
        } else {
            form.find("input[type=text]").val("").select();
            disabled.enable();
        }
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

jQuery.postJSON = function(url, args, callback) {
    args._xsrf = getCookie("_xsrf");
    $.ajax({url: url, data: $.param(args), dataType: "text", type: "POST",
            success: function(response) {
        if (callback) callback(eval("(" + response + ")"));
    }, error: function(response) {
        console.log("ERROR:", response)
    }});
};

jQuery.fn.formToDict = function() {
    var fields = this.serializeArray();
    var json = {}
    for (var i = 0; i < fields.length; i++) {
        json[fields[i].name] = fields[i].value;
    }
    if (json.next) delete json.next;
    return json;
};

jQuery.fn.disable = function() {
    this.enable(false);
    return this;
};

jQuery.fn.enable = function(opt_enable) {
    if (arguments.length && !opt_enable) {
        this.attr("disabled", "disabled");
    } else {
        this.removeAttr("disabled");
    }
    return this;
};

var updater = {
    errorSleepTime: 500,
    cursor: null,

    poll: function() {
        var args = {"_xsrf": getCookie("_xsrf")};
        if (updater.cursor) args.cursor = updater.cursor;
        $.ajax({url: "/a/message/updates", type: "POST", dataType: "text",
                data: $.param(args), success: updater.onSuccess,
                error: updater.onError});
    },

    onSuccess: function(response) {
        try {
            updater.newMessages(eval("(" + response + ")"));
        } catch (e) {
            updater.onError();
            return;
        }
        updater.errorSleepTime = 500;
        window.setTimeout(updater.poll, 0);
    },

    onError: function(response) {
        updater.errorSleepTime *= 2;
        console.log("Poll error; sleeping for", updater.errorSleepTime, "ms");
        window.setTimeout(updater.poll, updater.errorSleepTime);
    },

    newMessages: function(response) {
        if (!response.messages) return;
        updater.cursor = response.cursor;
        var messages = response.messages;
        updater.cursor = messages[messages.length - 1].id;
        console.log(messages.length, "new messages, cursor:", updater.cursor);
        for (var i = 0; i < messages.length; i++) {
            updater.showMessage(messages[i]);
        }
    },

    showMessage: function(message) {
        var existing = $("#m" + message.id);
        if (existing.length > 0) return;
        var node = $(message.html);
        node.hide();
        $("#inbox").append(node);
        node.slideDown();
    }
};
*/