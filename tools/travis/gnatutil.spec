%undefine _hardened_build
%define _gprdir %_GNAT_project_dir
%define gcc_version 10.1.1

Name:       libgnatutil
Version:    10.1.1
Release:    %{?dist}
Summary:    GNU Ada compiler selected components
Group:      Development/Libraries
License:    GPL
URL:        https://www.adacore.com/download/more
Source0:    https://src.fedoraproject.org/repo/pkgs/gcc/gcc-10.1.1-20200507.tar.xz/sha512/2847d8d44ea2f174dc4f510a1727150691c66ab4cc4e256630cafeb5f10272d1b1ab2aaa7dda21539cbd414a108355e7798b269cd91e0fe964ebc4bbcfc19604/gcc-10.1.1-20200507.tar.xz
Patch0:     gcc-10.1.1-gnat_util.patch
BuildRequires:   gcc-gnat = %{version}
BuildRequires:   fedora-gnat-project-common  >= 3
BuildRequires:   gprbuild

# gprbuild only available on these:
ExclusiveArch: %GPRbuild_arches

%description
GNU Ada compiler selected components required by ASIS.

%package devel

Group:      Development/Libraries
License:    GPL
Summary:    Devel package for libgnatutil
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:   fedora-gnat-project-common  >= 2

%description devel
Devel package for libgnatutil

%prep 
%setup -q -n gcc-10.1.1-20200507
%patch0 -p1

%build
make -C gcc/ada GPRBUILD_FLAGS="%Gnatmake_optflags"

%install
rm -rf %{buildroot}
make -C gcc/ada install DESTDIR=%{buildroot} LIBDIR=%{_libdir} PREFIX=%{_prefix} GPRDIR=%{_gprdir} BINDIR=%{_bindir}

%post     -p /sbin/ldconfig
%postun   -p /sbin/ldconfig

%files
%doc COPYING3
%dir %{_libdir}/gnat_util
%{_libdir}/gnat_util/libgnat_util.so
%{_libdir}/libgnat_util.so

%files devel
%{_libdir}/gnat_util/*.ali
%{_includedir}/gnat_util
%{_gprdir}/gnat_util.gpr
%{_gprdir}/manifests/gnat_util


%changelog
* Sat Jul 18 2020 Maxim Reznik <reznikmm@gmail.com> - 10.1.1
- Update to gcc 10.1.1 used in fedora 32

* Thu Mar 19 2020 Maxim Reznik <reznikmm@gmail.com> - 10.0.1
- Update to gcc 10.0.1 used in fedora 32

* Thu Nov 26 2019 Maxim Reznik <reznikmm@gmail.com> - 9.2.1
- Update to gcc 9.2.1 used in fedora 31

* Thu Jun  6 2019 Maxim Reznik <reznikmm@gmail.com> - 9.1.1
- Update to gcc 9.1.1 used in fedora 30

* Sat Nov 17 2018 Maxim Reznik <reznikmm@gmail.com> - 8.2.1
- Update to gcc 8.2.1 used in fedora 29

* Sun May 13 2018 Maxim Reznik <reznikmm@gmail.com> - 8.1.0
- Update to gcc 8.1.0

* Fri Jan 19 2018 Maxim Reznik <reznikmm@gmail.com> - 2016-gpl
- Initial package
