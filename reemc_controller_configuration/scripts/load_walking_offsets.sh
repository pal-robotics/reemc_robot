#!/bin/bash



ROBOT_CONTROLLER_CONFIGURATION_DIR=`rospack find reemc_controller_configuration`/config

HOME_CONTROLLER_CONFIGURATION_DIR="$HOME/.pal/reemc_controller_configuration/config"

mkdir -p $HOME_CONTROLLER_CONFIGURATION_DIR

rosparam load $ROBOT_CONTROLLER_CONFIGURATION_DIR/offsets.yaml walking_controller/offsets

if [ -f $HOME_CONTROLLER_CONFIGURATION_DIR/offsets.yaml ]; then

rosparam load $HOME_CONTROLLER_CONFIGURATION_DIR/offsets.yaml walking_controller/offsets

fi



