#!/usr/bin/env python3

# this line now prompts the user for input
ipchk = input("Apply an IP address: ")


# if user set IP of gateway
if ipchk == "192.168.70.1":
    # not recommended IP address
    print("Looks like the IP address of the Gateway was set: " +ipchk + " This is not recommended.")
elif ipchk:
    print("Looks like the IP address was set: " +ipchk) # data that was input by user
else: 
    print("You did not provide input.")  # if data was not provided
