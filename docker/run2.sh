docker run --privileged -it --rm --gpus all \
  -p 8082:8082 \
  -p 6000:6000 \
  -p 6007:6007 \
  -e RESOLUTION=1280x800 \
  -e VNCPASS=pass \
  -e DISPLAY=:1 \
  -e BUS_ID=13:0:0 \
  -e NOVNC_PORT=8082 \
  -e API_PORT=6000 \
  -e API_HOST=0.0.0.0 \
  -e API_FILE_PATH=/workspace/libultimate/run_server.py \
  -v "/mnt/bigdata/00_students/ruirui_nis/DeepSmashProject/games:/workspace/games" \
  -v "/mnt/bigdata/00_students/ruirui_nis/DeepSmashProject/keys:/root/.local/share/yuzu/keys" \
  --name libultimate deepsmash/libultimate


  #-v "/home/ruirui_nis/workspace/DeepSmashProject:/workspace" \