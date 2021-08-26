import os
import json
class Cube:
    def __init__(self) -> None:
        pass
class Scene:
    def __init__(self) -> None:
        pass
    def get_shape(self,name):
        return Cube() 
class Mesh:
    def __init__(self,name) -> None:
        self.default=True
        self.scene=Scene()
        self.game=name
        self.shape=None if self.default!= True else self.scene.get_shape(self.game)
class gameObject:
    def __init__(self) -> None:
        self.name='Gameo'
        self.mesh=Mesh(self.name)
class prefabManager:
    def __init__(self,gameObject:gameObject) -> None:
        self.gameObject=gameObject
        print(self.gameObject.mesh.shape)
prefabManager(gameObject())