Summary:	DevFS Daemon
Summary(pl):	Deamon DevFS
Name:		devfsd
Version:	1.3.10
Release:	2
Source0:	ftp://ftp.atnf.csiro.au:21/pub/people/rgooch/linux/daemons/%{name}-v%{version}.tar.gz
Source1:	devfsd.conf
License:	GPL
Group:		Base
Group(de):	Gr�nds�tzlich
Group(pl):	Podstawowe
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
Device File System Daemon.

%description -l pl
Demon systemu plik�w urz�dze�.

%prep
%setup  -q -n devfsd

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -I."

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}}

install devfsd		$RPM_BUILD_ROOT%{_sbindir}
install devfsd.8	$RPM_BUILD_ROOT%{_mandir}/man8
install modules.devfs	$RPM_BUILD_ROOT%{_sysconfdir}/modules.devfs
install %{SOURCE1} 	$RPM_BUILD_ROOT%{_sysconfdir}/devfsd.conf

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/devfsd.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/modules.devfs
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.gz
