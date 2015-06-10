^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package reemc_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.9.7 (2015-06-10)
------------------

0.9.6 (2015-06-05)
------------------
* Set default robot to reemc_full_ft_hey5
* Add robot urdf file for tf and hey5. Modified ftsensor urdf
* Add ft sensor to the wrist and Hey5 hand
* Contributors: Luca Marchionni

0.9.5 (2015-04-24)
------------------

0.9.4 (2015-04-08)
------------------

0.9.3 (2015-04-08)
------------------

0.9.2 (2015-03-31)
------------------
* Updated max velocity limits and effort for the arms of reemc
* fixes identation
* removes trailing spaces
* refs #7536 : increases range from 4.0 to 5.6m
  NOTE the lasers has a firmware (SCIP 2.0) that support this extended range
* Updated copyrights
* Changed cfmDamping instances for implicitSpringDamper instances.
  The first one was deprecated, so we get rid of all the deprecated warnings
* Fix: Paths of the meshes were pointing to reem model not reemc model
* Spread change from REEM-H model: Changed the multiplier of the mimic joints of the finger so the movement of the active joint spreads corretly to the subactuated joints
* sets laser noise to 0.03m
  See:
  http://www.hokuyo-aut.jp/02sensor/07scanner/download/products/urg-04lx-ug01/data/URG-04LX_UG01_spec_en.pdf
  3. Specifications
  Accuracy
* merged hand description from rockin branch and fixed pids for underactuated joints.
  Increased torso max torque in urdf for simulating sitting.
* refs #7535 : fixes range sensors (was using laser plugin!)
* remove unused file. Fix small discrepancy between the specified hfov and the expected value in stereo and back camera.
* Merge reemc_description from OROCOS_2.X
* refs #7502. Fix REEM-C right camera placement in hydro_migration. Cherry picking from OROCOS_2.X revision 49210
* reemc_description: remove reemc namespace
* Catkinize reemc_description
* reemc_description: add reemc.urdf.xacro for compatibility
* reemc_description: remove a ew unused descriptions
* reemc_description: ftplugin not needed anymore
* reemc_description: implicitSpringDamper doesn't work yet
* reemc_description: hardware_interface goes in joint
* reemc_description: remove execution bit
* Move reemc_description to catkin reemc_robot
* Contributors: Enrique Fernandez, Hilario Tome, Jordi Pages, Luca Marchionni, Paul Mathieu, Sam Pfeiffer, Victor Lopez
