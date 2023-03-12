import wpilib
import wpilib.drive
import rev
class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """Robot initialization function"""
        
        self.motor = rev.CANSparkMax(0, rev.CANSparkMax.MotorType.kBrushless)  
        self.m_pidController = self.motor.GetPIDController()
        self.encoder = self.motor.getEncoder()
        
        kP = 0.1
        kI = 1e-4
        kD = 1.0
        kIz = 0.0
        kFF = 0.0
        kMaxOutput = 1.0
        kMinOutput = -1.0

        self.stick = wpilib.Joystick(0) 
        
        REVLibError = self.motor.setSmartCurrentLimit(rev.CANSparkMax.MotorType.kBrushless, 50)

        self.motor.RestoreFactoryDefaults()

        #set PID coefficients
        self.m_pidController.SetP(kP)
        self.m_pidController.SetI(kI)
        self.m_pidController.SetD(kD)
        self.m_pidController.SetIZone(kIz)
        self.m_pidController.SetFF(kFF)
        self.m_pidController.SetOutputRange(kMinOutput, kMaxOutput)

        #display PID coefficients on SmartDashboard
        wpilib.SmartDashboard.PutNumber("P Gain", kP)
        wpilib.SmartDashboard.PutNumber("I Gain", kI)
        wpilib.SmartDashboard.PutNumber("D Gain", kD)
        wpilib.SmartDashboard.PutNumber("I Zone", kIz)
        wpilib.SmartDashboard.PutNumber("Feed Forward", kFF)
        wpilib.SmartDashboard.PutNumber("Max Output", kMaxOutput)
        wpilib.SmartDashboard.PutNumber("Min Output", kMinOutput)
        wpilib.SmartDashboard.PutNumber("Set Rotations", 0)

    def teleopPeriodic(self):
        #print(self.motor.get())
        
        print(self.encoder.getPosition())
        self.motor.set(0.5)
            
        #read PID coefficients from SmartDashboard
        p = wpilib.SmartDashboard.GetNumber("P Gain", 0)
        i = wpilib.SmartDashboard.GetNumber("I Gain", 0)
        d = wpilib.SmartDashboard.GetNumber("D Gain", 0)
        iz = wpilib.SmartDashboard.GetNumber("I Zone", 0)
        ff = wpilib.SmartDashboard.GetNumber("Feed Forward", 0)
        max = wpilib.SmartDashboard.GetNumber("Max Output", 0)
        min = wpilib.SmartDashboard.GetNumber("Min Output", 0)
        rotations = wpilib.SmartDashboard.GetNumber("Set Rotations", 0)

        #if PID coefficients on SmartDashboard have changed, write new values to controller
        if((p != kP)):  
            self.m_pidController.SetP(p)
            kP = p
        if((i != kI)):
            self.m_pidController.SetI(i)
            kI = i
        if((d != kD)):
            self.m_pidController.SetD(d)
            kD = d
        if((iz != kIz)):
            self.m_pidController.SetIZone(iz)
            kIz = iz
        if((ff != kFF)):
            self.m_pidController.SetFF(ff)
            kFF = ff
        if((max != kMaxOutput)or(min != kMinOutput)):
            self.m_pidController.SetOutputRange(min, max)
            kMinOutput = min
            kMaxOutput = max 
        

        
        self.m_pidController.SetReference(rotations, rev.CANSparkMax.ControlType.kPosition)
        
        wpilib.SmartDashboard.PutNumber("SetPoint", rotations)
        wpilib.SmartDashboard.PutNumber("ProcessVariable", self.m_encoder.GetPosition())


if __name__ == "__main__":
    wpilib.run(MyRobot)
