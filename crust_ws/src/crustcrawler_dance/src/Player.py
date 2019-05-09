#!/usr/bin/env python

from std_msgs.msg import String
from std_msgs.msg import Bool
import rospy
import pyglet
import rospkg


s_path = rospkg.RosPack().get_path('crustcrawler_dance') + "/music/Alan_Walker_Faded_uncompressed.wav" #LetItBe.wav"
#song = pyglet.resource.media(s_path)
song = pyglet.media.load(s_path)

def set_song(data):
    global song
    rospy.loginfo("Player ready with: %s", data.data)
    song = pyglet.resource.media(data.data)


def start_music(data):
    global song
    rospy.loginfo(data.data)
    if not data.data:
        rospy.loginfo("Player: Wait command!")
        return
    if not song:
        rospy.logerr("Player: No music, unable to play!")
        return
    rospy.loginfo("Player: Starting to play Music!")
    song.play()
    pyglet.app.run()

# ----------- INIT FUNCTION -----------
def listener():
    rospy.Subscriber('/MusicPub', String, set_song)
    rospy.Subscriber('/StartMusic', Bool, start_music)
    rospy.spin()



if __name__ == '__main__':
    try:
	rospy.init_node('music')
        listener()
    except rospy.ROSInterruptException:
        pass
