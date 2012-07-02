%define name plnode-utils
%define version 0.1
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

%description
This package provides the plnode_utils python package that provides utilities used in various places on a PlanetLab node, nodemanager among others

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --skip-build --root "$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{python_sitelib}/*

%changelog
