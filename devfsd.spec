Summary:	DevFS Daemon
Name:		devfsd
Version:	1.3.6
Release:	1
Source0:	ftp://ftp.atnf.csiro.au:21/pub/people/rgooch/linux/daemons/%{name}-v%{version}.tar.gz
Source1:	devfsd.conf
Patch0:		devfsd-nsl.patch
Copyright:	GPL
Group:		Base
Group(pl):	Podstawowe
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
Device File System Daemon.

%description -l pl
Demon systemu plików urz±dzeñ.

%prep
%setup  -q -n devfsd
%patch0 -p1

%build
make LDFLAGS="-lnsl"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}}

install devfsd		$RPM_BUILD_ROOT%{_sbindir}
install devfsd.8	$RPM_BUILD_ROOT%{_mandir}/man8
install %{SOURCE1} 	$RPM_BUILD_ROOT%{_sysconfdir}/devfsd.conf

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/devfsd.conf
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.gz
