import rospy
import asyncio

from queue import LifoQueue

from std_msgs.msg import Boolean




class TimedMoveQueue(object):
	def __init__(self):
		self._queue = LifoQueue() # .get() .put( obj )


	def get_future_event(self, event):
		self._queue.put(event)

	async def publish_spin(self):
		controller_publisher = rospy.Publisher('MultiControllerState', jointAngleMessage, queue_size=4) 
		
		while self._queue.empty():
			pass
		
		#Send start to player --> Rethink right syncing!
		rospy.Publisher('StartMusic', Boolean, queue_size=1).publish(True);
		next_event_time = rospy.get_rostime()
		
		while not rospy.is_shutdown():
			while self._queue.empty() && not rospy.is_shutdown(): 
				pass
			
			while rospy.get_rostime() < next_event_time:
				pass
				
			event = self._queue.get()
			controller_publisher.publish(event.jointAngles)
			next_event_time += event.delta_time
			
			#Breakaway check --> stop message?
			
			if event.delta_time - 100 > 0:
				await asyncio.sleep(event.delta_time - 100)
			


if __name__ == '__main__':
    queue = TimedMoveQueue()
    rospy.Subscriber('StartMusic', deltaAngleMsg, queue.get_future_event)
    ayncio.run(queue.publish_spin())
    rospy.spin()  	
		
		
			
