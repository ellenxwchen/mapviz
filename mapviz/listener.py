#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

def callback(data):
    x=data.pose.pose.position.x
    y=data.pose.pose.position.y
    orientation_z=data.pose.pose.orientation.z

    rospy.loginfo('x: {}, y:{}, orientation_z:{},' .format(x,y, orientation_z))

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('odometry', anonymous=True)

    rospy.Subscriber("ins", Odometry, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()