build:
	docker build -t deepsmash/libultimate:latest -f docker/Dockerfile .
run:
	docker run --privileged -it --rm --gpus all \
	-p 8081:8081 \
	-p 6000:6000 \
	-p 6006:6006 \
	-e RESOLUTION=1280x800 \
	-e DISPLAY=:1 \
	-e NOVNC_PORT=8081 \
	-e API_PORT=6000 \
	-e API_HOST=0.0.0.0 \
	-e API_FILE_PATH=/workspace/libultimate/run_server.py \
	-v "/home/ruirui_nis/workspace/DeepSmashProject:/workspace" \
	-v "/mnt/bigdata/00_students/ruirui_nis/DeepSmashProject/games:/data/games" \
	-v "/mnt/bigdata/00_students/ruirui_nis/DeepSmashProject/firmware:/data/firmware" \
	-v "/mnt/bigdata/00_students/ruirui_nis/DeepSmashProject/keys:/data/keys" \
	--name deepsmash/libultimate deepsmash/libultimate:latest
