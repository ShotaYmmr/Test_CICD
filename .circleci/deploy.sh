#!/bin/bash
TARGET_BRANCH=master

# clone repository
if [[ ! `ls | grep Hello-Automation-World-Product` ]]; then
    git clone -b $TARGET_BRANCH https://github.com/sendo111/Hello-Automation-World-Product.git
fi

# change working branch
cd Hello-Automation-World-Product

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
