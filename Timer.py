 # import the time module
import time
dilation = 2

# define the countdown func.
def countdown(t):
	print()

	while t:
		Rmins, Rsecs = divmod(t, 60)
		Rtimer = '{:02d}:{:02d}'.format(Rmins, Rsecs)
		Gmins, Gsecs = divmod(t//dilation, 60)
		Gtimer = '{:02d}:{:02d}'.format(Gmins, Gsecs)
		print("Game Time:", Gtimer, "     ", "Real Time:", Rtimer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('               Time\'s up               ')


# input time in seconds
t = dilation*int(input("Enter the time in seconds: "))

# function call
countdown(t)