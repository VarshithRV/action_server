# README

Created a basic action server and client using rospy on ros noetic<br>
The server node : factorial_server.py<br>
The client node : factorial_client.py<br>
Task : finds x! given x, using a simple loop, has a frequency of 1 for convenience of testing.<br>
Action file : factorial.action<br>
    goal.msg -> uint32 order <br>    
    result.msg->uint32 factorial <br>   
    feedback.msg -> uint32 current_factorial, uint32 current_order<br>
    
<i>The client is written so that the task isn't completed to test the safe interruptibility.</i>

### Steps : 
1. Add actionlib_msgs as build and exec dependencies for the package in the manifest.
2. Create ./action/factorial.action file, build it.
3. Write a server function code that handles preemptive interruption, publishes feedback messages and the result at the completion of the task.
4. Create a simple action server instance using actionlib, connecting the action identifier, action message (factorial.action) and task. Start the action, keep the loop busy with rospy.spin().
5. Write a client, using an instance of the actionlib.SimpleActionClient object with the same action identifier and action message type. 
6. Wait for connection with server, query status of execution, result.
7. Purposefully cancel the goal to activate the pre-emptive interruption handle in the server that aborts the task and cleans up.
8. Encryption can be done using the middleware encryption services provided by ros2 foxy, however this has not been implemented yet.

### Application : 
1. Developing an event based interface for control of robots in real time.