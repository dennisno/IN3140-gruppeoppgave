#!/usr/bin/env python


from std_msgs.msg import Float32
from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import UInt32

from crustcrawler_dance.msg import MusicString

import rospkg
import rospy
import librosa

music_filepath = rospkg.RosPack().get_path('crustcrawler_dance') + "/music/"

def read_beat(filename):

    y, sr = librosa.load(filename)
    #    Load the audio as a waveform `y`
    #    Store the sampling rate as `sr`

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    return tempo, beat_frames 

# ----------- INIT FUNCTION -----------
def talker():
    global music_filepath
    song_path = music_filepath + "Alan_Walker_Faded_uncompressed.wav" #'LetItBe.wav'
    
    tempo, beat_frames = read_beat(song_path)
    shorted_down_beat_frame = beat_frames #[::2]
    num_beats = len(shorted_down_beat_frame)
    rospy.loginfo("Found a total of %s beats", num_beats )
    rospy.loginfo('MusicPub: %s', song_path)
    
    # Setting the number of expected messages in the 'path_planner' node
    pub = rospy.Publisher("/planner/controller_max_points", UInt32, queue_size=1)
    while pub.get_num_connections() is 0:
		rospy.sleep(1)
    msg = UInt32()
    msg.data = num_beats
    pub.publish( msg )
        
    # Really not needed, just an extra check to see if we got connection to the 'player' node
    pub = rospy.Publisher('/player/start_music', Bool, queue_size=1)
    while pub.get_num_connections() is 0:
		rospy.sleep(1)
    msg = Bool()
    msg.data = False
    pub.publish( msg )
    
    # Setting the song in the 'player' node
    pub = rospy.Publisher('/player/set_music', MusicString, queue_size=1)
    while pub.get_num_connections() is 0:
		rospy.sleep(1)
    msg = MusicString()
    msg.file = song_path
    pub.publish( msg )
    
    # Starting to send messages down the message chain: this > point_2_point > inverse_kinematics > path_planner
    i = 0    
    r = rospy.Rate(30) # Hz
    pub = rospy.Publisher('/planner/delta_beat', Float32, queue_size = 100)
    while pub.get_num_connections() is 0:
		rospy.sleep(1)
    while not rospy.is_shutdown():
        time_of_beat = (shorted_down_beat_frame[i+1] - shorted_down_beat_frame[i]) * 2
        i += 1
        rospy.loginfo("Sending beat: %s / %s, Duration: %s", i+1, num_beats, time_of_beat )
        pub.publish(time_of_beat)
        r.sleep()

if __name__ == '__main__':
	try:
		rospy.init_node('publish_music',anonymous = True)
		talker()
	except rospy.ROSInterruptException:
		pass
	except IndexError:
		rospy.loginfo("All beats done!")
