Summary:	DevFS Daemon
Summary(pl):	Deamon DevFS
Name:		devfsd
Version:	1.3.16
Release:	2
License:	GPL
Source0:	ftp://ftp.atnf.csiro.au/pub/people/rgooch/linux/daemons/devfsd/%{name}-v%{version}.tar.gz
Source1:	%{name}.conf
Group:		Base
Group(de):	Gründsätzlich
Group(es):	Base
Group(pl):	Podstawowe
Group(pt_BR):	Base
Conflicts:	kernel =< 2.2
Requires:	devfs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
The devfsd programme is a daemon, run by the system boot scripts which
can provide for intelligent management of device entries in the Device
Filesystem (devfs).

As part of its setup phase devfsd creates certain symbolic links which
are compiled into the code. These links are required by
/usr/src/linux/Documentation/devices.txt. This behaviour may change in
future revisions.

devfsd will read the special control file .devfsd in a mounted devfs,
listening for the creation and removal of device entries (this is
termed a change operation). For each change operation, devfsd can take
many actions. The daemon will normally run itself in the background
and send messages to syslog.

The opening of the syslog service is automatically delayed until
/dev/log is created.

At startup, before switching to daemon mode, devfsd will scan the
mounted device tree and will generate synthetic REGISTER events for
each leaf node.

%description -l pl
Demon systemu plików urz±dzeñ. Pozwala na u¿ywanie "tradycyjnych" nazw
urz±dzeñ.

%prep
%setup  -q -n devfsd

%build
%{__make} CFLAGS="%{rpmcflags} -I."

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/{man8,man5},%{_sysconfdir}}

install devfsd		$RPM_BUILD_ROOT%{_sbindir}
install devfsd.8	$RPM_BUILD_ROOT%{_mandir}/man8
install devfsd.conf.5	$RPM_BUILD_ROOT%{_mandir}/man5
install modules.devfs	$RPM_BUILD_ROOT%{_sysconfdir}/modules.devfs
install %{SOURCE1} 	$RPM_BUILD_ROOT%{_sysconfdir}/devfsd.conf

%post
killall -HUP devfsd || :

%postun
[ "$1" = "0" ] && killall -TERM devfsd || :

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/devfsd.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/modules.devfs
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*.gz
