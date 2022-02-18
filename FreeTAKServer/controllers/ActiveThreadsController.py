#######################################################
# 
# ActiveThreadsController.py
# Python implementation of the Class ActiveThreadsController
# Generated by Enterprise Architect
# Created on:      21-May-2020 9:23:03 AM
# Original author: Natha Paquette
#
#######################################################
from FreeTAKServer.model.ActiveThreads import ActiveThreads

class ActiveThreadsController:
    def __init__(self):  
        self.ActiveThreads = ActiveThreads()

    def addClientThread(self, clientInformation, process):
        processObject = (clientInformation, process)
        self.ActiveThreads.thread_array.append(processObject)

    def addReceiveConnectionsThread(self, ReceiveConnectionsProcess, process):
        processObject = (ReceiveConnectionsProcess, process)
        self.ActiveThreads.thread_array.append(processObject)

    def removeClientThread(self, clientInformation):
        for x in self.ActiveThreads.thread_array:
            if x[0] == clientInformation:
                self.ActiveThreads.thread_array.remove(x)

    def removeReceiveConnectionProcess(self, ReceiveConnectionsProcess):
        for x in self.ActiveThreads.thread_array:
            if x[0] == ReceiveConnectionsProcess:
                self.ActiveThreads.thread_array.remove(x)
