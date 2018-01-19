%undefine _hardened_build
%define _gprdir %_GNAT_project_dir

Name:       libgpr
Version:    2016
Release:    gpl%{?dist}
Summary:    support for programs processing GNAT projects
Group:      Development/Libraries
License:    GPL
URL:        https://www.adacore.com/download/more
### gprbuild-gpl-2016-src.tar.gz
Source0:    http://mirrors.cdn.adacore.com/art/57399662c7a447658e0affa8
BuildRequires:   gcc-gnat
BuildRequires:   fedora-gnat-project-common  >= 3 
BuildRequires:   gprbuild
BuildRequires:   xmlada-devel
Requires:   xmlada

# gprbuild only available on these:
ExclusiveArch: %GPRbuild_arches

%description
GNAT projects are human-readable text files used to drive tools building or
inspecting lots of source files in several programming languages, like those
provided by the gprbuild package. 

This is a library to work with such a projects.

%package devel

Group:      Development/Libraries
License:    GPL
Summary:    Devel package for libgpr
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:   fedora-gnat-project-common  >= 2

%description devel
Devel package for libgpr

%prep 
%setup -q -n gprbuild-gpl-2016-src

%build
./configure --prefix=%{_prefix}
make libgpr.build.shared BUILDER="gprbuild -j0 -R -XBUILD=debug -p"

%install
rm -rf %{buildroot}
#  This is to fix strange complains about gpr-debug.ali :
ln -s lib-debug gpr/lib
gprinstall -P gpr/gpr.gpr -XLIBRARY_TYPE=relocatable -XBUILD=debug -p \
 --prefix=%{_prefix} \
 --sources-subdir=%{buildroot}%{_prefix}/include/%{name} \
 --lib-subdir=%{buildroot}%{_libdir}/%{name} \
 --project-subdir=%{buildroot}%{_gprdir} \
 --link-lib-subdir=%{buildroot}%{_libdir}

%post     -p /sbin/ldconfig
%postun   -p /sbin/ldconfig

%files
%doc COPYING3
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libgpr.so
%{_libdir}/libgpr.so

%files devel
%doc README.md
%{_libdir}/%{name}/*.ali
%{_includedir}/%{name}
%{_gprdir}/gpr.gpr
%{_gprdir}/manifests/gpr


%changelog
* Fri Jan 19 2018 Maxim Reznik <reznikmm@gmail.com> - 2016-gpl
- Initial package
