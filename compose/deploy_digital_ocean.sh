#! /bin/bash

# Make sure ssh private key has been added before running this script
# e.g.: eval `ssh-agent -s`
#       ssh-add ~/.ssh/do_consort_rsa

# This shell script quickly deploys your project to your
# DigitalOcean Droplet

if [ -z "$DIGITAL_OCEAN_IP_ADDRESS" ]
then
    echo "DIGITAL_OCEAN_IP_ADDRESS not defined"
    exit 0
fi

# generate TAR file from git
git archive --format tar --output ./project.tar main

echo 'Uploading project...'
rsync ./project.tar root@$DIGITAL_OCEAN_IP_ADDRESS:/tmp/project.tar
echo 'Uploaded complete.'

echo 'Building image...'
ssh -o StrictHostKeyChecking=no root@$DIGITAL_OCEAN_IP_ADDRESS << 'ENDSSH'
    mkdir -p /app
    rm -rf /app/* && tar -xf /tmp/project.tar -C /app
    docker compose -f /app/docker-compose.prod.yml -p consort_production build
    supervisorctl restart consort-app
ENDSSH
echo 'Build complete.'
