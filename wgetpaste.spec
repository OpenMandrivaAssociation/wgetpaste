Name:		wgetpaste
Version:	2.34
Release:	1
Summary:	pastebin command line tool
URL:		https://wgetpaste.zlin.dk
Source0:  https://github.com/zlin/wgetpaste/releases/download/%{version}/wgetpaste-%{version}.tar.xz
#Source0:	http://wgetpaste.zlin.dk/wgetpaste-%{version}.tar.bz2
Source1:	pastebin.mandriva.com.conf
License:	Public Domain
Requires:	wget
Group:		Networking/WWW
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
%description
Tool allowing to paste output from commands directly to several pastebin
websites.

%prep
%setup -q

%build

%install
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -p wgetpaste %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/wgetpaste.d
%{__cp} -p %{SOURCE1} %{buildroot}%{_sysconfdir}/wgetpaste.d/

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/wgetpaste.d/*
%{_bindir}/%{name}


%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 2.18-1mdv2011.0
+ Revision: 645487
- update to new version 2.18

* Wed Sep 30 2009 Nicolas Vigier <nvigier@mandriva.com> 2.14-1mdv2010.0
+ Revision: 451641
- version 2.14
- license changed: public domain
- import wgetpaste

