import commands2
import commands2.cmd

class RobotContainer:
    def __init__(self) -> None:
        self.configureButtonBindings()

    def configureButtonBindings(self) -> None:
        pass

    def getAutonomousCommand(self) -> commands2.Command:
        return commands2.cmd.nothing()
