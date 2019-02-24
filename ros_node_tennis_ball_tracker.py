import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

bridge = CvBridge()

def image_callback(ros_image):
	print("Got an image")
	global bridge 
	#convert ros_image into an opencv-compatible image
	try:
		cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
	except CvBridgeError as e:
		print(e)
	#from now on, you can work exactly like with opencv

	cv2.imshow("Image window", cv_image)
	cv2.waitKey(3)

def main(args):
	rospy.init_node('image_converter', anonymous=True)

	image_sub = rospy.Subscriber("/camera/rgb/image_raw/", Image, imge_callback)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()

if __name++ == '__main__':
	main(sys.argv)

	