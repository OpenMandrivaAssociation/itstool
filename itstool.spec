Name:		itstool
Version:	2.0.7
Release:	2
Summary:	ITS-based XML translation tool
Group:		System/Internationalization
License:	GPLv3+
URL:		https://itstool.org/
Source0:	http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2
# From upstream pull request:
# https://github.com/itstool/itstool/pull/18
Patch0101:	0001-Fix-a-segmentation-fault-bug-introduced-with-version.patch

BuildArch:	noarch
BuildRequires:	python-libxml2
Requires:	python-libxml2
Requires:	python

%description
ITS Tool allows you to translate XML documents with PO files, using rules from
the W3C Internationalization Tag Set (ITS) to determine what to translate and
how to separate it into PO file messages.

%prep
%autosetup -p1
autoreconf -fi

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
