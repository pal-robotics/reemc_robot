^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package reemc_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.9.8 (2015-06-14)
------------------
* Increase tolerance for hey5 controllers
* Contributors: Luca Marchionni

0.9.7 (2015-06-10)
------------------
* Fix ft sensor name for init_offset controller
* Contributors: Luca Marchionni

0.9.6 (2015-06-05)
------------------
* Make bringup fully aware of REEM-C variants
* Add hey5 launch files for reemc
* Add configuration for hey5 in jtc
* Add ft sensor to the wrist and Hey5 hand
* Add current limit controllers to robot bringup
* Contributors: Adolfo Rodriguez Tsouroukdissian, Bence Magyar, Luca Marchionni

0.9.5 (2015-04-24)
------------------
* Added missing dependencty imu controller and force torque controller
* Contributors: Hilario Tome

0.9.4 (2015-04-08)
------------------
* Add head_action dependency
* Contributors: Luca Marchionni

0.9.3 (2015-04-08)
------------------

0.9.2 (2015-03-31)
------------------
* added offsets for reemc-3 (legs soft offsets)
* Change reem_head_action with head_action and fix deps
* Extend config files for switch to handle lists
  Refs #9845
* Adding launch and config files for joint mode switches
  Refs #9845
* adds enabled param to odometry and moves odometry related params to 'odometry' ns
* removed line probably due to a wrong merge
* Added config and launch for homing controller
* added run dependency on reemc_init_offset_controller.
  closes #8800
* removes trailing spaces
* syncs with 4.1_REEMC_SDE4 (disables walking controller on the startup)
  svn merge svn+ssh://server/srv/svn/repos/branches/4.1_REEMC_SDE4/pal-ros-pkg/catkin_pkgs/reemc_robot/reemc_controller_configuration .
* Added timeout option to default_controllers
* Set REEM-C offsets for reemc2 by default
  Refs #8347
* adding different joint offsets for rc1 and rc2
* reemc_controller_configuration: fix controller name
* reemc_controller_configuration: load full-body joint list in launch file
  This is so because we want to be able to alternate from
  lowerbody only to full body walking controller.
* Add lower body walking controller from COSMOCAIXA branch
  Merged it with upper body joint trajectory controller launch file
* refs #7537 : adds covariance params
* refs #7537 : adds use_imu_yaw and odom_pub_rate params (for REEM-C)
* reemc_controller_configuration: walking->walking_controller
* Catkinize reemc_controller_configuration
* Merge reemc_robot from 3.6_REEMC_SDE3
* Merge from OROCOS_2.X
* Update manifests with maintainer information
* Merge from OROCOS_2.X
* reemc_controller_configuration: start manipulation controllers by
  default
* renamed test walking controler to squat_controller
* Re-enable manipulation controller loading.
* Temporarily remove loading of upper body controllers, as REEM-B chokes on this.
* Added manipulation controllers to default controllers
  Refs #6206
* changed namespace for biped_controller parameters (on reemc)
* changed namespace for parameters used for walking component on real robot
* Added hand controllers to Gazebo, will have to change it to real robot params once that part of ros_control is done.
  Refs #6212
* removed commented walking controller from reemc default controllers
* fixed parameter typo.
* Add joint trajectory controller groups for the whole body.
  Bring back the point head action.
* changed launch file for real reemc to load parameters in walking_controller namespace
* adding parameters for walking in a separated yaml file
* Refactored walking controller (got rid of virtual functions no longer needed).
  Encapsulated functions into an object used by ros_control walking plugin.
* added params for z com and ft sensor z for real robot
* Walking refactored with dynamic_reconfigure parameters.
  Added launch files for walking with different parameters on real and simulated robot.
* Fix dependency in reemc_controller_configuration
* walking ros_control tested on simulation.
  Sometimes eigen error occurs : http://eigen.tuxfamily.org/dox-devel/TopicUnalignedArrayAssert.html
* Load force-torque and IMU state publishers by default. Refs #5977.
* Create feature-limited reemc_hardware package and supporting infrastructure. Refs #5959.
* Contributors: Adolfo Rodriguez Tsouroukdissian, Bence Magyar, Enrique Fernandez, Luca Marchionni, Paul Mathieu, Victor Lopez
