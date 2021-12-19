FROM deepsmash/yuzu_emu:latest

WORKDIR /workspace/libultimate
COPY . .
#RUN git clone https://github.com/DeepSmashProject/libultimate.git
RUN pip install -e .

COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh