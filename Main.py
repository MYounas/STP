
from Switch import Switch

class Main:

    def main(self):
        totalSwitches=int(input("How many switches you want?"))

        switches=[]

        for i in range(totalSwitches):
            totalRoutes=int(input("Enter total number of routes for switch "+str(i)+":"))
            switches.append(Switch(i,totalRoutes))

        print("Now time for connections")
        print("If u r done with connection of a single switch write done and press enter")
        print("If u r done with connection of whole network write finished and press enter")














obj=Main()
obj.main()