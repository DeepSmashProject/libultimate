
# 0. generate xorg.conf
sudo nvidia-xconfig -a --allow-empty-initial-configuration --enable-all-gpus

cp /home/default/data/keys/prod.keys /home/default/.config/Ryujinx/system/prod.keys

# for running systemd
#/sbin/init
