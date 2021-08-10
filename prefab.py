import os
import json
class Test:
    def __init__(self) -> None:
        self.script='123456.py'
        self.mesh='(12,32,63,92),(12,96,31,35),(215,513,25,1.32),(15,31,2135,2)'
        self.transform='Vector3(16,20,30)'
        self.path='D:/pyunity'
        self.name='Test'
class Prefab:
    @staticmethod
    def Genrate(go:Test):
        script=go.script
        mesh=go.mesh
        trans=go.transform
        sp=go.path
        cwd=os.getcwd()
        json_={}
        json_["GameObject"]=go.name
        json_["script_name"]=script
        json_["script_path"]=sp
        json_["mesh"]=mesh
        json_["transform"]=trans
        c_json=json.dumps(json_)
        with open(f'{go.name}.json','w') as json_file:
            json_file.write(c_json)
    @staticmethod
    def Load(go:Test):
        with open(f'{go.name}.json','r') as json_f:
            data=json.load(json_f)
Prefab.Genrate(Test())
Prefab.Load(Test())