# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time

package = 'com.yahoo.mobile.client.android.ecstore'
activity = 'com.yahoo.mobile.client.android.ecstore.ui.ECSplashActivity'
interval = 1
intervals = 8
x = 304
y = 1051

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# sets the name of the component to start
runComponent = package + '/' + activity
integer = 0

while integer <= 1000:
    integer = integer + 1
    print(">>>>>>>>>>Time:" + str(integer))
    # Runs the component
    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(intervals)
    # Presses the myaccount 
    device.touch(1287,2469,"DOWN_AND_UP")
    MonkeyRunner.sleep(intervals)
    # Presses mobileappstore2 
    device.touch(814,490,"DOWN_AND_UP")
    MonkeyRunner.sleep(intervals)
    # Presses logout 
    device.touch(697,581,"DOWN_AND_UP")
    MonkeyRunner.sleep(10)
    # Presses confirm 
    device.touch(999,1594,"DOWN_AND_UP")
    MonkeyRunner.sleep(intervals)
    
