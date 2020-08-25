from pyunity import *

def main():
    scene = SceneManager.AddScene("Scene")
    
    scene.mainCamera.transform.position = Vector3(0, 3, -10)
    scene.mainCamera.transform.rotation = Vector3(20, 0, 0)
    
    cube = GameObject("Cube")
    cube.transform.position = Vector3(-4, 0, 0)
    renderer = cube.AddComponent(MeshRenderer)
    renderer.mesh = Mesh.cube(2)
    renderer.mat = Material((255, 0, 0))
    collider = cube.AddComponent(AABBoxCollider)
    collider.SetSize(-Vector3.one(), Vector3.one())
    collider.velocity = Vector3(-2, 0, 0)

    scene.Add(cube)
    
    cube = GameObject("Cube 2")
    cube.transform.position = Vector3(4, 0, 0)
    renderer = cube.AddComponent(MeshRenderer)
    renderer.mesh = Mesh.cube(2)
    renderer.mat = Material((0, 0, 255))
    collider = cube.AddComponent(AABBoxCollider)
    collider.SetSize(Vector3(4, -1, -1), Vector3(6, 1, 1))
    collider.velocity = Vector3(-4, 0, 0)

    scene.Add(cube)

    loader.SaveScene(scene)

    scene.Run()