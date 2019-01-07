%define name plnode-utils
%define version 1.0
%define taglevel 0

%define release %{taglevel}%{?pldistro:.%{pldistro}}%{?date:.%{date}}

%define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Summary: Python utilities for a PlanetLab node
Name: %{name}
Version: %{version}
Release: %{release}
License: PlanetLab
Group: System Environment/Libraries
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Vendor: PlanetLab
Packager: PlanetLab Central <support@planet-lab.org>
Distribution: PlanetLab %{plrelease}
URL: %{SCMURL}

Provides: bwlimit

%description
This python3 package provides utilities like bwlimit, used in various places on a PlanetLab node, nodemanager and mom among others. It aims at cleaning up the packaging scheme, as bwlimit used to ship with util-vserver-pl, but is relevant in the lxc variant as well.

%prep
%setup -q

%build
# xxx fixme
# this is where we chose which flavour of bwlimit gets shipped
cp plnode/bwlimit_vs.py plnode/bwlimit.py
# for backwards compatibilty until legacy packages import from plnode
cp plnode/bwlimit_vs.py bwlimit.py
python3 setup.py build

%install
python3 setup.py install --skip-build --root "$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

# moved from util-vserver-pl package
%post
/usr/bin/bwlimit init

%files
%{python3_sitelib}/*
%{_bindir}/*

%changelog
* Mon Jan 07 2019 Thierry <Parmentelat> - plnode-utils-1.0-0
- ported to python3 + various cleanups
- more tolerant wrt units (accepts more floats)

* Mon Feb 11 2013 Stephen Soltesz <soltesz@opentechinstitute.org> - plnode-utils-0.2-2
- import bwlimit from plnode dir, and keep legacy support.
