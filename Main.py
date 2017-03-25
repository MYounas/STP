
from Switch import Switch

class Main:

    def main(self):

        totalSwitches=int(input("How many switches you want?"))

        self.switches=[]

        for i in range(totalSwitches):
            totalPorts=int(input("Enter total number of ports for switch "+str(i)+":"))
            self.switches.append(Switch(i,totalPorts))

        print("Now time for connection configuration")

        for i in range(totalSwitches):
            print("Ports configuration for switch ",i)
            for j in range(self.switches[i].ports):
                a = int(input("Enter other switch ID:"))
                b = int(input("Enter other switch's port ID:"))
                self.switches[i].portsConf[j]=["",a,b]

        for i in range(self.switches[0].ports):
            self.switches[0].portsConf[i][0]="dp"

        #for first time root ports setting
        oppPorts=self.getOppositePorts("dp",self.switches[0])

        listKeys=list(oppPorts.keys())    #keys of oppPorts dict

        self.rootSelectionFromRoot(oppPorts,listKeys)

        #get list of switches jin ke root port set ni hoi basic rp setting k bad
        nonRootList=self.getNonRootSwitches()

        #set nonRoot switche's port to rp one by one

        if nonRootList:
            portsDist={}

            for i in range(len(nonRootList)):
                portsDist = {}
                currentSwitch=self.switches[nonRootList[i]]
                for j in range(currentSwitch.ports):
                    currentPort=currentSwitch.portsConf[j]
                    portsDist[j]=self.setRPOfNonROOT(currentSwitch,currentPort,dist=0)


        #work for dp

        print("thanks")

        # for i in range(totalSwitches):
        #     print(vars(switches[i]))
        #     print(dir(switches[i]))


    def setRPOfNonROOT(self,switch,port,dist):

        # portDistToRoot={}   #save as {port number:distance root switch tk}

        if port[1]==0:
            dist += 1
            return dist

        else:
            tempSwitch=self.switches[port[1]]
            dist += 1
            for j in range(tempSwitch.ports):
                tempPort=tempSwitch.portsConf[j]
                return self.setRPOfNonROOT(self.switches[port[1]],tempPort,dist)





    def getNonRootSwitches(self):

        nonRootList=[];rootFlag=False

        for i in range(1,len(self.switches)):
            rootFlag = False
            for j in range(self.switches[i].ports):
                if self.switches[i].portsConf[j][0]=="rp":
                    rootFlag=True
                    break
                elif self.switches[i].portsConf[j][0]!="rp":
                    rootFlag = False

            if not rootFlag:
                nonRootList.append(i)

        return nonRootList

    def rootSelectionFromRoot(self,oppPorts,listKeys):

        for i in range(len(listKeys)):
            switchId=listKeys[i]
            portNum=oppPorts[switchId]      #port number of switch get from oppPorts switches list

            self.switches[switchId].portsConf[portNum][0]="rp"      #save as switchs k 2 pr ja k us k ports conf pr ja k dict say key utha k us k port wali value wali jga pr rp likh do


    def getOppositePorts(self,portType,switch):

        oppPorts={}

        for i in range(switch.ports):
            if switch.portsConf[i][0]=="dp":

                dictSwitchID=switch.portsConf[i][1]
                dictSwitchPort=switch.portsConf[i][2]

                oppPorts[dictSwitchID]=dictSwitchPort     # save as oppPorts={2:1,...}#oppPorts me likh rha switch ke id and value  rkh rha hn jo us ke port hai

        return oppPorts









obj=Main()
obj.main()
