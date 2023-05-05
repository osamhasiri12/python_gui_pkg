import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import tkinter as tk

class GoalPublisher(Node):

    def __init__(self):
        super().__init__('goal_publisher')
        self.publisher_ = self.create_publisher(PoseStamped, '/goal_pose', 10)

        self.room1_pose = PoseStamped()
        self.room1_pose.header.frame_id = 'map'
        self.room1_pose.pose.position.x = 0.0
        self.room1_pose.pose.position.y = 0.0
        self.room1_pose.pose.orientation.w = 1.0

        self.room2_pose = PoseStamped()
        self.room2_pose.header.frame_id = 'map'
        self.room2_pose.pose.position.x = 0.821746
        self.room2_pose.pose.position.y = -2.27052
        self.room2_pose.pose.orientation.w = 1.0

        self.room3_pose = PoseStamped()
        self.room3_pose.header.frame_id = 'map'
        self.room3_pose.pose.position.x = 0.0
        self.room3_pose.pose.position.y = 0.0
        self.room3_pose.pose.orientation.w = 1.0

    def publish_goal(self, goal_pose):
        self.publisher_.publish(goal_pose)

class GoalPublisherGUI(tk.Tk):

    def __init__(self, goal_publisher):
        super().__init__()

        self.goal_publisher = goal_publisher

        self.title('Goal Publisher')
        self.configure(bg='white')
        self.geometry('400x400') 

        room1_button = tk.Button(self, text='Room 1', command=self.publish_room1, bg='aquamarine3', fg='white', font=('Arial', 20), height=2, width=10)
        room1_button.pack(pady=10)
        room1_button.place(x=25,y=100)

        room2_button = tk.Button(self, text='Room 2', command=self.publish_room2, bg='aquamarine3', fg='white', font=('Arial', 20), height=2, width=10)
        room2_button.pack(pady=10)
        room2_button.place(x=100,y=25)

        room3_button = tk.Button(self, text='Room 3', command=self.publish_room3, bg='aquamarine3', fg='white', font=('Arial', 20), height=2, width=10)
        room3_button.pack(pady=10)
        room3_button.place(x=200,y=100)
        
        exit_button = tk.Button(self, text="Exit", command=exit,bg='red', fg='white', font=('Arial', 20), height=2, width=10)
        exit_button.pack(pady=10)
        exit_button.place(x=100,y=225)
        
    def publish_room1(self):
        self.goal_publisher.publish_goal(self.goal_publisher.room1_pose)

    def publish_room2(self):
        self.goal_publisher.publish_goal(self.goal_publisher.room2_pose)

    def publish_room3(self):
        self.goal_publisher.publish_goal(self.goal_publisher.room3_pose)

def main(args=None):
    rclpy.init(args=args)

    goal_publisher = GoalPublisher()

    gui = GoalPublisherGUI(goal_publisher)
    gui.mainloop()

    rclpy.shutdown()

if __name__ == '__main__':
    main()