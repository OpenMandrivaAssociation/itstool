Name:		itstool
Version:	2.0.4
Release:	3
Summary:	ITS-based XML translation tool
Group:		System/Internationalization
License:	GPLv3+
URL:		http://itstool.org/
Source0:	http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2
# Patch to fix segfaults and build issues for some GNOME stuff. (penguin)
# More details https://github.com/voidlinux/void-packages/issues/8365#issuecomment-339443385
Patch0: itstool-fix-libxml2.patch
BuildArch:	noarch
BuildRequires:	python-libxml2
Requires:	python-libxml2
Requires:	python

%description
ITS Tool allows you to translate XML documents with PO files, using rules from
the W3C Internationalization Tag Set (ITS) to determine what to translate and
how to separate it into PO file messages.

%prep
%setup -q
%patch0 -p0
autoreconf -fi

%build
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
