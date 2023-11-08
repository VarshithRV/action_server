# the task accepts the order (goal) gives feedback as the as the array where fibonacci is stored
# result is true or false indicating completion or interruption and the fib(order)

import rospy
import actionlib
from interruptible_action_server.msg import fibonacciAction, fibonacciResult, fibonacciGoal, fibonacciFeedback

def task(goal:fibonacciGoal):
    # display the fib(order) keep giving feedback
    # after completion, indicate the completion
    rospy.loginfo("Task started")
    rate = rospy.Rate(1)
    
    order = goal.order
    feedback = fibonacciFeedback()
    result=fibonacciResult()
    result.completion=False
    
    feedback.sequence.append(0)
    feedback.sequence.append(1)
    

    for i in range(2,int(order)): # write a way to interrupt the task
        if action_server.is_preempt_requested():
            rospy.loginfo("Task interrupted")
            action_server.set_preempted()
            return
        feedback.sequence.append(feedback.sequence[i-1]+feedback.sequence[i-2])
        action_server.publish_feedback(feedback) #publish the feedback
        rospy.loginfo(feedback)
        rate.sleep()

    
    result.completion=True #contains the completion 
    result.result=feedback.sequence[order-1] #contains the final value
    action_server.set_succeeded(result) #publish the result
    rospy.loginfo(result)


if __name__=="__main__":
    rospy.init_node("fibonacci_action_server")
    action_server = actionlib.SimpleActionServer("fib_action",fibonacciAction,task,False)
    action_server.start()
    rospy.loginfo("Action server started")
    rospy.spin()


# how to send the goal and feedback?
# how to view the goal 
# how to interrupt the task?
# how to wait for results or feedback?

# How to view feedback?
# what does get_state do?
# how to encrypt the signals?
# can more than one clients call the same service (with the same name)?
# if more than one client can call the same service can call the action, then 
# will the server be able to handle concurrent requests?
# how to monitor all active actions and extract information from them?