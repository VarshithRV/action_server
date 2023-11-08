import rospy
import actionlib
from interruptible_action_server.msg import fibonacciAction, fibonacciGoal,fibonacciFeedback,fibonacciResult


if __name__ == "__main__":
    rospy.init_node("Fibonacci_client")
    action_client = actionlib.SimpleActionClient("fib_action",fibonacciAction) # create the client
    action_client.wait_for_server() # to connect the server
    rospy.loginfo("Server connected")
    # create a goal
    goal=fibonacciGoal()
    goal.order = 5
    # call the action
    action_client.send_goal(goal) # send the goal
    rospy.loginfo("Sent goal to the server")
    
    # action_client.wait_for_result(rospy.Duration.from_sec(5.0)) # wait for result
    
    rate=rospy.Rate(5)
    for i in range(5):
        rospy.loginfo(action_client.get_state())  # is this feedback or result?

        rate.sleep()
    # end the action
    action_client.cancel_goal()
    rospy.loginfo("Goal cancelled")
    # wait for result
    action_client.wait_for_result()
    rospy.loginfo("Received result from the server : ")
    rospy.loginfo(action_client.get_result()) # get the result