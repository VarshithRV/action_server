import rospy
import actionlib
from interruptible_action_server.msg import basic_actionAction

class basic_server :
    def __init__ (self): # set and start server for action
        self.server = actionlib.SimpleActionServer("do_action1", basic_actionAction, self.execute, False)
        self.server.start()

    def execute(self, goal):
        rospy.loginfo("Executing shit")
        self.server.set_succeeded()


if __name__=="__main__":
    rospy.init_node("basic_server")
    server = basic_server()
    rospy.spin()


# questions that needs to be asked

# 1. how to send feed back, and where to send it?
# 2. how to get the result and where to get it?
# 3. how to start it, track it and end it if its necessary?
# 4. how to encrypt the signals? 
# 5. can multiple clients connect to a single server?
# 6. how to see all the action servers that are currently active?
# 7. can a single server work on multiple clients connected?