%define name plnode-utils
%define version 0.2
%define taglevel 1

%define release %{taglevel}%{?pldistro:.%{pldistro}}%{?date:.%{date}}

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
cp plnode/bwlimit_vs.py plnode/bwlimit.py
python setup.py build

%install
python setup.py install --skip-build --root "$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

# moved from util-vserver-pl package
%post
/usr/bin/bwlimit init

%files
%{python_sitelib}/*
%{_bindir}

%changelog
