import wpilib
import wpilib.drive
import rev
class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """Robot initialization function"""
        
        self.motor = rev.CANSparkMax(51, rev.CANSparkMax.MotorType.kBrushless) 
        self.encoder = self.motor.getEncoder()
        REVLibError = self.motor.setSmartCurrentLimit(rev.CANSparkMax.MotorType.kBrushless, 50)

    def teleopPeriodic(self):
        #print(self.motor.get())
        
        print(self.encoder.getPosition())
        self.motor.set(0.1)
        get()


if __name__ == "__main__":
    wpilib.run(MyRobot)
