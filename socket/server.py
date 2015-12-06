
import os , sys , serial
"""
#serial_com = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600 ,
    timeout = 1
)

#serial_com.write( "s\n" )
#serial_com.write( "s\n" )
"""
DIR = os.path.dirname(__file__)

sys.path.append(  os.path.join( DIR , '../control' )  )

import logging
import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.websocket
import os.path
import uuid
import pprint
from tornado.concurrent import Future
from tornado import gen
from tornado.options import define, options, parse_command_line
from tornado_cors import CorsMixin

define("port", default=7777, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")
print "server in  port: 7777"

#from ControlRemoto import ControlRemoto
#control_remoto = ControlRemoto()

control_remoto = 2

class EchoWebSocket( tornado.websocket.WebSocketHandler ):
    def open( self ):
        print( "WebSocket opened" )
    def on_message( self, message ):
        print message
        #self.write_message( u"You said: " + message )
    def on_close(self):
        print( "WebSocket closed" )


class MessageBuffer(object):
    def __init__(self):
        self.waiters = set()
        self.cache = []
        self.cache_size = 200

    def wait_for_messages(self, cursor=None):
        # Construct a Future to return to our caller.  This allows
        # wait_for_messages to be yielded from a coroutine even though
        # it is not a coroutine itself.  We will set the result of the
        # Future when results are available.
        result_future = Future()
        if cursor:
            new_count = 0
            for msg in reversed(self.cache):
                if msg["id"] == cursor:
                    break
                new_count += 1
            if new_count:
                result_future.set_result(self.cache[-new_count:])
                return result_future
        self.waiters.add(result_future)
        return result_future

    def cancel_wait(self, future):
        self.waiters.remove(future)
        # Set an empty result to unblock any coroutines waiting.
        future.set_result([])

    def new_messages(self, messages):
        logging.info("Sending new message to %r listeners", len(self.waiters))
        for future in self.waiters:
            future.set_result(messages)
        self.waiters = set()
        self.cache.extend(messages)
        if len(self.cache) > self.cache_size:
            self.cache = self.cache[-self.cache_size:]


# Making this a non-singleton is left as an exercise for the reader.
global_message_buffer = MessageBuffer()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render( "index.html" , messages=global_message_buffer.cache )


class control_action_all( tornado.web.RequestHandler ):
    CORS_ORIGIN = '*'
    CORS_HEADERS = 'Content-Type'
    CORS_METHODS = 'POST'
    CORS_CREDENTIALS = True
    CORS_MAX_AGE = 21600
    CORS_EXPOSE_HEADERS = 'Location, X-WP-TotalPages'

    def post( self ):
        #pprint.pprint( self.request.arguments , width=1 )
        pprint.pprint( self.get_argument( "vel" ) )
        vel = int( float( self.get_argument( "vel" ) ) )
        #serial_com.write( "v%d\n"%(vel) )

class control_action_motor( tornado.web.RequestHandler ):
    def post( self ):
        #pprint.pprint( self.request.arguments , width=1 )
        pprint.pprint( self.get_argument( "vel" ) )
        num_motor = self.get_argument( "num_motor" )
        vel = int( float( self.get_argument( "vel" ) ) )
        #serial_com.write( "v%d\n"%(vel) )

class control_action_on_off( tornado.web.RequestHandler ):
    """
    CORS_ORIGIN = '*'
    CORS_HEADERS = 'Content-Type'
    CORS_METHODS = 'POST'
    CORS_CREDENTIALS = True
    CORS_MAX_AGE = 21600
    CORS_EXPOSE_HEADERS = 'Location, X-WP-TotalPages'
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        #self.set_header('Access-Control-Allow-Headers', 'origin, x-csrftoken, content-type, accept')
        self.set_header('Access-Control-Allow-Headers', '*')
        #self.set_header('Content-type', 'application/json')
    """
    def post( self ):
        pprint.pprint( self.request.arguments , width=1  )
        control_remoto.setAux2( int( self.get_argument( 'value' ) ) )

class control_action_roll( tornado.web.RequestHandler ):
    def post( self ):
        #print int( self.get_argument( 'roll' ) )
        control_remoto.setAleron( int( self.get_argument( "roll" ) ) )
class control_action_pitch( tornado.web.RequestHandler ):
    def post( self ):
        #print int( self.get_argument( 'pitch' ) )
        control_remoto.setElevador( int( self.get_argument( "pitch" ) ) )
class control_action_throttle( tornado.web.RequestHandler ):
    def post( self ):
        #print int( self.get_argument( 'throttle' ) )
        control_remoto.setAcelerador( int( self.get_argument( "throttle" ) ) )
class control_action_yaw( tornado.web.RequestHandler ):
    def post( self ):
        #print int( self.get_argument( 'yaw' ) )
        control_remoto.setTimon( int( self.get_argument( "yaw" ) ) )
class control_action_fly_mode( tornado.web.RequestHandler ):
    def post( self ):
        #print int( self.get_argument( 'value' ) )
        control_remoto.setAux1( int( self.get_argument( 'value' ) ) )
class control_action_accessory_0( tornado.web.RequestHandler ):
    def post( self ):
        #print int( self.get_argument( 'value' ) )
        control_remoto.setAux2( int( self.get_argument( 'value' ) ) )

class control_action_interrumpir( tornado.web.RequestHandler ):
    def post( self ):
        if self.get_argument("value") == 'on':
            print "encender"
        elif self.get_argument("value") == 'off':
            print "apagar"
            #control_remoto.interrumpir()


class control_action_reiniciar( tornado.web.RequestHandler ):
    def post( self ):
        if self.get_argument("value") == 'on':
            print "encender"
        elif self.get_argument("value") == 'off':
            print "apagar"
            control_remoto.reiniciar()

class control_action_resetear_valores( tornado.web.RequestHandler ):
    def post( self ):
        if self.get_argument("value") == 'on':
            print "encender"
        elif self.get_argument("value") == 'off':
            print "apagar"
            #control_remoto.resetearValores()


def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/control/action/on_off" , control_action_on_off ),
            (r"/control/action/all" , control_action_all ),

            (r"/control/action/roll" , control_action_roll ),
            (r"/control/action/pitch" , control_action_pitch ),
            (r"/control/action/throttle" , control_action_throttle ),
            (r"/control/action/yaw" , control_action_yaw ),

            (r"/control/action/fly_mode" , control_action_fly_mode ),
            (r"/control/action/accessory_0" , control_action_accessory_0 ),

            (r"/control/action/interrumpir" , control_action_interrumpir ),
            (r"/control/action/reiniciar" , control_action_reiniciar ),
            (r"/control/action/resetear_valores" , control_action_resetear_valores ),
            (r"/websocket" , EchoWebSocket )



        ],
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=False,
        debug=options.debug,
        )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
    tornado.autoreload.wait()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        #serial_com.write( "s\n" )
        #serial_com.close()
        print "Sever Close and Serial <Close></Close>"