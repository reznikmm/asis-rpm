%undefine _hardened_build
%define _gprdir %_GNAT_project_dir

Name:       libgnatutil
Version:    2016
Release:    gpl%{?dist}
Summary:    GNU Ada compiler selected components
Group:      Development/Libraries
License:    GPL
URL:        https://www.adacore.com/download/more
### gnat_util-gpl-2016-src.tar.gz:
Source0:    http://mirrors.cdn.adacore.com/art/57399637c7a447658e0affa6
BuildRequires:   gcc-gnat
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
%setup -q -n gnat_util-gpl-2016-src

%build
make generate_sources
gprbuild -R -P gnat_util -XLIBRARY_TYPE=relocatable -p -cargs -g

%install
rm -rf %{buildroot}
gprinstall -P gnat_util -XLIBRARY_TYPE=relocatable -p \
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
%{_libdir}/%{name}/libgnat_util.so
%{_libdir}/libgnat_util.so

%files devel
%doc README.gnat_util
%{_libdir}/%{name}/*.ali
%{_includedir}/%{name}
%{_gprdir}/gnat_util.gpr
%{_gprdir}/manifests/gnat_util


%changelog
* Fri Jan 19 2018 Maxim Reznik <reznikmm@gmail.com> - 2016-gpl
- Initial package
