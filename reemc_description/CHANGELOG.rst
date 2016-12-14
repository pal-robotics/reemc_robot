^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package reemc_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
