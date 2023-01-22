#!/usr/bin/env python3
import typing

import wpilib
import commands2
import commands2.cmd

import robotcontainer

class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        self.autonomousCommand: typing.Optional[commands2.Command] = None
        self.container = robotcontainer.RobotContainer()

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass

    def autonomousInit(self) -> None:
        self.autonomousCommand = self.container.getAutonomousCommand()

        if self.autonomousCommand is not None:
            self.autonomousCommand.schedule()
        else:
            print("no auto command?")

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        if self.autonomousCommand is not None:
            self.autonomousCommand.cancel()

    def teleopPeriodic(self) -> None:
        pass

    def testInit(self) -> None:
        commands2.CommandScheduler.getInstance().cancelAll()


if __name__ == "__main__":
    wpilib.run(MyRobot)
