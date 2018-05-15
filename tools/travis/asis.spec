%undefine _hardened_build
%define _gprdir %_GNAT_project_dir

Name:       asis
Version:    2017
Release:    gpl%{?dist}
Summary:    Ada Semantic Interface Specification (ASIS) runtime library
Group:      Development/Libraries
License:    GPL
URL:        https://www.adacore.com/download/more
### asis-gpl-2017-src.tar.gz:
Source0:    http://mirrors.cdn.adacore.com/art/591c45e2c7a447af2deecffb
Patch0:     no_version_check.diff
Patch1:     with_gnat_util.diff
Patch2:     gcc-8.diff
BuildRequires:   gcc-gnat
BuildRequires:   fedora-gnat-project-common  >= 3 
BuildRequires:   gprbuild
BuildRequires:   libgnatutil-devel

# gprbuild only available on these:
ExclusiveArch: %GPRbuild_arches

%description
ASIS (Ada Semantic Interface Specification) lets you develop applications to
walk through the sources of your Ada programs and examine the semantic
constructs.

This package contains the libraries necessary to execute ASIS programs. 
%package devel

Group:      Development/Libraries
License:    GPL
Summary:    Devel package for asis
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:   fedora-gnat-project-common  >= 2

%description devel
Devel package for asis

%prep 
%setup -q -n asis-gpl-2017-src
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
gprbuild -P asis.gpr %Gnatmake_optflags

%install
rm -rf %{buildroot}
gprinstall -P asis.gpr -p \
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
%{_libdir}/%{name}/lib%{name}.so
%{_libdir}/lib%{name}.so

%files devel
%doc README
%{_libdir}/%{name}/*.ali
%{_includedir}/%{name}
%{_gprdir}/%{name}.gpr
%{_gprdir}/manifests/%{name}


%changelog
* Tue May 15 2018 Maxim Reznik <reznikmm@gmail.com> - 2016-gpl
- Apply patch for gcc-8 from https://github.com/simonjwright/ASIS

* Fri Jan 19 2018 Maxim Reznik <reznikmm@gmail.com> - 2016-gpl
- Initial package
