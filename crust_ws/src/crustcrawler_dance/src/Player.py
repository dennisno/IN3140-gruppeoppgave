#!/usr/bin/env python

from std_msgs.msg import Float32
from std_msgs.msg import String
from std_msgs.msg import Bool
import rospy
import pyglet


global music = ""


def callback(data):
    rospy.loginfo(data.data)
    music = data.data

def start_music(data):
    rospy.loginfo(data.data)
    play_music(data.data)


def listener():
    rospy.init_node('music')
    rospy.Subscriber('MusicPub', String, callback)
    rospy.spin()
    rospy.init_node('start music')
    rospy.Subscriber('StartMusic', Bool, start_music)
    rospy.spin()

def play_music(start):
    while not start:
        playmusic = pyglet.resource.media(music)
        playmusic.play()
        pyglet.app.run()

if __name__ == '__main__':
    listener()
