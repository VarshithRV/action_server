import rospy
import actionlib
from interruptible_action_server.msg import basic_actionGoal,basic_actionResult, basic_actionFeedback, basic_actionAction



if __name__=="__main__":
    rospy.init_node("Client")
    n=1
    client=actionlib.SimpleActionClient(f"do_action{n}",basic_actionAction)
    client.wait_for_server()
    rospy.loginfo("Server connected")

    goal=basic_actionGoal()
    goal.goal=1
    client.send_goal(goal)
    rospy.loginfo("Sent goal to the server")
    client.wait_for_result(rospy.Duration.from_sec(5.0))
    rospy.loginfo("Received result from the server")
