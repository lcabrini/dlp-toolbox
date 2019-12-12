#! /bin/bash

# This sets up issabel-utils. Simply run this script.
#
# Author: Lorenzo Cabrini <lorenzo.cabrini@gmail.com>

gitrepo=https://github.com/lcabrini/issabel-utils.git
gitdir=/usr/local/git/
repodir=$gitdir/issabel-utils

which git >> /dev/null 2>&1
if [[ $? -ge 1 ]]; then
    yum install -y git
    if [[ $? -ge 1 ]]; then
        printf "Cannot install git. Aborting"
        exit 1
    fi
fi

if [[ ! -d $gitdir ]]; then
    mkdir -p $gitdir
fi

if [[ ! -d $repodir ]]; then
    cd $gitdir
    git clone $gitrepo
    cd $repodir
else
    cd $repodir
    git pull
fi

make
