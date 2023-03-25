FROM nvidia/cudagl:11.3.0-devel-ubuntu20.04

ENV DEBIAN_FRONTEND noninteractive
USER root
ENV HOME /root
WORKDIR $HOME

##################
# get keys for apt
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub

# Install locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
RUN apt-get update && apt-get install -y --no-install-recommends \
    locales && \
    echo "$LANG UTF-8" >> /etc/locale.gen && \
    locale-gen && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Timezone
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# (1) Install Common Packages
RUN dpkg --add-architecture i386 && \
    apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    wget \
    vim \
    zip \
    unzip \
    git \
    mesa-utils \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Install NVIDIA drivers, including X graphic drivers
# sudo nvidia-xconfig -a --virtual=$RESOLUTION --allow-empty-initial-configuration --enable-all-gpus --busid $BUS_ID
ARG NVIDIA_DRIVER_VERSION
RUN apt-get update && apt-get install -y \
    kmod \
    pkg-config \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
RUN cd /tmp \
    && curl -fSsl -O https://us.download.nvidia.com/XFree86/Linux-x86_64/$NVIDIA_DRIVER_VERSION/NVIDIA-Linux-x86_64-$NVIDIA_DRIVER_VERSION.run \
    && sh NVIDIA-Linux-x86_64-$NVIDIA_DRIVER_VERSION.run -x \
    && cd NVIDIA-Linux-x86_64-$NVIDIA_DRIVER_VERSION \
    && ./nvidia-installer --silent \
    --no-kernel-module \
    --install-compat32-libs \
    --no-nouveau-check \
    --no-nvidia-modprobe \
    --no-rpms \
    --no-backup \
    --no-check-for-alternate-installs \
    --no-libglx-indirect \
    --no-install-libglvnd \
    && mkdir -p /usr/src/nvidia-$NVIDIA_DRIVER_VERSION \
    && mv LICENSE mkprecompiled kernel /usr/src/nvidia-$NVIDIA_DRIVER_VERSION \
    && sed '9,${/^\(kernel\|LICENSE\)/!d}' .manifest > /usr/src/nvidia-$NVIDIA_DRIVER_VERSION/.manifest
ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics
ENV __GLX_VENDOR_LIBRARY_NAME=nvidia
ENV DRI_PRIME=1
ENV __NV_PRIME_RENDER_OFFLOAD=1
ENV __VK_LAYER_NV_optimus=NVIDIA_only

# Install systemd
RUN apt-get update && apt-get install -y \
    dbus dbus-x11 systemd \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*\
    && dpkg-divert --local --rename --add /sbin/udevadm\
    && ln -s /bin/true /sbin/udevadm \
    && systemctl disable systemd-resolved
VOLUME ["/sys/fs/cgroup"]
STOPSIGNAL SIGRTMIN+3
CMD [ "/sbin/init" ]

# Install GNOME
RUN apt-get update && apt-get install -y \
    ubuntu-desktop \
    fcitx-config-gtk \
    gnome-tweak-tool \
    gnome-usage \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && sed -i 's/\[daemon\]/[daemon]\nInitialSetupEnable=false/' /etc/gdm3/custom.conf

# Install TigerVNC server
COPY ./docker/tigervnc@.service /etc/systemd/system/tigervnc@.service
RUN apt-get update && apt-get install -y \
    tigervnc-common \
    tigervnc-scraping-server \
    tigervnc-standalone-server \
    tigervnc-xorg-extension \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && systemctl enable tigervnc@:1
EXPOSE 5901
ENV DISPLAY=:1
# Set up VNC
COPY ./docker/xstartup $HOME/.vnc/xstartup
ARG VNC_PASSWORD
RUN mkdir -p $HOME/.vnc \
    && echo ${VNC_PASSWORD} | vncpasswd -f >> $HOME/.vnc/passwd && chmod 600 $HOME/.vnc/passwd

# Install noVNC
COPY ./docker/novnc.service /etc/systemd/system/novnc.service
RUN apt-get update && apt-get install -y \
    net-tools \
    novnc \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/share/novnc/vnc_lite.html /usr/share/novnc/index.html \
    && systemctl enable novnc
EXPOSE 6080

RUN echo "export __GLX_VENDOR_LIBRARY_NAME=nvidia" >> ~/.bashrc && \
    echo "export DRI_PRIME=1" >> ~/.bashrc && \
    echo "export __VK_LAYER_NV_optimus=NVIDIA_only" >> ~/.bashrc && \
    echo "export __NV_PRIME_RENDER_OFFLOAD=1" >> ~/.bashrc && \
    echo "export NVIDIA_VISIBLE_DEVICES=all" >> ~/.bashrc && \
    echo "export NVIDIA_DRIVER_CAPABILITIES=all" >> ~/.bashrc

# Install Ryujinx
RUN option=1 noconfirm=1 USER=$USER bash -c "$(curl -s https://raw.githubusercontent.com/edisionnano/Pine-jinx/main/pinejinx.sh)"

# Install Yuzu
#RUN wget https://github.com/yuzu-emu/yuzu-mainline/releases/download/mainline-0-1364/yuzu-mainline-20230308-9e9548d12.AppImage \
#    && chmod a+x yuzu-mainline-20230308-9e9548d12.AppImage \
#    && ./yuzu-mainline-20230308-9e9548d12.AppImage --appimage-extract \
#    && chmod a+x squashfs-root/AppRun && mkdir yuzu-mainline && mv squashfs-root/* yuzu-mainline

#RUN wget https://github.com/yuzu-emu/yuzu-mainline/releases/download/mainline-0-850/yuzu-20211216-fddc180bd.AppImage \
#    && chmod a+x yuzu-20211216-fddc180bd.AppImage \
#    && ./yuzu-20211216-fddc180bd.AppImage --appimage-extract \
#    && chmod a+x squashfs-root/AppRun && mkdir yuzu-mainline && mv squashfs-root/* yuzu-mainline

RUN wget https://github.com/yuzu-emu/yuzu-mainline/releases/download/mainline-0-1000/yuzu-20220429-31acffa26.AppImage \
    && chmod a+x yuzu-20220429-31acffa26.AppImage \
    && ./yuzu-20220429-31acffa26.AppImage --appimage-extract \
    && chmod a+x squashfs-root/AppRun && mkdir yuzu-mainline && mv squashfs-root/* yuzu-mainline

# Install libultimate
ARG LIB_ULTIMATE_VERSION
RUN mkdir $HOME/data && \
    curl -L https://github.com/DeepSmashProject/libultimate/releases/download/${LIB_ULTIMATE_VERSION}/release.zip > $HOME/data/release.zip && \
    unzip $HOME/data/release.zip -d $HOME/data && rm $HOME/data/release.zip
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* && \
    git clone https://github.com/DeepSmashProject/libultimate.git -b ${LIB_ULTIMATE_VERSION} && \
    cd libultimate && pip3 install -e .

# Install cargo skyline
ENV PATH="$HOME/.cargo/bin:$PATH"
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* && \ 
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    . "$HOME/.cargo/env" && cargo install cargo-skyline