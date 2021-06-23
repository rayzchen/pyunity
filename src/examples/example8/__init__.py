from pyunity import *
from pyunity import config
import os

def main():
    scene = SceneManager.AddScene("Scene")
    if config.audio:
        path = os.path.abspath(os.path.dirname(__file__))
        clip = AudioClip(os.path.join(path, "explode.ogg"))
        source = scene.mainCamera.AddComponent(AudioSource)
        source.SetClip(clip)
        source.PlayOnStart = True

    SceneManager.LoadScene(scene)


if __name__ == "__main__":
    main()
