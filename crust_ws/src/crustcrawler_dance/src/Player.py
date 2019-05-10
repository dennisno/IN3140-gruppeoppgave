#!/usr/bin/env python

from std_msgs.msg import String
from std_msgs.msg import Bool

from crustcrawler_dance.msg import MusicString
import rospy
import pyglet
import rospkg


#s_path = rospkg.RosPack().get_path('crustcrawler_dance') + "/music/Alan_Walker_Faded_uncompressed.wav" #LetItBe.wav"
#song = pyglet.resource.media(s_path)
song = None # pyglet.media.load(s_path)
offset = 0.0

def set_music(data):
    global song, offset
    rospy.loginfo("Player ready with: %s", data.file)
    song = pyglet.media.load(data.file) #pyglet.resource.media(data.file)
    offset = data.offset


def start_music(data):
    global song, offset
    rospy.loginfo(data.data)
    if not data.data:
        rospy.loginfo("Player: Wait command!")
        return
    if not song:
        rospy.logerr("Player: No music, unable to play!")
        return
    rospy.loginfo("Player: Starting to play Music!")
    rospy.sleep(offset)
    song.play()
    pyglet.app.run()

# ----------- INIT FUNCTION -----------
def listener():
    rospy.Subscriber('/player/set_music', MusicString, set_music)
    rospy.Subscriber('/player/start_music', Bool, start_music)
    rospy.spin()



if __name__ == '__main__':
	try:
		rospy.init_node('music',anonymous = True)
		listener()
	except rospy.ROSInterruptException:
		pass
