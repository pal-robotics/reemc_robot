^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package reemc_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.10.10 (2016-12-12)
--------------------
* Fixed force torque sensor sign in hardware config
* Contributors: Hilario Tome

0.10.9 (2016-12-12)
-------------------

0.10.8 (2016-12-12)
-------------------

0.10.7 (2016-10-06)
-------------------

0.10.6 (2016-10-06)
-------------------

0.10.5 (2016-10-06)
-------------------
* 0.10.4
* Updated changelog
* Revert "0.10.4"
  This reverts commit cede99f356296d77bdbf004c5edf1231df637d62.
* Contributors: Hilario Tome

0.10.4 (2016-10-06)
-------------------
* Revert "0.10.4"
  This reverts commit cede99f356296d77bdbf004c5edf1231df637d62.
* Contributors: Hilario Tome

0.10.3 (2016-04-14)
-------------------

0.10.2 (2016-04-08)
-------------------
* Added linear acceleration and angular velocity ports
* Contributors: Hilario Tome

0.10.1 (2016-04-07)
-------------------
* Added support for joint mode in urdf transmissions, pal hardware config file and added configuration files for REEM-C4
* Contributors: Hilario Tome

0.10.0 (2016-04-04)
-------------------
* Fix real sensor measures for matching sensor frame axes
* Contributors: Luca Marchionni

0.9.11 (2016-03-04)
-------------------
* Fix tf frames for ft sensors in ankles and wrists
* Contributors: Luca Marchionni

0.9.10 (2015-10-08)
-------------------

0.9.9 (2015-10-06)
------------------

0.9.8 (2015-06-14)
------------------

0.9.7 (2015-06-10)
------------------
* Add configuration for ignoring read errors
* Contributors: Adolfo Rodriguez Tsouroukdissian

0.9.6 (2015-06-05)
------------------
* Fix and update motions to take into account Hey5 hand
* Make bringup fully aware of REEM-C variants
* Add ros_control_monitor in bringup
* Add current limit controllers to robot bringup
* Contributors: Adolfo Rodriguez, Adolfo Rodriguez Tsouroukdissian, Bence Magyar, Luca Marchionni, Sammy Pfeiffer

0.9.5 (2015-04-24)
------------------

0.9.4 (2015-04-08)
------------------

0.9.3 (2015-04-08)
------------------
* Add reemc_moveit_config dependency
* Contributors: Luca Marchionni

0.9.2 (2015-03-31)
------------------
* Fix indent typo and an error
* Now we always load the public motions first, then try to load the proprietary ones. Also updated some motions
* Adding the loading of motions depending on what motions are available in the workspace
* adds missed joy dependency
* fixes for twist_mux w/o imu ramp limit
* removes deprecated control_loop_frequency param
* Update play_motion config in robots. Refs #8652.
  Set new parameter for minimum unplanned approach duration.
* reemc_bringup: fix joystick mappings for motions
  refs #8527
* reemc_bringup: sync a few motions from reem_bringup
  Especially for the fingers.
  refs #8527
  Conflicts:
  reemc_bringup/config/reemc_motions.yaml
* merges joy_teleop scaling from SDE4 branch
  svn merge svn+ssh://server/srv/svn/repos/branches/4.1_REEMC_SDE4/pal-ros-pkg/catkin_pkgs/reemc_robot/reemc_bringup/config .
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
* added walk_pose to bringup and updated package dependencies
* added config and launch for walk_pose
* changes the joystick configuration so it doesn't do anything (no turbo)
* updates dependency on twist_mux (not pal_mobile_base)
* renames mobile_base launch into twist_mux
* renames config for twist_mux (from mobile_base)
* uses twist_mux
* refs #7535 : adds tf_lookup dependency
  NOTE previous commit was based on this:
  svn merge svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot/reemc_bringup -c -52271
* refs #7535 : sorry, tf_lookup is actually needed
* refs #7535 : removes tf_lookup (not needed) from the bringup
* refs #7535 : puts reemc_bringup launch here
* refs #7536 : adds pal_mobile_base dependency
  NOTE the pal_mobile_base should be renamed to twist_mux or similar
* refs #7536 : adds twist mux*
  * mobile base node at this moment
* Remove turbo and map joystick buttons to the 5 motions
  refs #7778
* Add 2 poses and 6 new motions to REEM-C
  Fixes #7528
* refs #7537 : adds joy priority and turbo actions
* Merge reemc_robot from OROCOS_2.X
* Catkininze reemc_bringup
* Update manifests with maintainer information
* Merge from OROCOS_2.X
* reemc_bringup: merge from OROCOS_2.X
* Merge from OROCOS_2.X
* Moved config files to bringup and eliminated duplicated launch file.
  Updated reemc_gazebo.launch to have everything necessary for sitting.
  Refs #6437
* Added chair sitting config files for play_motion and joystick shortcuts(only for testing).
  Refs #6437
* reemc_bringup: now contains play_motion and joy_teleop launchfiles
* Add joint trajectory controller groups for the whole body.
  Bring back the point head action.
* Correctly do bringup. PIDs were being left out.
* Create feature-limited reemc_hardware package and supporting infrastructure. Refs #5959.
* Contributors: Adolfo Rodriguez Tsouroukdissian, Bence Magyar, Enrique Fernandez, Luca Marchionni, Paul Mathieu, Sammy Pfeiffer, Victor Lopez
