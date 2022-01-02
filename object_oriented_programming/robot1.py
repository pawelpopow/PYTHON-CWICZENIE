from object_oriented_programming.robot import Robot

if __name__ == '__main__':
    droid1 = Robot('R2-D2')
    droid1.przywitajSie()
    Robot.jakDuzo()

    droid2 = Robot('C-3PO')
    droid2.przywitajSie()
    Robot.jakDuzo()

    print ("\nUmówmy się, że roboty wykonują tutaj jakąś pracę.\n")

    print( "Roboty zakończyły swoje zadania, więc możemy się ich pozbyć.")
    del droid1
    del droid2

    Robot.jakDuzo()