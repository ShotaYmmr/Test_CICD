#!/bin/bash
TARGET_BRANCH=master

# clone repository
if [[ ! `ls | grep Test_CICD` ]]; then
    git clone -b $TARGET_BRANCH https://github.com/ShotaYmmr/Test_CICD.git 
fi

# change working branch
cd Test_CICD

# get remote diff
git fetch origin

# check current branch
CURRENT_BRANCH=`git branch --contains`
if [[ ! $CURRENT_BRANCH ]]; then
    git checkout $TARGET_BRANCH
fi

# update source
git pull origin $TARGET_BRANCH

# stop docker-compose if it is running
if [[ `ls | grep docker-compose.yml` && `sudo docker-compose ps -q | wc -l` > 0 ]] ; then 
    sudo docker-compose down
fi

# start docker-compose
sudo docker-compose up -d --build
