
from std_msgs.msg import int32
import rospy
import librosa


def read_beat(self, filename):

    y, sr = librosa.load(filename)
    #    Load the audio as a waveform `y`
    #    Store the sampling rate as `sr`

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    return tempo, beat_frames

def talker():
    pub = rospy.Publisher('BeatPlanPub', int32, queue_size = 10)
    rospy.init_node('talker', anonymous = True)
    rate = rospy.Rate(10)
    tempo, beat_frames = read_beat('LetItBe.wav')
    i = 0
    while not rospy.is_shutdown():
        time_of_beat = beat_frames[i]
        i += 1
        rospy.loginfo(time_of_beat)
        pub.publish(time_of_beat)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
