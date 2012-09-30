# coding=utf-8
import java.io.UnsupportedEncodingException
import java.nio.ByteBuffer


from pycolo.coap.OptionNumberRegistry import OptionNumberRegistry

class Option(object):
    """ This class describes the functionality of the CoAP header options. """
    DEFAULT_MAX_AGE = 60

    #  Attributes /////////////////////////////////////////////////////////////
    #  The option number defining the option type.
    optionNr = int()

    #  The raw data of the option.
    value = ByteBuffer()

    #  Constructors ///////////////////////////////////////////////////////////
    #
    # 	 * This is a constructor for a new option with a given number.
    # 	 *
    # 	 * @param nr the option number
    # 	 * @return A new option with a given number based on a byte array
    #
    @overloaded
    def __init__(self, nr):
        """ generated source for method __init__ """
        setOptionNumber(nr)

    #
    # 	 * This is a constructor for a new option with a given number, based on a
    # 	 * given byte array.
    # 	 *
    # 	 * @param raw the byte array
    # 	 * @param nr the option number
    # 	 * @return A new option with a given number based on a byte array
    # 	 
    @__init__.register(object, int, int)
    def __init___0(self, raw, nr):
        """ generated source for method __init___0 """
        setValue(raw)
        setOptionNumber(nr)

    @__init__.register(object, str, int)
    def __init___1(self, str_, nr):
        """
        This is a constructor for a new option with a given number, based on a
        given string.
        @param str the string
        @param nr the option number
        @return A new option with a given number based on a string
        """
        self.setStringValue(str_)
        self.setOptionNumber(nr)

    @__init__.register(object, int, int)
    def __init___2(self, val, nr):
        """
        This is a constructor for a new option with a given number, based on a
        given integer value.
        @param val the integer value
        @param nr the option number
        @return A new option with a given number based on a integer value
        """
        self.setIntValue(val)
        self.setOptionNumber(nr)

    @classmethod
    def fromNumber(cls, nr):
        """
        This method creates a new Option object with dynamic type corresponding
        to its option number.
        @param nr the option number
        @return A new option whose type matches the given number
        """
        if nr == OptionNumberRegistry.BLOCK1:
            pass
        elif nr == OptionNumberRegistry.BLOCK2:
            return BlockOption(nr)
        else:
            return Option(nr)

    @classmethod
    def split(cls, optionNumber, s, delimiter):
        """ generated source for method split """
        #  create option list
        options = ArrayList()
        if s != None:
            for segment in s.split(delimiter):
                #  handle non-empty segments only
                if not segment.isEmpty():
                    #  create a new option from the segment
                    #  and add it to the list
                    options.add(Option(segment, optionNumber))
        return options

    @classmethod
    def join(cls, options, delimiter):
        """ generated source for method join """
        if options != None:
            for opt in options:
                builder.append(delimiter)
                builder.append(opt.getStringValue())
            return builder.__str__()
        else:
            return ""

    def getOptionNumber(self):
        """ This method returns the option number of the current option """
        return self.optionNr

    def setOptionNumber(self, nr):
        """ This method sets the number of the current option. """
        self.optionNr = nr

    def getRawValue(self):
        """
        This method returns the data of the current option as byte array
        @return The byte array holding the data
        """
        return self.value.array()

    def setValue(self, value):
        """
        This method sets the current option's data to a given byte array
        @param value the byte array.
        """
        self.value = ByteBuffer.wrap(value)

    def getIntValue(self):
        """
        This method returns the value of the option's data as integer
        @return The integer representation of the current option's data
        """
        byteLength = self.value.capacity()
        temp = ByteBuffer.allocate(4)
        i = 0
        while i < (4 - byteLength):
            temp.put(int(0))
            i += 1
        i = 0
        while i < byteLength:
            temp.put(self.value.get(i))
            i += 1
        val = temp.getInt(0)
        return val

    def setIntValue(self, val):
        """
        This method sets the data of the current option based on a integer
        value.
        @param val the integer representation of the data which is stored in
        the current option
        """
        neededBytes = 4
        if val == 0:
            self.value = ByteBuffer.allocate(1)
            self.value.put(int(0))
        else:
            aux.putInt(val)
            while i >= 0:
                if aux.get(3 - i) == 0x00:
                    neededBytes -= 1
                else:
                    break
                i -= 1
            self.value = ByteBuffer.allocate(neededBytes)
            while i >= 0:
                self.value.put(aux.get(3 - i))
                i -= 1

    def getStringValue(self):
        """
        This method returns the value of the option's data as string
        @return The string representation of the current option's data
        """
        result = ""
        try:
            result = str(self.value.array(), "UTF8")
        except UnsupportedEncodingException as e:
            System.err.println("String conversion error")
        return result


    def setStringValue(self, str_):
        """
        This method sets the data of the current option based on a string input
        @param str the string representation of the data which is stored in the
        current option.
        """
        self.value = ByteBuffer.wrap(str_.getBytes())

    def getName(self):
        return str(OptionNumberRegistry.(self.optionNr))

    #
    # 	 * This method returns the length of the option's data in the ByteBuffer
    # 	 *
    # 	 * @return The length of the data stored in the ByteBuffer as number of
    # 	 * bytes
    #
    def getLength(self):
        """ generated source for method getLength """
        return self.value.capacity() if self.value != None else 0


    def equals(self, obj):
        """ generated source for method equals """
        if self == obj:
            return True
        if obj == None:
            return False
        if self.getClass() != obj.__class__:
            return False
        other = obj
        if self.optionNr != other.optionNr:
            return False
        if self.getRawValue() == None:
            if other.getRawValue() != None:
                return False
        elif not Arrays == self.getRawValue(, other.getRawValue()):
            return False
        return True

    @classmethod
    def hex(cls, data):
        """ generated source for method hex """
        if data != None and len(data):
            while len(data):
                builder.append("{:02X}".format((0xFF & data[i])))
                if i < len(data):
                    builder.append(' ')
                i += 1
            return builder.__str__()
        else:
            return "--"

    def __str__(self):
        """
        Returns a human-readable string representation of the option's value
        @Return The option value represented as a string
        """
        if self.optionNr == self.OptionNumberRegistry.CONTENT_TYPE:
            return self.MediaTypeRegistry.toString(self.getIntValue())
        elif self.optionNr == self.OptionNumberRegistry.MAX_AGE:
            return "{:d} s".format(self.getIntValue())
        elif self.optionNr == self.OptionNumberRegistry.PROXY_URI:
            return self.getStringValue()
        elif self.optionNr == self.OptionNumberRegistry.ETAG:
            return self.hex(self.getRawValue())
        elif self.optionNr == self.OptionNumberRegistry.URI_HOST:
            return self.getStringValue()
        elif self.optionNr == self.OptionNumberRegistry.LOCATION_PATH:
            return self.getStringValue()
        elif self.optionNr == self.OptionNumberRegistry.URI_PORT:
            return str(self.getIntValue())
        elif self.optionNr == self.OptionNumberRegistry.LOCATION_QUERY:
            return self.getStringValue()
        elif self.optionNr == self.OptionNumberRegistry.URI_PATH:
            return self.getStringValue()
        elif self.optionNr == self.OptionNumberRegistry.OBSERVE:
            return str.valueOf(self.getIntValue())
        elif self.optionNr == self.OptionNumberRegistry.TOKEN:
            return self.hex(self.getRawValue())
        elif self.optionNr == self.OptionNumberRegistry.URI_QUERY:
            return self.getStringValue()
        elif self.optionNr == self.OptionNumberRegistry.BLOCK1:
            pass
        elif self.optionNr == OptionNumberRegistry.BLOCK2:
            #  this case is actually handled
            #  in subclass BlockOption
            return str(self.getIntValue())
        else:
            return self.hex(self.getRawValue())

    def isDefaultValue(self):
        """ generated source for method isDefaultValue """
        if self.optionNr == OptionNumberRegistry.MAX_AGE:
            return self.getIntValue() == self.DEFAULT_MAX_AGE
        elif self.optionNr == OptionNumberRegistry.TOKEN:
            return self.getLength() == 0
        else:
            return False
