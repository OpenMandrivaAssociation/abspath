Summary:	Return the absolute path of a file or directory
Name:		abspath
Version:	0.1
Release:	8
License:	GPLv2+
Group:		File tools
Url:		https://web.archive.org/web/20230000000000*/http://voxel.jouy.inra.fr/darcs/abspath
Source0:	%{name}-%{version}.tar.bz2
Patch0:		abspath-asciidoc.patch
Requires:	python
BuildRequires:	asciidoc
BuildRequires:	docbook-style-xsl
BuildRequires:	xmlto
BuildArch:	noarch

%description
Return a normalized absolutized version of the pathnames. If no arguments
are passed on the command line, the standard input is used.

This package is deprecated, just use the realpath command.

%files
%{_bindir}/abspath
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
2to3 -w abspath
chmod a+x abspath
asciidoc -b docbook -d manpage abspath.1.txt
xmlto man abspath.1.xml
perl -e 's/\.sp$/\n\.sp/g' -pi abspath.1

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 abspath %{buildroot}%{_bindir}/
install -m 0644 abspath.1 %{buildroot}%{_mandir}/man1/

