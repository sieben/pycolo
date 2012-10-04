# coding=utf-8

import logging
from pycolo import LinkFormat, LocalEndpoint
from pycolo.coap import mediaTypeRegistry
from .pycolo.tests.ipso import DeviceBattery, PowerCumulative
from tests.ipso import DeviceModel, PowerRelay, DeviceSerial, DeviceManufacturer, DeviceName, PowerDimmer, PowerInstantaneous
import unittest

class DeviceManufacturer(LocalResource):
    """ This resource implements a part of the IPSO profile. """
    def __init__(self):
        """ generated source for method __init__ """
        super(DeviceManufacturer, self).__init__("dev/mfg")
        self.title = "Manufacturer"
        self.resourceType = "ipso:dev-mfg"
        self.interfaceDescription = "core#rp"

    def performGET(self, request):
        """ generated source for method performGET """
        #  complete the request
        request.respond(CodeRegistry.RESP_CONTENT,\
            "Pycolo", mediaTypeRegistry["TEXT_PLAIN"])

class DeviceModel(LocalResource):
    """ This resource implements a part of the IPSO profile. """
    def __init__(self):
        """ generated source for method __init__ """
        super(DeviceModel, self).__init__("dev/mdl")
        self.setTitle("Model")
        self.setResourceType("ipso:dev-mdl")
        self.setInterfaceDescription("core#rp")

    def performGET(self, request):
        """ generated source for method performGET """
        #  complete the request
        request.respond(codes.RESP_CONTENT,\
            "Californium", mediaTypeRegistry["TEXT_PLAIN"])

class DeviceName(LocalResource):
    """ This resource implements a part of the IPSO profile. """
    name = "IPSO Server"

    def __init__(self):
        """ generated source for method __init__ """
        self.title = "Name"
        self.resourceType = "ipso:dev-n"
        self.interfaceDescription = "core#p"
        self.address = "dev/n"

    def performGET(self, request):
        """ generated source for method performGET """
        #  complete the request
        request.respond(CodeRegistry.RESP_CONTENT,\
            self.name,\
            mediaTypeRegistry["TEXT_PLAIN"])

    def performPUT(self, request):
        """ generated source for method performPUT """
        if request.contentType != mediaTypeRegistry["TEXT_PLAIN"]:
            request.respond(CodeRegistry.RESP_BAD_REQUEST, "text/plain only")
            return
        self.name = request.payload
        #  complete the request
        request.respond(CodeRegistry.RESP_CHANGED)

class DeviceSerial(LocalResource):
    """ This resource implements a part of the IPSO profile. """
    def __init__(self):
        """ generated source for method __init__ """
        super(DeviceSerial, self).__init__("dev/ser")
        setTitle("Serial")
        setResourceType("ipso:dev-ser")
        setInterfaceDescription("core#rp")

    def performGET(self, request):
        """ generated source for method performGET """
        #  complete the request
        request.respond(codes.RESP_CONTENT, "4711", mediaTypeRegistry["TEXT_PLAIN"])



class DeviceBattery(LocalResource):
    """ This resource implements a part of the IPSO profile. """
    power = 3.6

    def __init__(self):
        """ generated source for method __init__ """
        super(DeviceBattery, self).__init__("dev/bat")
        self.title = "Battery"
        self.setResourceType("ipso:dev-bat")
        #  second rt not supported by current SensiNode RD demo
        # setResourceType("ucum:V");
        self.setInterfaceDescription("core#s")
        self.isObservable(True)
        #  Set timer task scheduling
        timer = Timer()
        timer.schedule(TimeTask(), 0, 1000)

    class TimeTask(TimerTask):
        """ generated source for class TimeTask """
        def run(self):
            """ generated source for method run """
            self.power -= 0.001 * random.SystemRandom()
            #  Call changed to notify subscribers
            self.changed()

    def performGET(self, request):
        """
         TODO: Strange call
        """
        #  complete the request
        request.respond(CodeRegistry.RESP_CONTENT,\
            self.power * 1000 / 1000,\
            mediaTypeRegistry["TEXT_PLAIN"])

class PowerCumulative(LocalResource):
    """ This resource implements a part of the IPSO profile. """
    power = 0

    def __init__(self):
        """ generated source for method __init__ """
        super(PowerCumulative, self).__init__("pwr/kwh")
        self.setTitle("Cumulative Power")
        self.setResourceType("ipso:pwr-kwh")
        #  second rt not supported by current SensiNode RD demo
        # setResourceType("ucum:kWh");
        self.setInterfaceDescription("core#s")
        self.isObservable(True)
        #  Set timer task scheduling
        timer = Timer()
        timer.schedule(TimeTask(), 0, 1000)

    class TimeTask(TimerTask):
        """ generated source for class TimeTask """
        def run(self):
            """ generated source for method run """
            if PowerRelay.getRelay():
                self.power += Math.round(10 * random.SystemRandom() * (PowerDimmer.getDimmer() / 100))
                #  Call changed to notify subscribers
                self.changed()

    def performGET(self, request):
        """ generated source for method performGET """
        #  complete the request
        request.respond(CodeRegistry.RESP_CONTENT, Double.toString(self.power), MediaTypeRegistry.TEXT_PLAIN)

class PowerDimmer(LocalResource):
    """ This resource implements a part of the IPSO profile. """
    percent = 100

    def __init__(self):
        """ generated source for method __init__ """
        super(PowerDimmer, self).__init__("pwr/dim")
        self.title = "Load Dimmer"
        self.resourceType = "ipso:pwr-dim"
        self.interfaceDescription = "core#a"
        self.observable = True

    def performGET(self, request):
        """ generated source for method performGET """
        #  complete the request
        request.respond(CodeRegistry.RESP_CONTENT,\
            int(self.percent),\
            mediaTypeRegistry["TEXT_PLAIN"])

    def performPUT(self, request):
        """ generated source for method performPUT """
        if request.contentType != mediaTypeRegistry["TEXT_PLAIN"]:
            request.respond(CodeRegistry.RESP_BAD_REQUEST, "text/plain only")
            return
        pl = int(request.payload)
        if 0 <= pl <= 100:
            if self.percent == pl:
                return
            self.percent = pl
            request.respond(CodeRegistry.RESP_CHANGED)
            self.changed()
        else:
            request.respond(CodeRegistry.RESP_BAD_REQUEST, "use 0-100")

class PowerInstantaneous(LocalResource):
    """ This resource implements a part of the IPSO profile. """
    power = 0

    def __init__(self):
        """ generated source for method __init__ """
        super(PowerInstantaneous, self).__init__("pwr/w")
        self.title = "Instantaneous Power"
        self.setResourceType("ipso:pwr-w")
        #  second rt not supported by current SensiNode RD demo
        # setResourceType("ucum:W");
        self.setInterfaceDescription("core#s")
        self.isObservable(True)
        #  Set timer task scheduling
        timer = Timer()
        timer.schedule(TimeTask(), 0, 1000)

    class TimeTask(TimerTask):
        """ generated source for class TimeTask """
        def run(self):
            """ generated source for method run """
            if self.PowerRelay.getRelay():
                self.power = 1500 * random.SystemRandom() * (PowerDimmer.getDimmer() / 100)
            else:
                #  skip changed() update if nothing changed
                if self.power == 0:
                    return
                self.power = 0
                #  Call changed to notify subscribers
            self.changed()

    def performGET(self, request):
        """ generated source for method performGET """
        #  complete the request
        request.respond(CodeRegistry.RESP_CONTENT,\
            str(self.power),\
            mediaTypeRegistry["TEXT_PLAIN"])

class PowerRelay(LocalResource):
    """ This resource implements a part of the IPSO profile. """
    on = True

    @classmethod
    def getRelay(cls):
        """ generated source for method getRelay """
        return cls.on

    def __init__(self):
        """ generated source for method __init__ """
        super(PowerRelay, self).__init__("pwr/rel")
        self.setTitle("Load Relay")
        self.setResourceType("ipso:pwr-rel")
        self.setInterfaceDescription("core#a")
        self.isObservable(True)

    def performGET(self, request):
        """ generated source for method performGET """
        #  complete the request
        request.respond(CodeRegistry.RESP_CONTENT,\
            "1" if self.on else "0",\
            mediaTypeRegistry["TEXT_PLAIN"])

    def performPUT(self, request):
        """ generated source for method performPUT """
        if request.contentType != mediaTypeRegistry["TEXT_PLAIN"]:
            request.respond(CodeRegistry.RESP_BAD_REQUEST, "text/plain only")
            return
        pl = request.getPayloadString()
        if pl == "true" or pl == "1":
            if self.on:
                return
            self.on = True
        elif pl == "false" or pl == "0":
            if not self.on:
                return
            self.on = False
        else:
            request.respond(CodeRegistry.RESP_BAD_REQUEST,\
                "use true/false or 1/0")
            return
            #  complete the request
        request.respond(CodeRegistry.RESP_CHANGED)
        self.changed()



class IpsoServer(LocalEndpoint):
    """
    The class IpsoServer provides an example of the IPSO Profile specification.
    The server registers its resources at the SensiNode Resource Directory.
    """
    #  exit codes for runtime errors
    ERR_INIT_FAILED = 1

    def __init__(self):
        """
        Constructor for a new PlugtestServer.Call to configure
        the port, etc. according to the {@link LocalEndpoint} constructors.
        Add all initial {@link LocalResource}s here.
        """
        super(IpsoServer, self).__init__()
        #  add resources to the server
        self.addResource(DeviceName())
        self.addResource(DeviceManufacturer())
        self.addResource(DeviceModel())
        self.addResource(DeviceSerial())
        self.addResource(DeviceBattery())
        self.addResource(PowerInstantaneous())
        self.addResource(PowerCumulative())
        self.addResource(PowerRelay())
        self.addResource(PowerDimmer())

    #  Logging ////////////////////////////////////////////////////////////////
    def handleRequest(self, request):
        """ generated source for method handleRequest """
        #  Add additional handling like special logging here.
        request.prettyPrint()
        #  dispatch to requested resource
        super(IpsoServer, self).handleRequest(request)

    #  Application entry point /////////////////////////////////////////////////
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        #  create server
        try:
            logging.info(IpsoServer.__class__.getSimpleName() + " listening on port %d.\n", server.port())
            #  specific handling for this request
            #  here: response received, output a pretty-print
            #  RD location
            if args[0].startsWith("coap://") and len(args):
                rd = args[0]
            else:
                logging.info("Hint: You can give the RD URI as first argument.")
                logging.info("Fallback to SensiNode RD")
            if args[1].matches("[A-Za-z0-9-_]+") and len(args):
                hostname = args[1]
            else:
                logging.info("Hint: You can give an alphanumeric (plus '-' and '_') string as second argument to specify a custom hostname.")
                logging.info("Fallback to hostname")
                try:
                    hostname = InetAddress.getLocalHost().getHostName()
                except UnknownHostException as e1:
                    print "Unable to retrieve hostname for registration"
                    print "Fallback to random"
            register.setURI(rd + "?h=Cf-" + hostname)
            register.setPayload(LinkFormat.serialize(server.getRootResource(), None, True), MediaTypeRegistry.APPLICATION_LINK_FORMAT)
            try:
                print("Registering at " + rd + " as Cf-" + hostname)
                register.execute()
            except Exception as e:
                logging.critical("Failed to execute request: " + e.getMessage())
                sys.exit(cls.ERR_INIT_FAILED)
        except SocketException as e:
            logging.critical("Failed to create " + IpsoServer.__class__.getSimpleName() + ": %s\n", e.getMessage())
            sys.exit(cls.ERR_INIT_FAILED)

if __name__ == '__main__':
    unittest.main()
