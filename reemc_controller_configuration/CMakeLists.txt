cmake_minimum_required(VERSION 2.8.3)
project(reemc_controller_configuration)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir config launch)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)


install(PROGRAMS 
    scripts/load_walking_offsets.sh
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
