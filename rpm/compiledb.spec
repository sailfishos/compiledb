# fixme: should be defined in base system side
%define python3_sitelib %(%{__python3} -Ic "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name: compiledb
Summary: Compilation Database Generator
Version: 0.10.1
Release: 1
License: GPLv3
URL: https://github.com/nickdiego/compiledb
Source0: %{name}-%{version}.tar.bz2
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-click
BuildRequires: python3-bashlex
BuildRequires: python3-shutilwhich
Requires: python3-click
Requires: python3-bashlex
Requires: python3-setuptools
Requires: python3-shutilwhich

%description
Tool for generating Clang's JSON Compilation Database file for GNU make-based build 
systems.

%prep
%autosetup -n %{name}-%{version}/compiledb

%build
CFLAGS="%{optflags}" %{__python3} setup.py build %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/compiledb
%{python3_sitelib}/compiledb
%{python3_sitelib}/compiledb-*.egg-info/
