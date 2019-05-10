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
    rospy.is_shutdown() # Call to stop sigterm errors
    #    Load the audio as a waveform `y`
    #    Store the sampling rate as `sr`

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    rospy.is_shutdown() # Call to stop sigterm errors
    #	beat_frames is not actually timed events, 
    #	but a more accurate format to represent this kind of measurements
    
    beat_seconds = librosa.core.frames_to_time(beat_frames, sr=sr)
    rospy.is_shutdown() # Call to stop sigterm errors
    #	beat_seconds is the actuall time of the beat
    #	given in seconds from the start
    
    return beat_seconds

# ----------- INIT FUNCTION -----------
def talker():
	global music_filepath
	song_path = music_filepath + "Alan_Walker_Faded_uncompressed.wav" #'LetItBe.wav'
	r = rospy.Rate(25) # Hz
	song_offset = 2.0 # in seconds!
	
	beat_seconds = read_beat(song_path)
	rospy.is_shutdown() # Call to stop sigterm errors
	selected_beat_seconds = beat_seconds #[::2]
	num_beats = len(selected_beat_seconds)
	rospy.loginfo("Found a total of %s beats", num_beats )
	rospy.loginfo('MusicPub: %s', song_path)
	
	# Setting the number of expected messages in the 'path_planner' node
	pub = rospy.Publisher("/planner/controller_max_points", UInt32, queue_size=1)
	while pub.get_num_connections() is 0:
		r.sleep()
	msg = UInt32()
	msg.data = num_beats
	pub.publish( msg )
	
	# Really not needed, just an extra check to see if we got connection to the 'player' node
	pub = rospy.Publisher('/player/start_music', Bool, queue_size=1)
	while pub.get_num_connections() is 0:
		r.sleep()
	msg = Bool()
	msg.data = False
	pub.publish( msg )
	
	# Setting the song in the 'player' node
	pub = rospy.Publisher('/player/set_music', MusicString, queue_size=1)
	while pub.get_num_connections() is 0:
		r.sleep()
	msg = MusicString()
	msg.file = song_path
	msg.offset = song_offset
	pub.publish( msg )
	
	# Starting to send messages down the message chain: this > point_2_point > inverse_kinematics > path_planner
	pub = rospy.Publisher('/planner/delta_beat', Float32, queue_size = 50)
	while pub.get_num_connections() is 0:
		r.sleep()
	
	tick = rospy.Publisher('/planner/tick', Float32, queue_size = 50)
	while tick.get_num_connections() is 0:
		r.sleep()
	
	pub.publish(data=song_offset) #First beat should happen instantly?! >> Predetermined delay?
	tick.publish(data=song_offset)
	r.sleep()
	i = 1
	while not rospy.is_shutdown() and i < num_beats:
		time_of_beat = (selected_beat_seconds[i] - selected_beat_seconds[i-1])
		i += 1
		rospy.loginfo("Sending beat: %s / %s, Duration: %s", i+1, num_beats, time_of_beat )
		pub.publish(data=time_of_beat)
		tick.publish(data=time_of_beat)
		r.sleep()
	
	rospy.loginfo("All beats done!")
	

if __name__ == '__main__':
	try:
		rospy.init_node('publish_music',anonymous = True)
		talker()
	except rospy.ROSInterruptException:
		pass
