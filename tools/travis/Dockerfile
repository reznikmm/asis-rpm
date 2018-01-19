FROM fedora
RUN dnf --assumeyes upgrade libsolv && \
 dnf --assumeyes install rpmdevtools && \
 dnf --assumeyes install gcc-gnat && \
 dnf --assumeyes install gprbuild && \
 dnf --assumeyes install gdb && \
 dnf --assumeyes install xmlada-devel && \
useradd max && \
su -c rpmdev-setuptree max
COPY * /src/