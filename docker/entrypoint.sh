
# 0. generate xorg.conf
sudo nvidia-xconfig -a --allow-empty-initial-configuration --enable-all-gpus

# for running systemd
/sbin/init
