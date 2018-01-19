FROM fedora
RUN dnf --assumeyes upgrade libsolv && \
 dnf --assumeyes install rpmdevtools && \
 dnf --assumeyes install gcc-gnat && \
 dnf --assumeyes install gprbuild && \
useradd max && \
su -c rpmdev-setuptree max
COPY * /src/