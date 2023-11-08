# action to get the factorial of a number

import rospy, actionlib
from interruptible_action_server.msg import factorialAction, factorialGoal, factorialFeedback, factorialResult


def factorial(goal:factorialGoal):
    rospy.loginfo("Finding the factorial")
    
    success=True # Initialize variables for feedback and result to be sent
    n=goal.order
    feedback=factorialFeedback()
    result=factorialResult
    fact=1
    rate=rospy.Rate(1)

    for i in range(1,n+1):
        if action.is_preempt_requested(): # detect and handle the preemtive shutdown if provided
            rospy.loginfo("Task aborted")
            action.set_preempted()
            return

        fact*=i
        feedback.current_factorial=fact
        feedback.current_order=i
        rospy.loginfo(feedback)
        action.publish_feedback(feedback) # publish feedback every iteration
        rate.sleep()

    result.factorial=fact
    action.set_succeeded(result) # return result to the client


if __name__=="__main__":
    rospy.init_node("factorial_server")
    action = actionlib.SimpleActionServer("factorial_action",factorialAction,factorial,False) # initialize the action
    # connect the action with the task=factorial
    action.start() # start the server
    rospy.spin() # suspend the thread and keep the server running