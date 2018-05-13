FROM fedora
RUN dnf --assumeyes install rpmdevtools && \
 dnf --assumeyes install gcc-gnat && \
 dnf --assumeyes install gprbuild && \
 dnf --assumeyes install make && \
useradd max && \
su -c rpmdev-setuptree max
COPY * /src/