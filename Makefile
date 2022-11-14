include docker/.env
build:
	docker build -t deepsmash/libultimate:latest -f docker/Dockerfile . --build-arg NVIDIA_DRIVER_VERSION=${NVIDIA_DRIVER_VERSION} --build-arg VNC_PASSWORD=${VNC_PASSWORD}
run:
	docker-compose -f docker/docker-compose.yml --env-file ./docker/.env up -d
remove:
	docker-compose -f docker/docker-compose.yml --env-file ./docker/.env down
