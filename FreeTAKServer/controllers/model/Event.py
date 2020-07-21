import uuid
import datetime as dt
from .Detail import Detail
from .Point import Point
from lxml import etree

class Event:
    # TODO: fix emergency methods
    # Event.py
    # Python implementation of the Class Event
    # represents a TAK event: this class is instantiated with a standard set of
    #    values.
    # Generated by Enterprise Architect
    # Created on: 11-Feb-2020 11:08:07 AM
    # Original author: Corvo
    #

    # event as an XML
    #<?xml version="1.0" encoding="UTF-8" standalone="yes"?><event version="2.0" uid="Linux-ABC.server-ping" type="b-t-f" time="2020-02-14T20:32:31.444Z" start="2020-02-14T20:32:31.444Z" stale="2020-02-15T20:32:31.444Z" how="h-g-i-g-o"> 
        
        #default constructor

    def __init__(self):
        
        
        self.version = None
        self.uid = None
        self.type = None
        self.how = None

        self.m_detail = None
        self.m_Point = None
        self.Start = None
        case = {

            'default': self.defaultFunc,

            'timeout': self.timeoutFunc
            
            }

        DATETIME_FMT = "%Y-%m-%dT%H:%M:%SZ"
        # flag to determin e if this event is a geo chcat if so, will be added as a
        # prefix to the uid
        
        # starting time when an event should be considered valid
        start = "%Y-%m-%dT%H:%M:%SZ"
        # basic event
        # Gives a hint about how the coordinates were generated
        

        # Schema version of this event instance (e.g.  2.0)
            
        # time stamp: when the event was generated
        time = "%Y-%m-%dT%H:%M:%SZ" 
        
        # Hierarchically organized hint about event type (defaultis is 'a-f-G-I'
        # for infrastructure)
        
            # ending time when an event should no longer be considered valid
        stale = "%Y-%m-%dT%H:%M:%SZ" 
        
            # Globally unique name for this information on this event can have
            # additional information attached.
        # e.g.  -ping means that this request is a ping
        
        # flag to determine if this event is a Ping, in this case append to the UID
        
        
    @staticmethod
    def Connection(xml):
        m_event = Event()
        m_event.setm_detail(Detail.Connection(xml.find('detail')))
        m_event.setm_Point(Point(xml.find('point')))
        m_event.setversion("2.0")
        m_event.setuid(xml.get('uid'))
        m_event.settype(xml.get('type'))
        m_event.sethow(xml.get('how'))
        return m_event

    @staticmethod
    def GeoChat(xml):
        m_event = Event()
        m_event.setm_detail(Detail.GeoChat(xml.find('detail')))
        m_event.setm_Point(Point(xml.find('point')))
        m_event.setversion("2.0")
        m_event.setuid(xml.get('uid'))
        m_event.settype(xml.get('type'))
        m_event.sethow(xml.get('how'))
        return m_event

    @staticmethod
    def Ping(xml):
        m_event = Event()
        m_event.setm_detail(Detail.Ping(xml.find('detail')))
        m_event.setm_Point(xml.find('point'))
        m_event.setversion("2.0")
        m_event.setuid(xml.get('uid'))
        m_event.settype(xml.get('type'))
        m_event.sethow(xml.get('how'))
        return m_event

    @staticmethod
    def Other(xml, clientInformation):
        m_event = Event()
        m_event.setm_detail(Detail.Other(xml.find('detail')))
        m_event.setm_Point(xml.find('point'))
        m_event.setversion("2.0")
        m_event.setuid(xml.get('uid'))
        m_event.settype(xml.get('type'))
        m_event.sethow(xml.get('how'))
        return m_event

    @staticmethod
    def emergecyOn(xml):
        m_event = Event()
        m_event.setm_detail(Detail.Other(xml.find('detail')))
        m_event.setm_Point(xml.find('point'))
        m_event.setversion("2.0")
        m_event.setuid(xml.get('uid'))
        m_event.settype(xml.get('type'))
        m_event.sethow(xml.get('how'))
        return m_event

    @staticmethod
    def emergecyOff(xml):
        m_event = Event()
        m_event.setm_detail(Detail.Other(xml.find('detail')))
        m_event.setm_Point(xml.find('point'))
        m_event.setversion("2.0")
        m_event.setuid(xml.get('uid'))
        m_event.settype(xml.get('type'))
        m_event.sethow(xml.get('how'))
        return m_event

    @staticmethod
    def dropPoint(xml):
        m_event = Event()
        m_event.setm_detail(Detail.point(xml.find('detail')))
        m_event.setm_Point(xml.find('point'))
        m_event.setversion("2.0")
        m_event.setuid(xml.get('uid'))
        m_event.settype(xml.get('type'))
        m_event.sethow(xml.get('how'))
        return m_event

    def defaultFunc(self, DATETIME_FMT,  version, uid, type, how, isGeochat, isPing):
        self.how = how

        timer = dt.datetime
        now = timer.utcnow()
        zulu = now.strftime(DATETIME_FMT)
        stale_part = dt.datetime.strptime(zulu, DATETIME_FMT) + dt.timedelta(minutes = 1)
        stale_part = stale_part.strftime(DATETIME_FMT)
        self.setstale(str(stale_part))
        self.setstart(zulu)
        self.settime(zulu)
        self.type = type
        self.setuid(isGeochat=isGeochat, isPing=isPing)
        self.version = version

    def timeoutFunc(self, DATETIME_FMT, version, uid, type, how, isGeochat, isPing):
        self.how = how

        timer = dt.datetime
        now = timer.utcnow()
        zulu = now.strftime(DATETIME_FMT)
        stale_part = dt.datetime.strptime(zulu, DATETIME_FMT) - dt.timedelta(minutes = 1)
        stale_part = stale_part.strftime(DATETIME_FMT)
        self.setstale(str(stale_part))
        self.setstart(zulu)
        self.settime(zulu)
        self.type = type
        self.setuid(isGeochat = isGeochat, isPing=isPing)
        self.version = version
        #Start getter

    def getstart(self): 
        return self.Start 
    
        # Start setter
    def setstart(self, Start=0):  
        self.start = Start 
    
        # m_Point setter
    def setpoint(self, m_Point=0):  
        self.point = m_Point
    
        # how getter
    def gethow(self): 
        return self.how 
    
        
    # how setter
    def sethow(self, how=0):  
        self.how = how 

        # uid getter
    def getuid(self): 
        return self.uid 
    
        # uid setter
    def setuid(self, uid):
        self.uid = uid

            # version getter
    def getversion(self): 
        return self.version 
    
        # version setter
    def setversion(self, version):  
        self.version = version 

            # time getter
    def gettime(self): 
        return self.time 
    
        # time setter
    def settime(self, time=0):  
        self.time = time
        
        # stale getter
    def getstale(self): 
        return self.stale 
    
        # stale setter
    def setstale(self, stale=0):
        self.stale = stale 
    
            # type getter
    def gettype(self): 
        return self.type 
    
        # type setter
    def settype(self, type=0):  
        self.type = type

    def getm_Point(self):
        return self.m_Point

        # type setter

    def setm_Point(self, m_Point=None):
        self.m_Point = m_Point

    def getm_detail(self):
        return self.m_detail

        # type setter

    def setm_detail(self, m_detail=None):
        self.m_detail = m_detail