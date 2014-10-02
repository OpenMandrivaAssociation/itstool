Name:		itstool
Version:	2.0.2
Release:	2
Summary:	ITS-based XML translation tool
Group:		System/Internationalization
License:	GPLv3+
URL:		http://itstool.org/
Source0:	http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	python2-libxml2
Requires:	python2-libxml2
Requires:	python2

%description
ITS Tool allows you to translate XML documents with PO files, using rules from
the W3C Internationalization Tag Set (ITS) to determine what to translate and
how to separate it into PO file messages.

%prep
%setup -q
sed -i 's/| python/&2/' configure.ac
autoreconf -fi

%build
export PYTHON=/usr/bin/python2
%configure
%make

%install
%makeinstall_std

%files
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
