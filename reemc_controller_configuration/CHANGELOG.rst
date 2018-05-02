^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package reemc_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* Merge branch 'local_control' into 'erbium-devel'
  Local control
  See merge request robots/reemc_robot!16
* Typo
* Add local control files
* Contributors: Adria Roig, Hilario Tome

1.0.0 (2018-01-26)
------------------
* Remove offsets from previous reemc
* Activate odom in walking params
* modified params in init_offset_controller.yaml
* Remove offsets from previous reemc
* Activate odom in walking params
* modified params in init_offset_controller.yaml
* Contributors: Adrià Roig

0.10.18 (2017-12-04)
--------------------

0.10.17 (2017-11-11)
--------------------

0.10.16 (2017-05-15)
--------------------

0.10.15 (2017-03-27)
--------------------

0.10.14 (2017-03-27)
--------------------

0.10.13 (2017-02-15)
--------------------
* robot specification fixes
* Fix walk_pose launch
* Contributors: Hilario Tome, luca

0.10.12 (2016-12-14)
--------------------
* Add walk_pose to default_controllers, instead of bringup
* Contributors: luca

0.10.11 (2016-12-13)
--------------------
* Merge branch 'dubnium-devel' of gitlab:robots/reemc_robot into dubnium-devel
* Updated changelog
* Contributors: Hilario Tome

0.10.10 (2016-12-12 16:57)
--------------------------
* Updated changelog
* Contributors: Hilario Tome

0.10.9 (2016-12-12 12:51)
-------------------------
* Updated changelog
* Contributors: Hilario Tome

0.10.8 (2016-12-12 12:18)
-------------------------
* Updated changelog
* Updated walking params
* Fixed walking params error
* Modified reemc controller params
* Contributors: Hilario Tome

0.10.7 (2016-10-06 16:32)
-------------------------
* Updated changelog
* Fixed typo
* Contributors: Hilario Tome

0.10.6 (2016-10-06 16:09)
-------------------------
* Updated changelog
* Contributors: Hilario Tome

0.10.5 (2016-10-06 12:12)
-------------------------
* Updated changelog
* 0.10.4
* Updated changelog
* Added reemc specifics to walking params, and reverted torso to revolute joint
* Revert "0.10.4"
  This reverts commit cede99f356296d77bdbf004c5edf1231df637d62.
* Contributors: Hilario Tome

0.10.4 (2016-04-18)
-------------------
* Update changelog
* Point to correct config file
* Contributors: Sam Pfeiffer

0.10.3 (2016-04-14)
-------------------
* Updated changelog
* Contributors: Hilario Tome

0.10.2 (2016-04-08)
-------------------
* Updated changelog
* Contributors: Hilario Tome

0.10.1 (2016-04-07)
-------------------
* Updated changelogs
* Contributors: Hilario Tome

0.10.0 (2016-04-04)
-------------------
* Updated changelogs
* Contributors: Hilario Tome

0.9.11 (2016-03-04)
-------------------
* Add changelog
* Contributors: Luca Marchionni

0.9.10 (2015-10-08)
-------------------
* Update changelog
* Contributors: Adolfo Rodriguez Tsouroukdissian

0.9.9 (2015-10-06)
------------------
* Update changelog
* Contributors: Víctor López

0.9.8 (2015-06-14)
------------------
* Add changelog
* Increase tolerance for hey5 controllers
* Contributors: Luca Marchionni

0.9.7 (2015-06-10)
------------------
* Update changelogs
* Fix ft sensor name for init_offset controller
* Contributors: Adolfo Rodriguez Tsouroukdissian, Luca Marchionni

0.9.6 (2015-06-05)
------------------
* Update changelogs
* Loading offsets for walking from .pal if they have been overwritten
* Make bringup fully aware of REEM-C variants
  - Load robot-specific hardware configuration (formerly reemc_hardware driver)
  - Separate ROS param configuration of hand controllers from the main
  joint_trajectory_controller.yaml file. Correct hand controller configuration
  is loaded based on the robot launch argument.
  - Fix broken yaml spec of hey5 hand controllers.
  - Add simple grasping action to controller launch files.
* revert joint_trajectory_controller to 3 finger hand version
* Add hey5 launch files for reemc
* Add configuration for hey5 in jtc
* Add ft sensor to the wrist and Hey5 hand
* Add configuration for hey5 in jtc
* Add ft sensor to the wrist and Hey5 hand
* Add current limit controllers to robot bringup
  Current limit controllers are only spawned when working with real hardware.
  They do not exist in simulated deployments.
  These controllers are spawned by default. No user action is required to bring
  them up.
* Contributors: Adolfo Rodriguez Tsouroukdissian, Bence Magyar, Luca Marchionni

0.9.5 (2015-04-24)
------------------
* Updated changelog
* Added missing dependencty imu controller and force torque controller
* Contributors: Hilario Tome

0.9.4 (2015-04-08 18:21)
------------------------
* Update changelog
* Add head_action dependency
* Contributors: Luca Marchionni

0.9.3 (2015-04-08 18:14)
------------------------
* Update changelog
* Contributors: Luca Marchionni

0.9.2 (2015-03-31)
------------------
* Add changelog
* added offsets for reemc-3 (legs soft offsets)
* Change reem_head_action with head_action and fix deps
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@58015 5e370ff8-3418-0410-babe-3378cc20a00d
* Extend config files for switch to handle lists
  Refs #9845
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@57686 5e370ff8-3418-0410-babe-3378cc20a00d
* Adding launch and config files for joint mode switches
  Refs #9845
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@57591 5e370ff8-3418-0410-babe-3378cc20a00d
* adds enabled param to odometry and moves odometry related params to 'odometry' ns
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@56837 5e370ff8-3418-0410-babe-3378cc20a00d
* removed line probably due to a wrong merge
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@56576 5e370ff8-3418-0410-babe-3378cc20a00d
* Added config and launch for homing controller
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@54756 5e370ff8-3418-0410-babe-3378cc20a00d
* added run dependency on reemc_init_offset_controller.
  closes #8800
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@54703 5e370ff8-3418-0410-babe-3378cc20a00d
* git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@54190 5e370ff8-3418-0410-babe-3378cc20a00d
* removes trailing spaces
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@54167 5e370ff8-3418-0410-babe-3378cc20a00d
* syncs with 4.1_REEMC_SDE4 (disables walking controller on the startup)
  svn merge svn+ssh://server/srv/svn/repos/branches/4.1_REEMC_SDE4/pal-ros-pkg/catkin_pkgs/reemc_robot/reemc_controller_configuration .
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@53121 5e370ff8-3418-0410-babe-3378cc20a00d
* syncs with 4.1_REEMC_SDE4
  svn merge svn+ssh://server/srv/svn/repos/branches/4.1_REEMC_SDE4/pal-ros-pkg/catkin_pkgs/reemc_robot/reemc_controller_configuration .
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@53116 5e370ff8-3418-0410-babe-3378cc20a00d
* Added timeout option to default_controllers
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52828 5e370ff8-3418-0410-babe-3378cc20a00d
* Set REEM-C offsets for reemc2 by default
  Refs #8347
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52570 5e370ff8-3418-0410-babe-3378cc20a00d
* adding different joint offsets for rc1 and rc2
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52478 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_controller_configuration: fix controller name
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@51797 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_controller_configuration: load full-body joint list in launch file
  This is so because we want to be able to alternate from
  lowerbody only to full body walking controller.
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@51796 5e370ff8-3418-0410-babe-3378cc20a00d
* Add lower body walking controller from COSMOCAIXA branch
  Merged it with upper body joint trajectory controller launch file
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@51795 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7537 : adds covariance params
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@50933 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7537 : adds use_imu_yaw and odom_pub_rate params (for REEM-C)
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@50894 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_controller_configuration: walking->walking_controller
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@49128 5e370ff8-3418-0410-babe-3378cc20a00d
* Catkinize reemc_controller_configuration
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@48953 5e370ff8-3418-0410-babe-3378cc20a00d
* Merge reemc_robot from 3.6_REEMC_SDE3
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@48649 5e370ff8-3418-0410-babe-3378cc20a00d
* Merge from OROCOS_2.X
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@48584 5e370ff8-3418-0410-babe-3378cc20a00d
* Update manifests with maintainer information
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@47601 5e370ff8-3418-0410-babe-3378cc20a00d
* git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@47342 5e370ff8-3418-0410-babe-3378cc20a00d
* Merge from OROCOS_2.X
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@46633 5e370ff8-3418-0410-babe-3378cc20a00d
* Merge from OROCOS_2.X
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@46411 5e370ff8-3418-0410-babe-3378cc20a00d
* Merge from OROCOS_2.X
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@46156 5e370ff8-3418-0410-babe-3378cc20a00d
* Merge from OROCOS_2.X
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@46041 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_controller_configuration: start manipulation controllers by
  default
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@46012 5e370ff8-3418-0410-babe-3378cc20a00d
* renamed test walking controler to squat_controller
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@45060 5e370ff8-3418-0410-babe-3378cc20a00d
* Re-enable manipulation controller loading.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44690 5e370ff8-3418-0410-babe-3378cc20a00d
* Temporarily remove loading of upper body controllers, as REEM-B chokes on this.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44585 5e370ff8-3418-0410-babe-3378cc20a00d
* Added manipulation controllers to default controllers
  Refs #6206
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44557 5e370ff8-3418-0410-babe-3378cc20a00d
* changed namespace for biped_controller parameters (on reemc)
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44376 5e370ff8-3418-0410-babe-3378cc20a00d
* changed namespace for parameters used for walking component on real robot
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44370 5e370ff8-3418-0410-babe-3378cc20a00d
* Added hand controllers to Gazebo, will have to change it to real robot params once that part of ros_control is done.
  Refs #6212
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44342 5e370ff8-3418-0410-babe-3378cc20a00d
* removed commented walking controller from reemc default controllers
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44304 5e370ff8-3418-0410-babe-3378cc20a00d
* fixed parameter typo.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44275 5e370ff8-3418-0410-babe-3378cc20a00d
* Add joint trajectory controller groups for the whole body.
  Bring back the point head action.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44206 5e370ff8-3418-0410-babe-3378cc20a00d
* changed launch file for real reemc to load parameters in walking_controller namespace
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44134 5e370ff8-3418-0410-babe-3378cc20a00d
* adding parameters for walking in a separated yaml file
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44133 5e370ff8-3418-0410-babe-3378cc20a00d
* Refactored walking controller (got rid of virtual functions no longer needed).
  Encapsulated functions into an object used by ros_control walking plugin.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44114 5e370ff8-3418-0410-babe-3378cc20a00d
* added params for z com and ft sensor z for real robot
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44055 5e370ff8-3418-0410-babe-3378cc20a00d
* Walking refactored with dynamic_reconfigure parameters.
  Added launch files for walking with different parameters on real and simulated robot.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44016 5e370ff8-3418-0410-babe-3378cc20a00d
* Fix dependency in reemc_controller_configuration
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@43826 5e370ff8-3418-0410-babe-3378cc20a00d
* walking ros_control tested on simulation.
  Sometimes eigen error occurs : http://eigen.tuxfamily.org/dox-devel/TopicUnalignedArrayAssert.html
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@43358 5e370ff8-3418-0410-babe-3378cc20a00d
* Load force-torque and IMU state publishers by default. Refs #5977.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@42398 5e370ff8-3418-0410-babe-3378cc20a00d
* Create feature-limited reemc_hardware package and supporting infrastructure. Refs #5959.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@42304 5e370ff8-3418-0410-babe-3378cc20a00d
* Contributors: Adolfo Rodriguez Tsouroukdissian, Bence Magyar, Enrique Fernandez, Luca Marchionni, Paul Mathieu, Victor Lopez, lucamarchionni
