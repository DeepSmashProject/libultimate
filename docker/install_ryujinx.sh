#!/usr/bin/env sh
# Prepare environment
rm -rf /tmp/pineapple
mkdir -p /tmp/pineapple && cd /tmp/pineapple
gamemode="N"
mesanoerror="N"
gpuopt="1"
console="N"
alias="N"
USER="guest"
#Define the functions
install() {
    version=$(curl -s https://api.github.com/repos/Ryujinx/release-channel-master/releases/latest | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')
	printf "Latest version is: $version\n"
	printf "Downloading $version...\n"
	curl -L "https://github.com/Ryujinx/release-channel-master/releases/download/${version}/ryujinx-${version}-linux_x64.tar.gz" > ryujinx-${version}-linux_x64.tar.gz
	tar -xf ryujinx-${version}-linux_x64.tar.gz
	arch_dir=$(tar --exclude='*/*' -tf ryujinx-${version}-linux_x64.tar.gz)
	if [ -d "$arch_dir" ]; then
		printf "Extraction successful!\n"
		mkdir -p /home/${USER}/.local/share/Ryujinx
		cp -a $arch_dir/. /home/${USER}/.local/share/Ryujinx
	else
		printf "Extraction failed!\nAborting...\n"
		exit
	fi
	curl -s -L "https://raw.githubusercontent.com/edisionnano/Pine-jinx/main/Ryujinx.desktop" > Ryujinx.desktop
	curl -s -L "https://raw.githubusercontent.com/edisionnano/Pine-jinx/main/Ryujinx.png" > Ryujinx.png
	curl -s -L "https://raw.githubusercontent.com/edisionnano/Pine-jinx/main/Ryujinx.xml" > Ryujinx.xml

	if [ "$gamemode" = "y" ] || [ "$gamemode" = "Y" ]; then
		arg1="gamemoderun "
		curl -s -L "https://raw.githubusercontent.com/edisionnano/Pine-jinx/main/gamemode.ini" > /home/${USER}/.config/gamemode.ini
	else
		arg1=""
	fi
	if [ "$gpuopt" = "1" ]; then
		arg2='__GL_THREADED_OPTIMIZATIONS=0 __GL_SYNC_TO_VBLANK=0 '
	elif [ "$gpuopt" = "2" ]; then
		arg2="AMD_DEBUG=w32ge,w32cs,nohyperz,nofmask glsl_zero_init=true radeonsi_clamp_div_by_zero=true force_integer_tex_nearest=true mesa_glthread=false vblank_mode=0 RADV_PERFTEST=bolist"
		if [ "$mesanoerror" = "y" ] || [ "$mesanoerror" = "Y" ]; then
            arg3="MESA_NO_ERROR=1 "
        else
            arg3=""
        fi
	else
		arg2=''
	fi
	arg=$(echo "$arg2$arg3$arg1"|sed 's/ *$//')
	if [ "$console" = "y" ] || [ "$console" = "Y" ]; then
		sed -i "s/Terminal=true/Terminal=false/g" Ryujinx.desktop
	fi
	if [ "$alias" = "y" ] || [ "$alias" = "Y" ]; then
		makealias
	else
		:
	fi
    #Desktop entries do not accept relative paths so the user's name must be in the file
	sed -i "s/dummy/${USER}/g" Ryujinx.desktop
	#Append any optimizations
	sed -i "s/x11/x11 ${arg}/" Ryujinx.desktop
	#Place desktop entry
	mkdir -p /home/${USER}/.local/share/applications && cp Ryujinx.desktop /home/${USER}/.local/share/applications
	#Place icon
	mkdir -p /home/${USER}/.local/share/icons && cp Ryujinx.png /home/${USER}/.local/share/icons
	#Place mime entry
	mkdir -p /home/${USER}/.local/share/mime/packages && cp Ryujinx.xml /home/${USER}/.local/share/mime/packages
	#Set the rights
	chmod +x /home/${USER}/.local/share/Ryujinx/Ryujinx
	#Update the MIME database
	update-mime-database /home/${USER}/.local/share/mime
	#Update the application database
	update-desktop-database /home/${USER}/.local/share/applications
	printf "Installation successful, launch Ryujinx from your app launcher.\n"
	printf "Also don't forget to show your love on Patreon at https://www.patreon.com/ryujinx\n"
}

install
exit
