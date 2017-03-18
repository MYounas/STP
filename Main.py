
from Switch import Switch

class Main:

    def main(self):

        totalSwitches=int(input("How many switches you want?"))

        switches=[]

        for i in range(totalSwitches):
            totalPorts=int(input("Enter total number of ports for switch "+str(i)+":"))
            switches.append(Switch(i,totalPorts))

        print("Now time for connection configuration")

        for i in range(totalSwitches):
            print("Ports configuration for switch ",i)
            for j in range(switches[i].ports):
                a = int(input("Enter other switch ID:"))
                b = int(input("Enter other switch's port ID:"))
                switches[i].portsConf[j]=["",a,b]

        for i in range(switches[0].ports):
            switches[0].portsConf[i][0]="dp"

        #for first time root ports setting
        oppPorts=self.getOppositePorts("dp",switches[0])

        keys=oppPorts.keys()    #keys of oppPorts dict

        for i in range(len(oppPorts)):
            for j in range(len(keys)):

                switchId=keys[j]
                portNum=oppPorts[switchId]      #port number of switch get from oppPorts switches list

                switches[switchId].portsConf[portNum][0]="rp"      #save as switchs k 2 pr ja k us k ports conf pr ja k dict say key utha k us k port wali value wali jga pr rp likh do


        print("thanks")

        # for i in range(totalSwitches):
        #     print(vars(switches[i]))
        #     print(dir(switches[i]))


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
