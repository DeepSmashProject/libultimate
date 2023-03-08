FROM nvidia/cudagl:11.4.2-runtime-ubuntu20.04

ENV container docker
ENV DEBIAN_FRONTEND noninteractive

##################
# get keys for apt
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub

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

# Install systemd
RUN apt-get update && apt-get install -y \
    dbus dbus-x11 systemd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* &&\
    dpkg-divert --local --rename --add /sbin/udevadm &&\
    ln -s /bin/true /sbin/udevadm
RUN systemctl disable systemd-resolved
VOLUME ["/sys/fs/cgroup"]
STOPSIGNAL SIGRTMIN+3
CMD [ "/sbin/init" ]

# Install GNOME
# NOTE if you want plain gnome, use: apt-get install -y --no-install-recommends gnome-session gnome-terminal and remove the modification of /etc/gdm3/custom.conf
#   && apt-get install -y --no-install-recommends gnome-session gnome-terminal \
RUN apt-get update \
    && apt-get install -y ubuntu-desktop fcitx-config-gtk gnome-tweak-tool gnome-usage \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && sed -i 's/\[daemon\]/[daemon]\nInitialSetupEnable=false/' /etc/gdm3/custom.conf


# Install TigerVNC server
# TODO set VNC port in service file > exec command
# TODO check if it works with default config file
# NOTE tigervnc because of XKB extension: https://github.com/i3/i3/issues/1983
RUN apt-get update \
    && apt-get install -y tigervnc-common tigervnc-scraping-server tigervnc-standalone-server tigervnc-xorg-extension \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# NOTE logout will stop tigervnc service -> need to manually start (gdm for graphical login is not working)
COPY ./docker/tigervnc@.service /etc/systemd/system/tigervnc@.service
RUN systemctl enable tigervnc@:1
EXPOSE 5901

# Install noVNC
# TODO novnc depends on net-tools until version 1.1.0: https://github.com/novnc/noVNC/issues/1075
RUN apt-get update && apt-get install -y \
    net-tools novnc \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/share/novnc/vnc_lite.html /usr/share/novnc/index.html
# TODO specify options like ports as environment variables -> source variables in service via EnvironmentFile=/path/to/env
COPY ./docker/novnc.service /etc/systemd/system/novnc.service
RUN systemctl enable novnc
EXPOSE 6080

# Create unprivileged user
# NOTE user hardcoded in tigervnc.service
# NOTE alternative is to use libnss_switch and create user at runtime -> use entrypoint script
ARG UID=1000
ARG USER=default
RUN useradd ${USER} -u ${UID} -U -d /home/${USER} -m -s /bin/bash
RUN apt-get update && apt-get install -y sudo && apt-get clean && rm -rf /var/lib/apt/lists/* && \
    echo "${USER} ALL=(ALL) NOPASSWD: ALL" > "/etc/sudoers.d/${USER}" && \
    chmod 440 "/etc/sudoers.d/${USER}"
USER "${USER}"
ENV USER="${USER}" \
    HOME="/home/${USER}"
WORKDIR "/home/${USER}"

# Set up VNC
ARG VNC_PASSWORD
RUN mkdir -p $HOME/.vnc
COPY ./docker/xstartup $HOME/.vnc/xstartup
RUN echo ${VNC_PASSWORD} | vncpasswd -f >> $HOME/.vnc/passwd && chmod 600 $HOME/.vnc/passwd

######### Install and Build ryujinx #############
RUN sudo apt-get update && sudo apt-get install -y curl
RUN option=1 noconfirm=1 bash -c "$(curl -s https://raw.githubusercontent.com/edisionnano/Pine-jinx/main/pinejinx.sh)"

# switch back to root to start systemd
USER root

##################
# Install NVIDIA drivers, including X graphic drivers
# sudo nvidia-xconfig -a --virtual=$RESOLUTION --allow-empty-initial-configuration --enable-all-gpus --busid $BUS_ID
ARG NVIDIA_DRIVER_VERSION
RUN apt-get install -y kmod pkg-config
RUN cd /tmp && \
    curl -fSsl -O https://us.download.nvidia.com/tesla/$NVIDIA_DRIVER_VERSION/NVIDIA-Linux-x86_64-$NVIDIA_DRIVER_VERSION.run && \
    sh NVIDIA-Linux-x86_64-$NVIDIA_DRIVER_VERSION.run -x && \
    cd NVIDIA-Linux-x86_64-$NVIDIA_DRIVER_VERSION && \
    ./nvidia-installer --silent \
    --no-kernel-module \
    --install-compat32-libs \
    --no-nouveau-check \
    --no-nvidia-modprobe \
    --no-rpms \
    --no-backup \
    --no-check-for-alternate-installs \
    --no-libglx-indirect \
    --no-install-libglvnd && \
    mkdir -p /usr/src/nvidia-$NVIDIA_DRIVER_VERSION && \
    mv LICENSE mkprecompiled kernel /usr/src/nvidia-$NVIDIA_DRIVER_VERSION && \
    sed '9,${/^\(kernel\|LICENSE\)/!d}' .manifest > /usr/src/nvidia-$NVIDIA_DRIVER_VERSION/.manifest

############# for NVIDIA ##################
ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

# Ryujinx Dependecies
RUN apt-get install -y libx11-dev libsdl2-dev 

## for fixing Application: Unhandled exception caught:SPB. error
ENV __GLX_VENDOR_LIBRARY_NAME=nvidia
ENV DRI_PRIME=1

## for glxinfo openGL version
ENV __NV_PRIME_RENDER_OFFLOAD=1
ENV __VK_LAYER_NV_optimus=NVIDIA_only
RUN apt-get install -y mesa-utils

# Install Python3
RUN apt-get install -y python3 python3-pip

# Install Cargo Skyline
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN . "$HOME/.cargo/env" && cargo install cargo-skyline

############ for Application ############
ARG LIB_ULTIMATE_VERSION
RUN mkdir $HOME/data && \
    curl -L https://github.com/DeepSmashProject/libultimate/releases/download/${LIB_ULTIMATE_VERSION}/release.zip > $HOME/data/release.zip && \
    unzip $HOME/data/release.zip -d $HOME/data && rm $HOME/data/release.zip

WORKDIR $HOME
RUN apt-get install -y git
RUN git clone https://github.com/DeepSmashProject/libultimate.git -b ${LIB_ULTIMATE_VERSION} --depth 1 
WORKDIR $HOME/libultimate
RUN sudo -H pip install -e .

COPY ./docker/entrypoint.sh $HOME/entrypoint.sh
