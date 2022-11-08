build:
	docker build -t deepsmash/libultimate:latest -f docker/Dockerfile .
run:
	docker-compose -f docker/docker-compose.yml --env-file ./docker/.env up -d
remove:
	docker-compose -f docker/docker-compose.yml --env-file ./docker/.env down
