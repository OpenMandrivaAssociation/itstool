Summary:	ITS-based XML translation tool
Name:		itstool
Version:	1.2.0
Release:	1
Group:		System/Internationalization
License:	GPLv3+
Url:		http://itstool.org/
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

