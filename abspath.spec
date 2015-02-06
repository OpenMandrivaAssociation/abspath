Summary:	Return the absolute path of a file or directory
Name:		abspath
Version:	0.1
Release:	7
License:	GPLv2+
Group:		File tools
Url:		http://voxel.jouy.inra.fr/darcs/abspath
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

%files
%{_bindir}/abspath
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
chmod a+x abspath
asciidoc -b docbook -d manpage abspath.1.txt
xmlto man abspath.1.xml
perl -e 's/\.sp$/\n\.sp/g' -pi abspath.1

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 abspath %{buildroot}%{_bindir}/
install -m 0644 abspath.1 %{buildroot}%{_mandir}/man1/

