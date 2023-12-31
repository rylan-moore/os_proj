#
# Makefile that downloads data files
#

#
# You should be able to download or access the datafiles using the link 
#     https://drive.google.com/drive/folders/1LtCL6YW-W3Ug3KAvo0gbHC3mdRXawGuo?usp=sharing
# this will show them to you in Google Drive.
#
# Alternatively, you can use the git repo at https://github.com/cu-csci-4253-datacenter/lab3-hadoop-join-patent-data
#
# The following make rules download from the git repo
#
VERSION=v1
DOCKERUSER=rylanm14

get:	cite75_99.txt.gz apat63_99.txt.gz

cite75_99.txt.gz:
	wget 'https://github.com/cu-csci-4253-datacenter/lab4-pyspark-patent-data/raw/master/cite75_99.txt.gz'

apat63_99.txt.gz:
	wget 'https://github.com/cu-csci-4253-datacenter/lab4-pyspark-patent-data/raw/master/apat63_99.txt.gz'

docker_build:
	sudo docker build -f Dockerfile -t spark-server .

docker_tag:
	sudo docker tag spark-server $(DOCKERUSER)/spark-server:latest
docker_push:
	sudo docker push $(DOCKERUSER)/spark-server:latest

docker_manager:
	sudo docker run --restart always -d -p 9005:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:linux-arm
