# django sample apps

# Run "docker network inspect bridge" and use the "IPAM/Config/Gateway" IP address for setting http/https proxy
docker-compose build --build-arg http_proxy=http://192.168.0.1:3128 --build-arg https_proxy=https://192.168.0.1:3128 nginx django_server
