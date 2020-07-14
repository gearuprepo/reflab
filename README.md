# reflab


# Removing container with given name
#docker ps -a | awk '{ print $1,$2 }' | grep ngui | awk '{print $1 }' | xargs -I {} | docker rm -f {}