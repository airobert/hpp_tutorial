#Robert White
#LAAS-CNRS
#gepetto-viewer-server
#hppcorbaserver


# two robots in the environment trying to find a path each with no collision
from hpp.corbaserver.pr2 import Robot
robot1 = Robot ('1')
robot1.setJointBounds ("base_joint_xy", [-4, -3, -5, -3])

robot2 = Robot ('2')
robot2.setJointBounds ("base_joint_xy", [-4, -3, -5, -3])

robot3 = Robot ('3')
robot3.setJointBounds ("base_joint_xy", [-4, -3, -5, -3])

from hpp.corbaserver import ProblemSolver
ps1 = ProblemSolver (robot1)
ps2 = ProblemSolver (robot2)
ps3 = ProblemSolver (robot3)

from hpp.gepetto import ViewerFactory
vf1 = ViewerFactory (ps1)
vf2 = ViewerFactory (ps2)
vf3 = ViewerFactory (ps3)

robot1_q_init = robot1.getCurrentConfig ()
robot2_q_init = robot2.getCurrentConfig ()
robot3_q_init = robot3.getCurrentConfig ()

r1 = vf1.createViewer()
r2 = vf2.createViewer()
r3 = vf3.createViewer()

robot2_q_init [0:2] = [-3.2, -4]
robot3_q_init [0:2] = [3.2, -4]

r1(robot1_q_init)
r2(robot2_q_init)
r3(robot3_q_init)

robot2_q_goal = robot2_q_init

robot2_q_goal [0:2] = [-3.2, -4]
rank = robot2.rankInConfiguration ['l_shoulder_lift_joint']
robot2_q_goal [rank] = 0.5
rank = robot2.rankInConfiguration ['l_elbow_flex_joint']
robot2_q_goal [rank] = -0.5
rank = robot2.rankInConfiguration ['r_shoulder_lift_joint']
robot2_q_goal [rank] = 0.5
rank = robot2.rankInConfiguration ['r_elbow_flex_joint']
robot2_q_goal [rank] = -0.5

robot3_q_goal = robot3_q_init

robot3_q_goal [0:2] = [3.2, -4]
rank = robot3.rankInConfiguration ['l_shoulder_lift_joint']
robot3_q_goal [rank] = -0.5
rank = robot3.rankInConfiguration ['l_elbow_flex_joint']
robot3_q_goal [rank] = 0.5
rank = robot3.rankInConfiguration ['r_shoulder_lift_joint']
robot3_q_goal [rank] = 0.5
rank = robot3.rankInConfiguration ['r_elbow_flex_joint']
robot3_q_goal [rank] = -0.5

r2(robot2_q_goal)
r3(robot3_q_goal)



        ## Draws robot configuration, along with octrees associated
        #
    # \param viewer gepetto viewer instance
    def draw(self, configuration, viewer):
        viewer(configuration)
        for limb, groupid in self.octrees.iteritems():
                transform = self.client.rbprm.rbprm.getOctreeTransform(limb,
configuration)
                viewer.client.gui.applyConfiguration(groupid,transform)
        viewer.client.gui.refresh()
