

var DEFAULT_STABILITY_THROTTLE = 40;

var url_cv = "http://192.168.17.102:8081";

function send_post ( url , data ){
  var xhr = new XMLHttpRequest();
  xhr.withCredentials = true;

  xhr.addEventListener( "readystatechange" , function () {
    if ( this.readyState === this.DONE ) {
        console.log( this.responseText );
    }
  });

  xhr.open( "POST", url );
  xhr.send( data );
}


function send_get( url_params ){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", url_params, false ); // false for synchronous request
  xmlHttp.send( null );
  return xmlHttp.responseText;
}

var element = document.getElementById('joystick_left');
var joydiv = new JoydivModule.Joydiv( { 'element' : element } );

  // conduccion

element.addEventListener( 'joydiv-changed' , function( e ) {
    document.getElementById( 'direction' ).value = joydiv.getOneOf8Directions().name;

    aux = joydiv.getOneOf8Directions() ;

    switch( aux.name ){
      /*
      case 'up' :
        up_val =  ( 50 + ( 32 * aux.magnitude ) ).toFixed( 0 ) ;
        //console.log( 'up' , ( up_val <= 100 ) ? up_val : 100 );
      break;
      */
      case 'right' :
        right_val =  ( 50 + ( 33.3 * aux.magnitude ) ).toFixed( 0 ) ;
        //console.log( 'right' , ( right_val <= 100 ) ? right_val : 100 );
        var data = new FormData();
        data.append( "yaw" , ( right_val <= 100 ) ? right_val : 100 );
        send_post( "/control/action/yaw" , data );
      break;
      /*
      case 'down' :
        down_val = ( 50 - ( 33.3 * aux.magnitude ) ).toFixed( 0 ) ;
        console.log( 'down' , ( down_val >= 0 ) ? down_val : 0 );
      break;*/
      case 'left' :
        left_val = ( 50 - ( 33.3 * aux.magnitude ) ).toFixed( 0 ) ;
        //console.log( 'left' , ( left_val >= 0 ) ? left_val : 0 );
        var data = new FormData();
        data.append( "yaw" , ( left_val >= 0 ) ? left_val : 0 );
        send_post( "/control/action/yaw" , data );
      break;
      /*
      case 'up-right' :
        up_right_val =  ( 50 + ( 32 * aux.magnitude ) ).toFixed( 0 ) ;
        console.log( 'up-right' , ( up_right_val <= 100 ) ? up_right_val : 100 );
      break;
      case 'down-right' :
        down_right_val = ( 50 - ( 33.3 * aux.magnitude ) ).toFixed( 0 ) ;
        console.log( 'down-right' , ( down_right_val >= 0 ) ? down_right_val : 0 );
      break;
      case 'down-left' :
        down_left_val = ( 50 - ( 33.3 * aux.magnitude ) ).toFixed( 0 ) ;
        console.log( 'down-left' , ( down_left_val >= 0 ) ? down_left_val : 0 );
      break;
      case 'up-left' :
        up_left_val =  ( 50 + ( 32 * aux.magnitude ) ).toFixed( 0 ) ;
        console.log( 'up-left' , ( up_left_val <= 100 ) ? up_left_val : 100 );
      break;
      */
      case 'none' :
        var data = new FormData();
        data.append( "yaw" , 50 );
        send_post( "/control/action/yaw" , data );
        console.log( "______  none ----------" );
      break;
    }
});

// mando

var element2 = document.getElementById('joystick_right');
var joydiv2 = new JoydivModule.Joydiv( { 'element' : element2 } );

element2.addEventListener( 'joydiv-changed' , function( e ) {
    document.getElementById( 'direction' ).value = joydiv2.getOneOf8Directions().name;

    aux = joydiv2.getOneOf8Directions();

    switch( aux.name ){
      case 'up' :
        up_val =  ( 50 + ( 32 * aux.magnitude ) ).toFixed( 0 ) ;
        //console.log( 'up' , ( up_val <= 100 ) ? up_val : 100 );
        var data = new FormData();
        data.append( "pitch" , ( up_val <= 100 ) ? up_val : 100 );
        send_post( "/control/action/pitch" , data )
      break;
      case 'right' :
        right_val =  ( 50 + ( 32 * aux.magnitude ) ).toFixed( 0 ) ;
        //console.log( 'right' , ( right_val <= 100 ) ? right_val : 100 );
        var data = new FormData();
        data.append( "roll" , ( right_val <= 100 ) ? right_val : 100  );
        send_post( "/control/action/roll" , data );
      break;
      case 'down' :
        down_val = ( 50 - ( 33.3 * aux.magnitude ) ).toFixed( 0 ) ;
        //console.log( 'down' , ( down_val >= 0 ) ? down_val : 0 );
        var data = new FormData();
        data.append( "pitch" , ( down_val >= 0 ) ? down_val : 0 );
        send_post( "/control/action/pitch" , data );
      break;
      case 'left' :
        left_val = ( 50 - ( 33.3 * aux.magnitude ) ).toFixed( 0 ) ;
        //console.log( 'left' , ( left_val >= 0 ) ? left_val : 0 );
        var data = new FormData();
        data.append( "roll" , ( left_val >= 0 ) ? left_val : 0 );
        send_post( "/control/action/roll" , data );
      break;

      /*
      case 'up-right' :
        up_right_val =  ( 50 + ( 32 * aux.magnitude ) ).toFixed( 0 ) ;
        console.log( 'up-right' , ( up_right_val <= 100 ) ? up_right_val : 100 );
      break;
      case 'down-right' :
        //down_right_val = ( 50 - ( 33.3 * aux.magnitude ) ).toFixed( 0 ) ;
        //console.log( 'down-right' , ( down_right_val >= 0 ) ? down_right_val : 0 );
      break;
      case 'down-left' :
        //down_left_val = ( 50 - ( 33.3 * aux.magnitude ) ).toFixed( 0 ) ;
        //console.log( 'down-left' , ( down_left_val >= 0 ) ? down_left_val : 0 );
      break;
      case 'up-left' :
        //up_left_val =  ( 50 + ( 32 * aux.magnitude ) ).toFixed( 0 ) ;
        //console.log( 'up-left' , ( up_left_val <= 100 ) ? up_left_val : 100 );
      break;
      */

      case 'none' :
        var data = new FormData();
        data.append( "roll" , 50 );
        data.append( "pitch" , 50 );
        send_post( "/control/action/roll" , data );
        send_post( "/control/action/pitch" , data );
        send_post( "/control/action/roll" , data );
        send_post( "/control/action/pitch" , data );
        console.log( "______  none ----------" );
      break;
    }
});



  /*
  sen_post( "/control/action/aux_1" , data )
  sen_post( "/control/action/aux_2" , data )
  sen_post( "/control/action/interrumpir" , data )
  sen_post( "/control/action/reiniciar" , data )
  sen_post( "/control/action/resetear_valores" , data )
  */

  /*
  var aux_1_slider = new Seekbar.Seekbar({
      renderTo: "#seekbar-container-horizontal-aux1",
      minValue: 0,
      maxValue: 100,
      barSize : 5,
      needleSize : 0.1,
      valueListener: function ( value ) {
          throttle_val = Math.round( value );
          console.log( throttle_val );
      },
      thumbColor: '#cc006699', // ARGB is supported, Alpha, Red, Green and Blue
      negativeColor: '#006699',
      positiveColor: '#CCC',
      value: 0
  });


   var blueSlider = new Seekbar.Seekbar({
      renderTo: "#seekbar-container-vertical-blue",
      minValue: 0,
      maxValue: 100,
      barSize : 5,
      needleSize : 0.1,
      valueListener: function ( value ) {
          throttle_val = Math.round( value );
          this.value = throttle_val;
          var data = new FormData();
          data.append( "throttle" , throttle_val );
          send_post( "/control/action/throttle" , data );
          console.log( throttle_val );
      },
      thumbColor: '#cc006699', // ARGB is supported, Alpha, Red, Green and Blue
      negativeColor: '#006699',
      positiveColor: '#CCC',
      value: 0
  });


  switch_on_off = document.querySelector( ".switch label input" );
  switch_aux_1 = document.querySelector( ".switch label input" );
  switch_aux_2 = document.querySelector( ".switch label input" );

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
  */

// Add segments to a slider
$.fn.addSliderSegments = function (amount, orientation) {
  return this.each(function () {
    if (orientation == "vertical") {
      var output = ''
        , i;
      for (i = 1; i <= amount - 2; i++) {
        output += '<div class="ui-slider-segment" style="top:' + 100 / (amount - 1) * i + '%;"></div>';
      };
      $(this).prepend(output);
    } else {
      var segmentGap = 100 / (amount - 1) + "%"
        , segment = '<div class="ui-slider-segment" style="margin-left: ' + segmentGap + ';"></div>';
      $(this).prepend(segment.repeat(amount - 2));
    }
  });
};

var $slider_fly_mode  = $( "#slider_aux_1" );
var $slider_accessory_0  = $( "#slider_aux_2" );
var $slider_on_off = $( "#slider_on_off" );
var $slider_throttle = $( "#slider_throttle" );


if ( $slider_fly_mode.length > 0 && $slider_on_off.length > 0 ) {
  $slider_fly_mode.slider({
    min: 1,
    max: 3,
    value: 2,
    orientation: "horizontal",
    range: "min",
    slide: function( event , ui ) {

      var data = new FormData();
      data.append( "type" , "command" );
      if ( ui.value == 1 )
          data.append( "value" , 0 );
      else if ( ui.value == 2 )
          data.append( "value" , 50 );
      else if ( ui.value == 3 )
          data.append( "value" , 100 );

      send_post( "/control/action/fly_mode" , data );
    }
  });//.addSliderSegments( $slider.slider("option").max );

  $slider_on_off.slider({
    min: 1,
    max: 2,
    value: 1,
    orientation: "horizontal",
    range: "min",
    slide: function( event , ui ) {
      var data = new FormData();
      data.append( "type" , "command" );
      if ( ui.value == 2 )
          data.append( "value" , 100 );
      else
          data.append( "value" , 0 );
      send_post( "/control/action/on_off" , data );
    }
  });

    /*
    $slider_accessory_0.slider({
      min: 1,
      max: 3,
      value: 2,
      orientation: "horizontal",
      range: "min",
      slide: function( event , ui ) {

        console.log( ui.value );

        var data = new FormData();
        data.append( "type" , "command" );
        if ( ui.value == 1 )
            data.append( "value" , 0 );
        else if ( ui.value == 2 )
            data.append( "value" , 50 );
        else if ( ui.value == 3 )
            data.append( "value" , 100 );

        send_post( "/control/action/accessory_0" , data );
      }
    });
    */

  $slider_throttle.slider({
    min: 0,
    max: 100,
    value: 0,
    orientation: "vertical",
    range: "min",
    slide: function( event , ui ) {
      throttle_val = Math.round( ui.value );
        this.value = throttle_val;
        var data = new FormData();
        data.append( "throttle" , throttle_val );
        send_post( "/control/action/throttle" , data );
        document.querySelector( "#slider_throttle .ui-slider-handle" ).innerText = throttle_val;
    }
  })

  $slider_throttle.mouseup(function(){
    if ( $slider_throttle.val() >= DEFAULT_STABILITY_THROTTLE ) {
      $slider_throttle.slider( "value" , DEFAULT_STABILITY_THROTTLE  )
      var data = new FormData();
      data.append( "throttle" , DEFAULT_STABILITY_THROTTLE );
      send_post( "/control/action/throttle" , data );
      document.querySelector( "#slider_throttle .ui-slider-handle" ).innerText = DEFAULT_STABILITY_THROTTLE;
    }
  });

}

$("input[name='option_radios_cv']").bind( 'change' , function( evt ){
    window.test = evt;
    console.log( test.target.value  );
    var data = new FormData();
    data.append( "CMD" ,  evt.target.value );
    document.getElementById( "cv_control" ).style.display = "none";
    document.getElementById( "btn_cv_control" ).style.display = "block"
    send_get( url_cv + "/?cmd=" + evt.target.value );
});

  /*

  $("input[id='switch-02']").bootstrapSwitch();


  $("input[id='switch-02']").on('switchChange.bootstrapSwitch', function(event, state) {

    var data = new FormData();
    data.append( "type" , "command" );
    if ( state == false )
        data.append( "value" , 0 );
    else if ( state == true )
        data.append( "value" , 100 );

    send_post( "/control/action/accessory_0" , data );

  });
*/

document.getElementById( "btn_cv_control" ).addEventListener( 'click' , function(){
  document.getElementById( "cv_control" ).style.display = "block";
  document.getElementById( "btn_cv_control" ).style.display = "none"
});



var ws = new WebSocket( document.location.origin.replace( "http" , "ws" ) + "/websocket" );
ws.onopen = function() {
   ws.send("Hello, world");
};
ws.onmessage = function (evt) {
   alert(evt.data);
};


