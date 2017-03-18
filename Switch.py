
class Switch():

    def __init__(self,id,ports):
        self.id=id
        self.ports=ports
        self.portsConf={}   #ports structure=["port type",switch_id,root_id]
