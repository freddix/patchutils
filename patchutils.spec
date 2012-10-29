Summary:	Patchutils is a small collection of programs that operate on patch files
Name:		patchutils
Version:	0.3.2
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://cyberelk.net/tim/data/%{name}/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	74607b4a28c9009c6aeeed0e91098917
Patch1:		%{name}-fixcvsdiff.patch
URL:		http://cyberelk.net/tim/patchutils/
BuildRequires:	diffutils
BuildRequires:	patch
BuildRequires:	perl-base
Requires:	diffutils
Requires:	patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Patchutils is a small collection of programs that operate on patches.

%prep
%setup -q
%patch1 -p0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

sed -i "s|^#!/bin|#!/usr/bin|" $RPM_BUILD_ROOT%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*

