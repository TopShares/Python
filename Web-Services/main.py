import sys
from spyne import Application,rpc,ServiceBase,Iterable,Integer,Unicode
from spyne.protocol.soap import Soap11,Soap12
from spyne.server.wsgi import WsgiApplication
 
class HelloWorldService1(ServiceBase):

    @rpc(Unicode,Integer,_returns=Iterable(Unicode))
    def say_hello11(ctx,name,times):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>
        @param name the name to say hello toccccccc
        @param times the number of times to say hello
        @return the completed array
        """
        for i in range(times):
            yield u'say_hello11 : Hello,%s' % name
    @rpc(Unicode,Integer,_returns=Iterable(Unicode))
 
    def say_hello12(ctx,name,times):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>
        @param name the name to say hello to
        @param times the number of times to say hello
        @return the completed array
        """
        for i in range(times):
            yield u'say_hello12 :　Hello,%s' % name
 

    @rpc(Unicode, Unicode, Unicode, _returns=Iterable(Unicode))
    def login(ctx,MAC,UserId,password):
        return '1'

class HelloWorldService2(ServiceBase):
    @rpc(Unicode,Integer,_returns=Iterable(Unicode))
    def say_hello21(ctx,name,times):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>
        @param name the name to say hello to
        @param times the number of times to say hello
        @return the completed array
        """
        for i in range(times):
            yield u'say_hello21 : Hello,%s' % name
 
    @rpc(Unicode,Integer,_returns=Iterable(Unicode))
    def say_hello22(ctx,name,times):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>
        @param name the name to say hello to
        @param times the number of times to say hello
        @return the completed array
        """
        for i in range(times):
            yield u'say_hello22 : Hello,%s' % name
 
# application = Application([HelloWorldService1,HelloWorldService2], 'http://www.cooldota.cn/mywebservice.asmx?WSDL',in_protocol=Soap11(validator='lxml'),out_protocol=Soap11())
application = Application([HelloWorldService1,HelloWorldService2],'http://schemas.xmlsoap.org/soap/envelope',in_protocol=Soap11(validator='lxml'),out_protocol=Soap11())
wsgi_application = WsgiApplication(application)
 
if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
    logging.info("listening to http://192.168.2.135:8080")
    logging.info("wsdl is at: http://192.168.2.135:8080/?wsdl")
    server = make_server('192.168.2.135',8080,wsgi_application)
    sys.exit(server.serve_forever())