^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package reemc_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------

1.0.2 (2018-06-19)
------------------

1.0.1 (2018-05-02)
------------------

1.0.0 (2018-01-26)
------------------
* Rm motions from three finger hand
* Contributors: Adrià Roig

0.10.18 (2017-12-04)
--------------------
* Remove ignore_read_errors
* Contributors: Victor Lopez

0.10.17 (2017-11-11)
--------------------
* Add motions for the humanoids demo
* Contributors: davidfernandez

0.10.16 (2017-05-15)
--------------------

0.10.15 (2017-03-27)
--------------------

0.10.14 (2017-03-27)
--------------------
* added config files for reemc no hands, and removed reemc three finger hand model
* Contributors: Hilario Tome

0.10.13 (2017-02-15)
--------------------

0.10.12 (2016-12-14)
--------------------
* Add walk_pose to default_controllers, instead of bringup
* Contributors: luca

0.10.11 (2016-12-13)
--------------------
* Merge branch 'dubnium-devel' of gitlab:robots/reemc_robot into dubnium-devel
* Updated changelog
* Updated walk pose
* Contributors: Hilario Tome

0.10.10 (2016-12-12 16:57)
--------------------------
* Updated changelog
* Fixed force torque sensor sign in hardware config
* Contributors: Hilario Tome

0.10.9 (2016-12-12 12:51)
-------------------------
* Updated changelog
* Contributors: Hilario Tome

0.10.8 (2016-12-12 12:18)
-------------------------
* Updated changelog
* Contributors: Hilario Tome

0.10.7 (2016-10-06 16:32)
-------------------------
* Updated changelog
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
* Revert "0.10.4"
  This reverts commit cede99f356296d77bdbf004c5edf1231df637d62.
* Contributors: Hilario Tome

0.10.4 (2016-04-18)
-------------------
* Update changelog
* Contributors: Sam Pfeiffer

0.10.3 (2016-04-14)
-------------------
* Updated changelog
* Contributors: Hilario Tome

0.10.2 (2016-04-08)
-------------------
* Updated changelog
* Added linear acceleration and angular velocity ports
* Contributors: Hilario Tome

0.10.1 (2016-04-07)
-------------------
* Updated changelogs
* Added support for joint mode in urdf transmissions, pal hardware config file and added configuration files for REEM-C4
* Contributors: Hilario Tome

0.10.0 (2016-04-04)
-------------------
* Updated changelogs
* Fix real sensor measures for matching sensor frame axes
* Contributors: Hilario Tome, Luca Marchionni

0.9.11 (2016-03-04)
-------------------
* Add changelog
* Fix tf frames for ft sensors in ankles and wrists
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
* Contributors: Luca Marchionni

0.9.7 (2015-06-10)
------------------
* Update changelogs
* Add configuration for ignoring read errors
* Contributors: Adolfo Rodriguez Tsouroukdissian

0.9.6 (2015-06-05)
------------------
* Update changelogs
* Make play_motion launch files aware of 'robot' arg
  Make approach_planner configuration compatible with REEM-C variants, and use the
  'robot' roslaunch argument to switch between them.
* Merge branch 'walk-pose-hey5' into 'cobalt-devel'
  Walk Pose Hey5
* Trivial motion description doc fix
* Fix broken 'hands_up' motion
  Was missing two left arm joints, which made play_motion (rightfully) choke on
  it while attempting to plan an approach trajectory, and reject it.
* Roslaunch 'robot' arg: default to 'full_ft_hey5'
  Previous default was 'full'.
* Add deployment files for 3 fingers or hey5 hand for walk_pose
* Removing test_motion as it was problematic and as per ticket https://redmine/issues/11157 it was not referenced anywhere
* Move 'interact' to public set of motions
  - Removed from reemc_robot_proprietary repo, and into this repo
* Fix broken full_ft_hey5 motions
  - home: Incorrect joint names and mismatching vector sizes
  - hands_up: self-colliding configuration
* Make bringup fully aware of REEM-C variants
  - Load robot-specific hardware configuration (formerly reemc_hardware driver)
  - Separate ROS param configuration of hand controllers from the main
  joint_trajectory_controller.yaml file. Correct hand controller configuration
  is loaded based on the robot launch argument.
  - Fix broken yaml spec of hey5 hand controllers.
  - Add simple grasping action to controller launch files.
* Pass robot arg to move group
* Setting default robot to full
* Preparing the pipeline to accept the robot argument
* Add ros_control_monitor in bringup
* Restore moveit_config and play_motion launches
* Comment motion planning launch in bringup because of errors due to hey5 integration
* Add current limit controllers to robot bringup
  Current limit controllers are only spawned when working with real hardware.
  They do not exist in simulated deployments.
  These controllers are spawned by default. No user action is required to bring
  them up.
* Contributors: Adolfo Rodriguez, Adolfo Rodriguez Tsouroukdissian, Bence Magyar, Luca Marchionni, Sammy Pfeiffer

0.9.5 (2015-04-24)
------------------
* Updated changelog
* Contributors: Hilario Tome

0.9.4 (2015-04-08 18:21)
------------------------
* Update changelog
* Contributors: Luca Marchionni

0.9.3 (2015-04-08 18:14)
------------------------
* Update changelog
* Add reemc_moveit_config dependency
* Contributors: Luca Marchionni

0.9.2 (2015-03-31)
------------------
* Add changelog
* Fix indent typo and an error
* Now we always load the public motions first, then try to load the proprietary ones. Also updated some motions
* Adding the loading of motions depending on what motions are available in the workspace
* adds missed joy dependency
* fixes for twist_mux w/o imu ramp limit
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@58127 5e370ff8-3418-0410-babe-3378cc20a00d
* removes deprecated control_loop_frequency param
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@58054 5e370ff8-3418-0410-babe-3378cc20a00d
* Update play_motion config in robots. Refs #8652.
  Set new parameter for minimum unplanned approach duration.
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@55944 5e370ff8-3418-0410-babe-3378cc20a00d
* git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@54190 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_bringup: fix joystick mappings for motions
  refs #8527
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@53518 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_bringup: sync a few motions from reem_bringup
  Especially for the fingers.
  refs #8527
  Conflicts:
  reemc_bringup/config/reemc_motions.yaml
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@53517 5e370ff8-3418-0410-babe-3378cc20a00d
* merges joy_teleop scaling from SDE4 branch
  svn merge svn+ssh://server/srv/svn/repos/branches/4.1_REEMC_SDE4/pal-ros-pkg/catkin_pkgs/reemc_robot/reemc_bringup/config .
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@53155 5e370ff8-3418-0410-babe-3378cc20a00d
* git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@53114 5e370ff8-3418-0410-babe-3378cc20a00d
* Transfer motions from REEM-H3. Refs #8124.
  The following motions have been transfered verbatim, replacing the adapted REEM-C
  ones that were there before (REEM-C specific motions like squat are still there):
  1.  arms_t
  2.  center_head
  3.  home
  4.  interact_to_rest
  5.  interact
  6.  joystick_open_arms
  7.  joystick_salute
  8.  joystick_shale_left
  9.  joystick_shake_right
  10. joystick_wave
  11. joystick_were_here
  12. no
  13. open_arms
  14. rest_to_interact
  15. salute
  16. shake_left
  17. shake_right
  18. wave
  19. were_here
  20. yes_fast
  21. yes
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52702 5e370ff8-3418-0410-babe-3378cc20a00d
* added walk_pose to bringup and updated package dependencies
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52609 5e370ff8-3418-0410-babe-3378cc20a00d
* added config and launch for walk_pose
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52608 5e370ff8-3418-0410-babe-3378cc20a00d
* changes the joystick configuration so it doesn't do anything (no turbo)
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52461 5e370ff8-3418-0410-babe-3378cc20a00d
* updates dependency on twist_mux (not pal_mobile_base)
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52443 5e370ff8-3418-0410-babe-3378cc20a00d
* renames mobile_base launch into twist_mux
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52324 5e370ff8-3418-0410-babe-3378cc20a00d
* renames config for twist_mux (from mobile_base)
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52321 5e370ff8-3418-0410-babe-3378cc20a00d
* uses twist_mux
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52320 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7535 : adds tf_lookup dependency
  NOTE previous commit was based on this:
  svn merge svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot/reemc_bringup -c -52271
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52274 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7535 : sorry, tf_lookup is actually needed
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52273 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7535 : removes tf_lookup (not needed) from the bringup
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52271 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7535 : puts reemc_bringup launch here
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52270 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7536 : adds pal_mobile_base dependency
  NOTE the pal_mobile_base should be renamed to twist_mux or similar
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52118 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7536 : adds twist mux*
  * mobile base node at this moment
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52116 5e370ff8-3418-0410-babe-3378cc20a00d
* Remove turbo and map joystick buttons to the 5 motions
  refs #7778
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@51778 5e370ff8-3418-0410-babe-3378cc20a00d
* Add 2 poses and 6 new motions to REEM-C
  Fixes #7528
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@51603 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7537 : adds joy priority and turbo actions
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@51080 5e370ff8-3418-0410-babe-3378cc20a00d
* Merge reemc_robot from OROCOS_2.X
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@49864 5e370ff8-3418-0410-babe-3378cc20a00d
* Catkininze reemc_bringup
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@48952 5e370ff8-3418-0410-babe-3378cc20a00d
* Update manifests with maintainer information
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@47601 5e370ff8-3418-0410-babe-3378cc20a00d
* git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@47342 5e370ff8-3418-0410-babe-3378cc20a00d
* Merge from OROCOS_2.X
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@46633 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_bringup: merge from OROCOS_2.X
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@46048 5e370ff8-3418-0410-babe-3378cc20a00d
* Merge from OROCOS_2.X
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/stacks/reemc_robot@46041 5e370ff8-3418-0410-babe-3378cc20a00d
* Moved config files to bringup and eliminated duplicated launch file.
  Updated reemc_gazebo.launch to have everything necessary for sitting.
  Refs #6437
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44909 5e370ff8-3418-0410-babe-3378cc20a00d
* Added chair sitting config files for play_motion and joystick shortcuts(only for testing).
  Refs #6437
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44896 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_bringup: now contains play_motion and joy_teleop launchfiles
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44837 5e370ff8-3418-0410-babe-3378cc20a00d
* Add joint trajectory controller groups for the whole body.
  Bring back the point head action.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@44206 5e370ff8-3418-0410-babe-3378cc20a00d
* Correctly do bringup. PIDs were being left out.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@43296 5e370ff8-3418-0410-babe-3378cc20a00d
* Create feature-limited reemc_hardware package and supporting infrastructure. Refs #5959.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/OROCOS_2.X/pal-ros-pkg/stacks/reemc_robot@42304 5e370ff8-3418-0410-babe-3378cc20a00d
* Contributors: Adolfo Rodriguez Tsouroukdissian, Bence Magyar, Enrique Fernandez, Luca Marchionni, Paul Mathieu, Sammy Pfeiffer, Victor Lopez, enriquefernandez, icarus
