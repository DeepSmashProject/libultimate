function usage {
       printf "Usage:\n"
       printf " -h                               Display this help message.\n"
       printf " -p/--port <port>                 NoVNC Port. Default is 8081.\n"
       printf " -d/--display <display num>       DISPLAY number. Default is :1.\n"
       printf " -g/--game_dir <game dir>         Game directory. Required.\n"
       printf " -k/--keys_dir <keys dir>         Keys directory. Required.\n"
       printf " -v/--volume <volume dir>         Volume directory. Required.\n"
       printf " -n/--name <name>                 Docker container name. Default is yuzu_emu.\n"
       printf "Example: bash run.sh -p 8081 -d :0 -g /home/user/games/ -k /home/user/keys -v /home/user/workspace -n example\n"
       exit 0
}

run_ryujinx() {
  local opt optarg h m s
  PORT=8081
  VNCPASS="pass"
  DISPLAY=:1
  BUS_ID=13:0:0
  GAME_DIR=""
  KEYS_DIR=""
  VOLUME=""
  NAME=yuzu_emu

  # 引数を取る指定は - のみ
  while getopts hpdgkvn-: opt; do
      # OPTIND 番目の引数を optarg へ代入
      optarg="${!OPTIND}"
      [[ "$opt" = - ]] && opt="-$OPTARG"

      case "-$opt" in
          -h|--help)
              usage
              shift
              ;;
          -p|--port)
              PORT="$optarg"
              shift
              ;;
          -d|--display)
              DISPLAY="$optarg"
              shift
              ;;
          -g|--game_dir)
              GAME_DIR="$optarg"
              shift
              ;;
          -k|--keys_dir)
              KEYS_DIR="$optarg"
              shift
              ;;
          -v|--volume)
              VOLUME="$optarg"
              shift
              ;;
          -n|--name)
              NAME="$optarg"
              shift
              ;;
          --)
              break
              ;;
          -\?)
              exit 1
              ;;
          --*)
              echo "$0: illegal option -- ${opt##-}" >&2
              exit 1
              ;;
      esac
  done
  shift $((OPTIND - 1))
  echo "game " $GAME_DIR

  if [ "$GAME_DIR" = "" ] 
  then
    echo "ERROR: option -g is required."
    exit 1
  fi
  if [ "$KEYS_DIR" = "" ] 
  then
    echo "ERROR: option -k is required."
    exit 1
  fi
  if [ "$VOLUME" = "" ] 
  then
    echo "ERROR: option -v is required."
    exit 1
  fi

  COMMAND="docker run --privileged -it --gpus all \
  -p $PORT:$PORT \
  -e RESOLUTION=1280x800 \
  -e VNCPASS=$VNCPASS \
  -e DISPLAY=$DISPLAY \
  -e BUS_ID=13:0:0 \
  -e NOVNC_PORT=$PORT \
  -v $VOLUME:/workspace \
  -v $GAME_DIR:/workspace/games \
  -v $KEYS_DIR:/root/.local/share/yuzu/keys \
  --name $NAME deepsmash/yuzu_emu"

  echo $COMMAND
  $COMMAND
}


run_ryujinx $@
