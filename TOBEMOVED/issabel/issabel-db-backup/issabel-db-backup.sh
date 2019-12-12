#! /bin/bash

# Backup the Issabel databases.
#
# I wrote this because Issabel's own backups was given us a lot of 
# issues. It currently does what I need of it. The day new requirements
# come up, I will update this. Until then it probably stays the way it is.
#
# NOTE: this script assumes that the environment variable $destination
# exists in the script's execution context, so it is a good idea to 
# make sure it is set.
#
# Author: Lorenzo Cabrini <lorenzo.cabrini@gmail.com>

databases="asterisk asteriskcdrdb call_center endpointconfig qstats"
mysqluser=root
mysqlpass=$(cat /etc/issabel.conf | grep ^mysqlrootpwd | cut -d'=' -f2)
tmpdir=$(mktemp -d tmp.db_backup.XXXXXXX)
backupname=issabel-db-backup-$(date +"%Y%m%d-%H%M")
backup_count=20
tarname=$backupname.tar.gz
destination=$ISSABEL_BACKUP_DIRECTORY
if [[ -z $destination ]]; then
    destination=/backup/database
fi

# TODO: there are issues that could happen here, such as $destination
# exists but it is a file. Check for these as well.
if [[ ! -d $destination ]]; then
    mkdir -p $destination
fi

cd $tmpdir
mkdir $backupname
for db in $databases; do
    mysqldump -u $mysqluser -p"$mysqlpass" $db > $backupname/$db.sql    
done

tar zcf $tarname $backupname
mv $tarname $destination
cd
rm -rf $tmpdir

cd $destination
backups=$(ls *.tar.gz | wc -l)
if [[ $backups -gt $backup_count ]]; then
    rm $(ls | head -n $(($backups - $backups_count)))
fi
