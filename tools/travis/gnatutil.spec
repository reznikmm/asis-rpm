%undefine _hardened_build
%define _gprdir %_GNAT_project_dir
%define gcc_version 9.2.0

Name:       libgnatutil
Version:    9.2.1
Release:    %{?dist}
Summary:    GNU Ada compiler selected components
Group:      Development/Libraries
License:    GPL
URL:        https://www.adacore.com/download/more
Source0:    http://robotlab.itk.ppke.hu/gcc/releases/gcc-%{gcc_version}/gcc-%{gcc_version}.tar.xz
Patch0:     gcc-9.1.0-gnat_util.patch
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
%setup -q -n gcc-%{gcc_version}
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
