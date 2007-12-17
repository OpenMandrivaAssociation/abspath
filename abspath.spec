
Summary: Return the absolute path of a file or directory
Name: abspath
Version: 0.1
Release: %mkrel 1
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: File tools
Url: http://voxel.jouy.inra.fr/darcs/abspath
Requires: python
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: perl
BuildArch:    noarch

%description
Return a normalized absolutized version of the pathnames. If no arguments
are passed on the command line, the standard input is used.

%prep
%setup -q

%build
chmod a+x abspath
asciidoc -b docbook -d manpage abspath.1.txt
xmlto man abspath.1.xml
perl -e 's/\.sp$/\n\.sp/g' -pi abspath.1

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
cp abspath $RPM_BUILD_ROOT/%{_bindir}/
cp abspath.1 $RPM_BUILD_ROOT/%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/abspath
%{_mandir}/man1/*



