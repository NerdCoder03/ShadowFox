#application of inheritance
from typing import Self
class MobilePhone:
    def __init__(self,screen_type="Touch Screen",network_type="4G/5G",dual_sim="True/False",front_camera="5MP/8MP/12MP/16MP",
                 rear_camera="8MP/12MP/16MP/32MP/48MP",RAM="4GB/6GB/8GB/12GB",Storage="128GB/256GB/512GB/1024GB"):
        self.screen_type=screen_type
        self.network_type=network_type
        self.dual_sim=dual_sim
        self.front_camera=front_camera
        self.rear_camera=rear_camera
        self.RAM=RAM
        self.storage=Storage
    def make_call(self,number):
        print(f"Calling {number}...")
    def receive_call(self):
        print("Receiving call...")

    def taking_pictures(self,camera_type):
        if camera_type=='front':
            print(f"Taking a picture with the {self.front_camera} front camera")
        elif camera_type=='rear':
            print(f"Taking a picture with the {self.rear_camera} rear camera")
class Apple(MobilePhone):
    def __init__(self,model,**kwargs):
        super().__init__(**kwargs)
        self.brand="Apple"
        self.model=model
    def face_id(self):
        print(f"Unlocking {self.brand} {self.model} with face ID")
class Samsung(MobilePhone):
    def __init__(self,model,**kwargs):
        super().__init__(**kwargs)
        self.brand="Samsung"
        self.model=model
    def ai(self):
        print(f"Optimising an image on {self.brand} {self.model} with Samsung AI")
iphone_14=Apple(model="14",front_camera="12MP",rear_camera="32MP",RAM="8GB")
iphone_15_pro_max=Apple(model="15 pro max",front_camera="16MP",rear_camera="48MP",RAM="12GB")
samsung_A54=Samsung(model="A54",front_camera="8MP",RAM="8GB",Storage="256GB")
samsung_S24_ultra=Samsung(model="S24 Ultra",rear_camera="48MP",RAM="12GB",Storage="1024GB")
iphone_14.face_id()
iphone_15_pro_max.make_call("123-456-7890")
iphone_15_pro_max.taking_pictures("rear")
samsung_A54.taking_pictures("front")
samsung_S24_ultra.receive_call()
samsung_S24_ultra.ai()

