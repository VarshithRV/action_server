# client for the factorial action

import rospy, actionlib
from interruptible_action_server.msg import factorialAction, factorialGoal, factorialFeedback, factorialResult

if __name__=="__main__":
    rospy.init_node("factorial_client")
    
    goal = factorialGoal()# create a goal
    goal.order=8
    
    factorial_client=actionlib.SimpleActionClient("factorial_action",factorialAction)# create the client
    
    factorial_client.wait_for_server()# wait for connection
    rospy.loginfo("Server connected")
    
    factorial_client.send_goal(goal)#send the goal and call the task
    
    # monitor the task for 2 seconds
    rate=rospy.Rate(2)
    for i in range(5):
        rospy.loginfo(factorial_client.get_goal_status_text())
        # rospy.loginfo(factorial_client.get_state())
        # rospy.loginfo(factorial_client.get_result())
        rate.sleep()
    
    # interrupt the task, query status
    factorial_client.cancel_goal()
    rospy.loginfo("Task Interrupted by the client")
    rospy.loginfo(factorial_client.get_goal_status_text())
    