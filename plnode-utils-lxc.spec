%define name plnode-utils
%define version 0.2
%define taglevel 2

%define release %{taglevel}%{?pldistro:.%{pldistro}}%{?date:.%{date}}

# for f12
%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

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
This python package provides utilities like bwlimit, used in various places on a PlanetLab node, nodemanager and mom among others. It aims at cleaning up the packaging scheme, as bwlimit used to ship with util-vserver-pl, but is relevant in the lxc variant as well.

%prep
%setup -q

%build
# xxx fixme
# this is where we chose which flavour of bwlimit gets shipped
cp plnode/bwlimit_lxc.py plnode/bwlimit.py
/usr/bin/python setup.py build

%install
/usr/bin/python setup.py install --skip-build --root "$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{python_sitelib}/*
%{_bindir}/*

%changelog
