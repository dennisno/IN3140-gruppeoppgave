#!/usr/bin/env python

from std_msgs.msg import Int32
from std_msgs.msg import String
import rospy
import pyglet


music = ""


pyglet.app.run()

def callback(data):
    rospy.loginfo(data)
    music = data

def listener():
    rospy.init_node('music')
    rospy.Subscriber('MusicPub', String, callback)
    pub = rospy.Publisher('sync', Int32, queue_size = 100)
    play_music()
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rospy.loginfo()
        pub.publish()
        rate.sleep()

def play_music():
    playmusic = pyglet.resource.media(music)
    playmusic.play()

if __name__ == '__main__':
    listener()
