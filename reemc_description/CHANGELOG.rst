^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package reemc_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.0.16 (2021-11-17)
-------------------
* Merge branch 'set_nominal_extrinsics_param' into 'erbium-devel'
  added the use_nominal_extrinsics parameter to true for head_version V1
  See merge request robots/reemc_robot!33
* added the use_nominal_extrinsics parameter to true for head_version V1
* Contributors: Adria Roig, Sai Kishor Kothakota

1.0.15 (2021-09-17)
-------------------
* Merge branch 'gallium_fixes' into 'erbium-devel'
  Gallium fixes
  See merge request robots/reemc_robot!32
* Use pi instead of M_PI
* Added missing xacro tags
* Use xacro command
* Contributors: Jordan Palacios

1.0.14 (2021-08-31)
-------------------

Forthcoming
-----------
* Merge branch 'fix_stereo_camera_link' into 'erbium-devel'
  fix the stereo optical camera link origin
  See merge request robots/reemc_robot!34
* fix the stereo optical camera link origin
* Contributors: Sai Kishor Kothakota, saikishor

1.0.17 (2021-11-22)
-------------------
* 1.0.16
* Update Changelog
* Merge branch 'set_nominal_extrinsics_param' into 'erbium-devel'
  added the use_nominal_extrinsics parameter to true for head_version V1
  See merge request robots/reemc_robot!33
* added the use_nominal_extrinsics parameter to true for head_version V1
* 1.0.15
* Updated changelogs
* Merge branch 'gallium_fixes' into 'erbium-devel'
  Gallium fixes
  See merge request robots/reemc_robot!32
* Use pi instead of M_PI
* Added missing xacro tags
* Use xacro command
* 1.0.14
* Updated Changelog
* Contributors: Adria Roig, Jordan Palacios, Sai Kishor Kothakota, Victor Lopez

1.0.13 (2020-01-07)
-------------------
* Merge branch 'softlimit_fixes' into 'erbium-devel'
  update the soft limits of all joints
  See merge request robots/reemc_robot!27
* update the soft limits of all joints
* Contributors: Sai Kishor Kothakota, Victor Lopez

1.0.12 (2020-01-07)
-------------------

1.0.11 (2019-12-10)
-------------------
* Merge branch 'realsense_description' into 'erbium-devel'
  added URDF from realsense2_description and its dependency
  See merge request robots/reemc_robot!30
* added URDF from realsense2_description and its dependency
* Contributors: Sai Kishor Kothakota, Victor Lopez

1.0.10 (2019-10-30)
-------------------
* Merge branch 'realsense_plugin_macro_fix' into 'erbium-devel'
  realsense gazebo plugin macro fix
  See merge request robots/reemc_robot!28
* realsense gazebo plugin macro fix
* Contributors: Adria Roig, Sai Kishor Kothakota

1.0.9 (2019-08-22)
------------------

1.0.8 (2019-07-02)
------------------
* Merge branch 'reemc_head_leg_v0_and_v1' into 'erbium-devel'
  Adding legs v0,v1 specs and setting default version for leg and head to v0 for back-compatibility
  See merge request robots/reemc_robot!25
* Adding legs v0,v1 specs and setting default version for leg and head to v0 for back-compatibility
* Contributors: Luca Marchionni, Victor Lopez

1.0.7 (2019-03-14)
------------------

1.0.6 (2019-03-13)
------------------
* Merge branch 'realsense' into 'erbium-devel'
  Add realsense camera
  See merge request robots/reemc_robot!22
* Add generic camera frame
* Modified tests for REEM-C new version
* Update the rest of the robot files with the new head version
* Add realsense camera
* Contributors: Adria Roig, Victor Lopez

1.0.5 (2019-03-07)
------------------
* Merge branch 'merge-from-github' into 'erbium-devel'
  Switch Y_UP to Z_UP for all up_axis field of the meshes.
  See merge request robots/reemc_robot!20
* Switch Y_UP to Z_UP for all up_axis field of the meshes.
  Y_UP introduces a transform between the original geometry of the body.
  Rviz is explicitly removing this transform, see
  https://github.com/ros-visualization/rviz/blob/8a010bbda36d425129dc06887eddcab032459319/src/rviz/mesh_loader.cpp#L233
  Signed-off-by: Hilario Tome <hilario.tome@pal-robotics.com>
* Contributors: Olivier Stasse, Victor Lopez

1.0.4 (2018-12-12)
------------------

1.0.3 (2018-07-04)
------------------

1.0.2 (2018-06-19)
------------------

1.0.1 (2018-05-02)
------------------
* Merge branch 'test_urdf' of gitlab:robots/reemc_robot into erbium-devel
* Add tests for additional URDF files
* Test URDF file
* Contributors: Hilario Tome, davidfernandez

1.0.0 (2018-01-26)
------------------

0.10.18 (2017-12-04)
--------------------

0.10.17 (2017-11-11)
--------------------

0.10.16 (2017-05-15)
--------------------

0.10.15 (2017-03-27)
--------------------
* deleted broken link
* Contributors: Hilario Tome

0.10.14 (2017-03-27)
--------------------
* added config files for reemc no hands, and removed reemc three finger hand model
* Contributors: Hilario Tome

0.10.13 (2017-02-15)
--------------------
* robot specification fixes
* Contributors: Hilario Tome

0.10.12 (2016-12-14)
--------------------

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
* Added reemc specifics to walking params, and reverted torso to revolute joint
* Revert "0.10.4"
  This reverts commit cede99f356296d77bdbf004c5edf1231df637d62.
* Replaced hands with boxes
* Contributors: Alexander, Hilario Tome

0.10.4 (2016-04-18)
-------------------
* Update changelog
* Contributors: Sam Pfeiffer

0.10.3 (2016-04-14)
-------------------
* Updated changelog
* Changed robot hardware sim type to pal hardware gazebo
* Contributors: Hilario Tome

0.10.2 (2016-04-08)
-------------------
* Updated changelog
* Contributors: Hilario Tome

0.10.1 (2016-04-07)
-------------------
* Updated changelogs
* Added support for joint mode in urdf transmissions, pal hardware config file and added configuration files for REEM-C4
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
* Use custom head transmission.
  Tilt joint position limits depend on actual pan joint position.
  Refs #9907.
* Contributors: Adolfo Rodriguez Tsouroukdissian

0.9.9 (2015-10-06)
------------------
* Update changelog
* Changed min joint ankle y limit to -75
* Contributors: Luca Marchionni, Víctor López

0.9.8 (2015-06-14)
------------------
* Add changelog
* Contributors: Luca Marchionni

0.9.7 (2015-06-10)
------------------
* Update changelogs
* Contributors: Adolfo Rodriguez Tsouroukdissian

0.9.6 (2015-06-05)
------------------
* Update changelogs
* Parametrized wrist joint 6 limit to support different joint limits on reemc with ft sensor
* Added nice spacewq
* Remove comments
* Set default robot to reemc_full_ft_hey5.
* Add robot urdf file for tf and hey5. Modified ftsensor urdf
* Add ft sensor to the wrist and Hey5 hand
* Remove comments
* Set default robot to reemc_full_ft_hey5.
* Add robot urdf file for tf and hey5. Modified ftsensor urdf
* Add ft sensor to the wrist and Hey5 hand
* Contributors: Adolfo Rodriguez Tsouroukdissian, Bence Magyar, Luca Marchionni

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
* Contributors: Luca Marchionni

0.9.2 (2015-03-31)
------------------
* Add changelog
* Updated max velocity limits and effort for the arms of reemc
* git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@54190 5e370ff8-3418-0410-babe-3378cc20a00d
* fixes identation
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@53484 5e370ff8-3418-0410-babe-3378cc20a00d
* removes trailing spaces
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52768 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7536 : increases range from 4.0 to 5.6m
  NOTE the lasers has a firmware (SCIP 2.0) that support this extended range
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52544 5e370ff8-3418-0410-babe-3378cc20a00d
* Updated copyrights
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52367 5e370ff8-3418-0410-babe-3378cc20a00d
* Changed cfmDamping instances for implicitSpringDamper instances.
  The first one was deprecated, so we get rid of all the deprecated warnings
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52256 5e370ff8-3418-0410-babe-3378cc20a00d
* Fix: Paths of the meshes were pointing to reem model not reemc model
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52210 5e370ff8-3418-0410-babe-3378cc20a00d
* Spread change from REEM-H model: Changed the multiplier of the mimic joints of the finger so the movement of the active joint spreads corretly to the subactuated joints
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@52205 5e370ff8-3418-0410-babe-3378cc20a00d
* sets laser noise to 0.03m
  See:
  http://www.hokuyo-aut.jp/02sensor/07scanner/download/products/urg-04lx-ug01/data/URG-04LX_UG01_spec_en.pdf
  3. Specifications
  Accuracy
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@51904 5e370ff8-3418-0410-babe-3378cc20a00d
* merged hand description from rockin branch and fixed pids for underactuated joints.
  Increased torso max torque in urdf for simulating sitting.
  git-svn-id: svn+ssh://server/srv/svn/repos/trunk/pal-ros-pkg/catkin_pkgs/reemc_robot@51087 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7535 : fixes range sensors (was using laser plugin!)
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@50462 5e370ff8-3418-0410-babe-3378cc20a00d
* remove unused file. Fix small discrepancy between the specified hfov and the expected value in stereo and back camera.
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@50419 5e370ff8-3418-0410-babe-3378cc20a00d
* Merge reemc_description from OROCOS_2.X
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@49866 5e370ff8-3418-0410-babe-3378cc20a00d
* refs #7502. Fix REEM-C right camera placement in hydro_migration. Cherry picking from OROCOS_2.X revision 49210
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@49247 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_description: remove reemc namespace
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@49130 5e370ff8-3418-0410-babe-3378cc20a00d
* Catkinize reemc_description
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@48961 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_description: add reemc.urdf.xacro for compatibility
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@48960 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_description: remove a ew unused descriptions
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@48959 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_description: ftplugin not needed anymore
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@48958 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_description: implicitSpringDamper doesn't work yet
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@48957 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_description: hardware_interface goes in joint
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@48956 5e370ff8-3418-0410-babe-3378cc20a00d
* reemc_description: remove execution bit
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@48954 5e370ff8-3418-0410-babe-3378cc20a00d
* Move reemc_description to catkin reemc_robot
  git-svn-id: svn+ssh://server/srv/svn/repos/branches/hydro_migration/pal-ros-pkg/catkin_pkgs/reemc_robot@48918 5e370ff8-3418-0410-babe-3378cc20a00d
* Contributors: Enrique Fernandez, Hilario Tome, Jordi Pages, Luca Marchionni, Paul Mathieu, Sam Pfeiffer, Victor Lopez
