#!/usr/bin/env python


from std_msgs.msg import Float32
from std_msgs.msg import String
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
    publish = rospy.Publisher('MusicPub', String, queue_size = 1)
    rospy.loginfo('MusicPub')
    publish.publish('LetItBe.wav')
    pub = rospy.Publisher('BeatPlanPub', Float32, queue_size = 100)
    #rospy.init_node('talker', anonymous = True)
    rate = rospy.Rate(10)
    tempo, beat_frames = read_beat(music_filepath + 'LetItBe.wav')
    i = 0
    shorted_down_beat_frame = beat_frames[::2]
    while not rospy.is_shutdown():
        time_of_beat = shorted_down_beat_frame[i+1] - shorted_down_beat_frame[i]
        i += 1
        rospy.loginfo("D_beat " + str(time_of_beat))
        pub.publish(time_of_beat)
        rate.sleep()

if __name__ == '__main__':
    try:
	rospy.init_node('publishmusic',anonymous = True)
        talker()
    except rospy.ROSInterruptException:
        pass
    except IndexError:
	rospy.loginfo("All beats done!")
