cmake_minimum_required(VERSION 2.8.3)
project(reemc_controller_configuration_reemc_1)


find_package(catkin REQUIRED)


###################################
## catkin specific configuration ##
###################################
catkin_package()


#############
## Install ##
#############
install(DIRECTORY config
    DESTINATION ${CATKIN_GLOBAL_SHARE_DESTINATION}/reemc_controller_configuration)
