#!/usr/bin/env python
from xml.etree import ElementPath
import rospy
from inertial_sense_ros.msg import GPS
import gps_common.msg
import random 
import math

global turning, num
turning = [60,55,57,53,51,48,46,30,39,37,36,35,34,33]
num = 0
last_num = 180
var_neg = 20
var_pos = 20
direction = 1
count = 0
global_count = 0

def callback(data):
    x=data.latitude
    y=data.longitude
    z=data.altitude

    # rospy.loginfo('x: {}, y:{}, z:{},' .format(x,y, z))

def convert_msg(data):
    
    global turning, num, last_num, var_neg, var_pos, direction,count, global_count
    count += 1
    global_count += 1
    if count == 5000:
        if (global_count > 19340000 and global_count <309800000)  or global_count > 5009000000:
            var_neg = 30
            var_pos = 10
        elif global_count > 309800000:
            var_pos = 30
            var_neg = 10
        x=data.latitude
        y=data.longitude
        z=data.altitude


        new_message = gps_common.msg.GPSFix()
        new_message.latitude=data.latitude
        new_message.longitude=data.longitude
        new_message.altitude=data.altitude

        new_message.pitch = (random.randint(0,360))
        new_message.roll = (random.randint(0,360))
        new_message.dip = (random.randint(0,360))
        new_message.track = random.randrange(last_num - var_neg, last_num + var_pos)
        last_num = new_message.track
        # if num == len(turning) - 1:
        #     num = 0
        # new_message.track = math.degrees(math.acos((data.velEcef.x) / (data.velEcef.y)))

        # rospy.loginfo("pitch is changing")
        # rospy.loginfo('x: {}, y:{}, z:{},' .format(data.posEcef.x,data.posEcef.y, data.posEcef.z))
        rospy.loginfo('track: {}' .format(new_message.track))
    
        pub = rospy.Publisher('gps_converted', gps_common.msg.GPSFix, queue_size=10)
        pub.publish(new_message)
        count = 0

    # rospy.loginfo('x: {}, y:{}, z:{},' .format(x,y, z))


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('gps_new_node', anonymous=True)

    rospy.Subscriber("gps", GPS, convert_msg)

    # spin() simply keeps python from exiting until this node is stopped
    # rospy.spin()

# def publisher():
    # pub = rospy.Publisher('gps_converted', gps_common.msg.GPSFix, queue_size=10)
    # pub.publish(new_message)
    # rospy.init_node('node_name')
    # r = rospy.Rate(10) # 10hz

# if __name__ == '__main__':
while not rospy.is_shutdown():
    listener()
    r=rospy.Rate(0.00000001)
    # publisher()