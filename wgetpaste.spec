Name:		wgetpaste
Version:	2.18
Release:	%mkrel 1
Summary:	pastebin command line tool
URL:		http://wgetpaste.zlin.dk
Source0:	http://wgetpaste.zlin.dk/wgetpaste-%{version}.tar.bz2
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
