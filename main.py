import requests
import threading
#########################
class SpamRing:
    def __init__(self, token: str, gc: str, id: str) -> None:
        self.token = token
        self.gc = gc
        self.id = id
        self.headers = {"authorization": self.token}
        self.baseurl = "https://discord.com/api/v9/"
        self.json = {"recipients": [self.id]}


    def change(self):
        r = requests.post(f"{self.baseurl}channels/{self.gc}/call/ring", headers=self.headers, json=self.json)
        print(f"Ringing: {self.id}")
        b = requests.post(f"{self.baseurl}channels/{self.gc}/call/stop-ringing", headers=self.headers, json=self.json)
        print(f"Stopped Ringing: {self.id}")

    def execute(self):
        while True:
            threading.Thread(target=self.change).start()

if __name__ == '__main__':
    obj = SpamRing(token=input(f"Token: "), gc=input(f"Enter Gc ID: "), id=input(f"Target ID: "))
    obj.execute()
    
