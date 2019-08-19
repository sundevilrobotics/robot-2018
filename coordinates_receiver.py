#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_receive_coordinates(msg):
	rospy.loginfo("Coordinates received: ")
	rospy.loginfo(msg)

# generic name, change it to whatever is relevant
rospy.init_node("coordinate_receiver", anonymous=True)

# parameters are: topic to subscribe to, message type, function to plug message into
sub = rospy.Subscriber("/coordinates", String, callback_receive_coordinates)

rospy.spin()    # rospy.spin() is different from 'not while rospy.is_shutdown' ...
					# it is basically the same thing but it does more
					# it keeps the node alive AND checks for callbacks

					# sudo code for rospy.spin() is as follows
					# while not rospy.is_shutdown():
						# check for messages received over topics and other stuff
						# call callbacks related to received messages 