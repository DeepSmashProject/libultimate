include docker/.env
build:
	docker build -t deepsmash/libultimate:latest -f docker/Dockerfile . --build-arg NVIDIA_DRIVER_VERSION=${NVIDIA_DRIVER_VERSION} --build-arg VNC_PASSWORD=${VNC_PASSWORD} --build-arg LIB_ULTIMATE_VERSION=${LIB_ULTIMATE_VERSION}
run:
	docker-compose -f docker/docker-compose.yml --env-file ./docker/.env up -d
exec:
	docker exec -it libultimate bash
remove:
	docker-compose -f docker/docker-compose.yml --env-file ./docker/.env down
skyline-build:
	cd libultimate-plugin && cargo skyline build && cp target/aarch64-skyline-switch/release/liblibultimate_plugin.nro ../release/contents/01006A800016E000/romfs/skyline/plugins/