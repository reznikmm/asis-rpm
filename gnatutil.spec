%undefine _hardened_build
%define _gprdir %_GNAT_project_dir
%define gcc_version 10.2.1

Name:       libgnatutil
Version:    10.2.1
Release:    %{?dist}
Summary:    GNU Ada compiler selected components
Group:      Development/Libraries
License:    GPL
URL:        https://www.adacore.com/download/more
Source0:    gnatutil.tar.gz
Source1:    https://src.fedoraproject.org/repo/pkgs/gcc/gcc-10.2.1-20201016.tar.xz/sha512/d324b7c872210a14aabdc117567ae6eff98d40ee8bf7a705a8caf1330d698e167016fb98f095ab56de43140e5f19932775ff3d5757434e3f78f2eec57d3dd1c4/gcc-10.2.1-20201016.tar.xz
# Patch0:     gcc-10.1.1-gnat_util.patch
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
%setup -q -n gcc-10.2.1-20201016 -b0 -b1
pwd
patch -p1 < ../gnatutil/gcc-10.1.1-gnat_util.patch
#%patch0 -p1

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
* Fri Nov 27 2020 Maxim Reznik <reznikmm@gmail.com> - 10.2.1
- Update to gcc 10.2.1 used in fedora 33

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
