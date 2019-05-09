#!/usr/bin/env python


from std_msgs.msg import Float32
from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import UInt32

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
    rospy.loginfo("Found a total of %s beats", len(shorted_down_beat_frame) )
    rospy.loginfo('MusicPub: %s', song_path)  

	max_points = rospy.Publisher("/planner/controller_max_points", UInt32, queue_size=2)
	max_points.publish( len(shorted_down_beat_frame) )
	max_points.publish( len(shorted_down_beat_frame) )
	
	music_start = rospy.Publisher('/player/start_music', Bool, queue_size=2)
    music_start.publish(False)
    music_start.publish(False)
    
    set_music = rospy.Publisher('/player/set_music', String, queue_size=2)
    set_music.publish(song_path)
    set_music.publish(song_path)
    
    i = 0    
    r = rospy.Rate(100) # Hz
    pub = rospy.Publisher('/planner/delta_beat', Float32, queue_size = 100)
    while not rospy.is_shutdown():
        time_of_beat = (shorted_down_beat_frame[i+1] - shorted_down_beat_frame[i]) * 2
        i += 1
        rospy.loginfo("Delta_beat: %s", time_of_beat )
        pub.publish(time_of_beat)
        r.sleep()

if __name__ == '__main__':
    try:
		rospy.init_node('publishmusic',anonymous = True)
		talker()
    except rospy.ROSInterruptException:
        pass
    except IndexError:
	rospy.loginfo("All beats done!")
