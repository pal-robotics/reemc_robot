^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package reemc_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
