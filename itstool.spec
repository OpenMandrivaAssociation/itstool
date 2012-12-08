Name:		itstool
Version:	1.2.0
Release:	1
Summary:	ITS-based XML translation tool
Group:		System/Internationalization
License:	GPLv3+
URL:		http://itstool.org/
Source0:	http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	python-libxml2

%description
ITS Tool allows you to translate XML documents with PO files, using rules from
the W3C Internationalization Tag Set (ITS) to determine what to translate and
how to separate it into PO file messages.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*



%changelog
* Tue Mar 06 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.1.2-1
+ Revision: 782532
- imported package itstool

