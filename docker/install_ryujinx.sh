#!/usr/bin/env sh

install() {
    version=$(curl -s https://api.github.com/repos/Ryujinx/release-channel-master/releases/latest | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')
	printf "Latest version is: $version\n"
	printf "Downloading $version...\n"
	curl -L "https://github.com/Ryujinx/release-channel-master/releases/download/${version}/ryujinx-${version}-linux_x64.tar.gz" > ryujinx-${version}-linux_x64.tar.gz
	tar -xf ryujinx-${version}-linux_x64.tar.gz
	arch_dir=$(tar --exclude='*/*' -tf ryujinx-${version}-linux_x64.tar.gz)
	if [ -d "$arch_dir" ]; then
		printf "Extraction successful at /publish/Ryujinx!\n"
	else
		printf "Extraction failed!\nAborting...\n"
		exit
	fi
}

install
exit
