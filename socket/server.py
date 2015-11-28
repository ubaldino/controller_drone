
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
import os.path
import uuid
import pprint
from tornado.concurrent import Future
from tornado import gen
from tornado.options import define, options, parse_command_line

define("port", default=7777, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")
print "server in  port: 7777"

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
    def post( self ):
        if self.get_argument("value") == 'on':
            print "encender"
            #serial_com.write( "c\n" )
        elif self.get_argument("value") == 'off':
            print "apagar"
            #serial_com.write( "s\n" )

def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/control/action/on_off" , control_action_on_off ),
            (r"/control/action/all" , control_action_all )
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