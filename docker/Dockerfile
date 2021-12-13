FROM deepsmash/yuzu_emu:latest

WORKDIR /workspace
RUN git clone https://github.com/DeepSmashProject/libultimate.git
RUN pip install -e libultimate

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh