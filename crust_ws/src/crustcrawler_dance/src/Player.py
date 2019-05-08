#!/usr/bin/env python

from std_msgs.msg import String
from std_msgs.msg import Bool
import rospy
import pyglet



song = None

def callback(data):
    global song
    rospy.loginfo("Player ready with: %s", data.data)
    song = pyglet.resource.media(data.data)


def start_music(data):
    global song
    rospy.loginfo(data.data)
    if not data.data:
        rospy.loginfo("Player got False Start command!")
        return
    if not song:
        rospy.logerr("No music, unable to play!")
        return
    rospy.loginfo("Starting to play Music!")
    song.play()
    pyglet.app.run()

# ----------- INIT FUNCTION -----------
def listener():
    rospy.Subscriber('MusicPub', String, callback)
    rospy.Subscriber('StartMusic', Bool, start_music)
    rospy.spin()



if __name__ == '__main__':
    try:
	rospy.init_node('music')
        listener()
    except rospy.ROSInterruptException:
        pass
