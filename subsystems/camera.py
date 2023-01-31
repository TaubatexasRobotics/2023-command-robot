import commands2
import photonvision

class Camera(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.camera = photonvision.Camera('photonvision')
        result = self.camera.getLatestResult()
        if result.hasTargets():
            print('a target was found')
