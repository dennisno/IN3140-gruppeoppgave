<<<<<<< HEAD
#!/usr/bin/env python


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
    #rospy.spin()
    #rospy.init_node('start music')
    rospy.Subscriber('StartMusic', Bool, start_music)
    rospy.spin()

def play_music(start):
    while not start:
        playmusic = pyglet.resource.media(music)
        playmusic.play()
        pyglet.app.run()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
=======
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
    if not data.data:
		return
	if not music:
		rospy.logerr("No music, unable to play!")
		return
    playmusic = pyglet.resource.media(music)
    playmusic.play()
    pyglet.app.run()

# ----------- INIT FUNCTION -----------
def listener():
    rospy.Subscriber('MusicPub', String, callback)
    #rospy.spin()
    #rospy.init_node('start music')
    rospy.Subscriber('StartMusic', Bool, start_music)
    rospy.spin()

        

if __name__ == '__main__':
    try:
		rospy.init_node('music')
        listener()
    except rospy.ROSInterruptException:
        pass
>>>>>>> 183d3175de9819a77c7a56e6811d3ca3d36176b2
