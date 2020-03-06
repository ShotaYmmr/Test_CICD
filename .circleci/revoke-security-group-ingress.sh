#!/bin/sh
REGION=$1
SECURITY_GROUP=$2

IP=`curl -s ifconfig.me`
echo "#!/bin/bash" > ./sg.sh
echo "aws configure set region ${REGION}" >> ./sg.sh
echo "aws ec2 revoke-security-group-ingress --group-id ${SECURITY_GROUP} --protocol tcp --port 22 --cidr ${IP}/32" >> ./sg.sh
bash ./sg.sh
