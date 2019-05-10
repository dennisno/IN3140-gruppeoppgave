#!/usr/bin/env python

from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import Float32


from crustcrawler_dance.msg import MusicString
import rospy
import pyglet
import rospkg


song = None
offset = 0.0
tick = rospy.Publisher('/planner/tick', Float32, queue_size = 50)

def set_music(data):
    global song, offset, tick
    rospy.loginfo("Player ready with: %s", data.file)
    song = pyglet.media.load(data.file) #pyglet.resource.media(data.file)
    offset = data.offset
    while tick.get_num_connections() is 0:
		rospy.sleep(0.5)


def start_music(data):
    global song, offset, tick
    rospy.loginfo(data.data)
    if not data.data:
        rospy.loginfo("Player: Wait command!")
        return
    if not song:
        rospy.logerr("Player: No music, unable to play!")
        return
    rospy.loginfo("Player: Starting to play Music!")
    tick.publish(data=-1.0) # just to start to print messages to logout...
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
