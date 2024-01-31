class Positional_PID:
    """Positional PID algorithm: First order linear sustem

    u(k) = K_p*e(k) + K_I * sum(e(i)) + K_D[e(t) - e(t - 1)]

    u(k)     -> related to all past states; actual position of the actuator
    e(t)     -> error value
    P (Proportion): e(k)
    I (Integral):   sum(e(i)) <- accumulation of error
    D (Derivative) : e(t) - e(t - 1) <- current_error - last time error

    """

    """
    Proportional Derivative Controller:
    Reduces overshoot and settling time
    """
    def __init__(self, P, I, D):
        self.Kp = P # Proportional Gain -- reduces the rise time, increases the overshoot, and reduces the steady-state error
        self.Ki = I # Integral Gain -- decrease rise time and increase both the overshoot and the settling time, and reduces the steady-state error
        self.Kd = D # Derivative Gain -- reduces overshoot and rise time

        self.SystemOutput = 0.0
        self.ResultValueBack = 0.0
        self.PidOutput = 0.0
        self.PIDErrADD = 0.0
        self.ErrBack = 0.0

    # Set PID controller parameters
    def SetStepSignal(self, StepSignal):
        Err = StepSignal - self.SystemOutput
        KpWork = self.Kp * Err
        KiWork = self.Ki * self.PIDErrADD
        KdWork = self.Kd * (Err - self.ErrBack)
        self.PidOutput = KpWork + KiWork + KdWork
        self.PIDErrADD += Err
        self.ErrBack = Err

        print( self.PidOutput, self.PIDErrADD, self.ErrBack)

    # Set the first-order inertial link system, where inertiatime is the inertial time constant
    def SetInertiaTime(self, InertiaTime, SampleTime):
        self.SystemOutput = (InertiaTime * self.ResultValueBack + \
                             SampleTime * self.PidOutput) / (SampleTime + InertiaTime)
        self.ResultValueBack = self.SystemOutput

    # def PID_control(self, s: str):
    #     """
    #     Closed loop PID
    #     X(s) is output
    #     R(s) is input

    #     X(s)/R(s)

    #     Args:
    #         tf (str): transfer function
    #     """
    #     s = int(s)
    #     T = (self.Kd * s^2 + self.Kp)
    #     pass

    # def continuous_time_controller(self, s: str):
    #     C =  self.Kp + self.Ki/s + self.Kd*s
    #     self.print_transfer_function(s)

    # def print_transfer_function(self, s: str): 
    #     print_string ="({kd}*{tf}^2+{kp}{tf}+{ki})/s".format(kp=self.Kp,tf=s,ki=self.Ki, kd=self.Kd)
    #     print(print_string)


    