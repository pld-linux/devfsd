Summary:	DevFS Daemon
Summary(pl):	Demon DevFS
Name:		devfsd
Version:	1.3.18
Release:	3
License:	GPL
Source0:	ftp://ftp.atnf.csiro.au/pub/people/rgooch/linux/daemons/devfsd/%{name}-v%{version}.tar.gz
Source1:	%{name}.conf
URL:		http://www.atnf.csiro.au/~rgooch/linux/
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
Devfsd jest demonem startowanym ze skryptów startowych systemu, który
daje mo¿liwo¶æ inteligentnego zarz±dzania wpisami w Device Filesystem
(devfs). Jako czê¶æ fazy ustawieñ devfsd tworzy linki symboliczne,
które s± wkompilowane w kod. Te linki s± wymagane zgodnie z
/usr/src/linux/Documentation/devices.txt. To zachowanie mo¿e siê
zmieniæ w przysz³o¶ci.

devfsd czyta specjalny plik kontrolny .devfsd w zamontowanym katalogu
devfs i czeka na na tworzenie i usuwanie wpisów urz±dzeñ (nazywa siê
to operacj± zmiany). Dla ka¿dej zmiany devfsd mo¿e podj±æ wiele
dzia³añ. Demon normalnie uruchamia sam siebie i wysy³a komunikat do
syslog'a.

Otwarcie syslog'a jest normalnie automatycznie opó¼nione do czasu, gdy
/dev/log nie zostanie utworzony.

Demon systemu plików urz±dzeñ. Pozwala na u¿ywanie "tradycyjnych" nazw
urz±dzeñ.

%prep
%setup  -q -n devfsd

%build
%{__make} CEXTRAS="%{rpmcflags} -I."

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/{man8,man5},%{_sysconfdir}}

install devfsd		$RPM_BUILD_ROOT%{_sbindir}
install devfsd.8	$RPM_BUILD_ROOT%{_mandir}/man8
install devfsd.conf.5	$RPM_BUILD_ROOT%{_mandir}/man5
install modules.devfs	$RPM_BUILD_ROOT%{_sysconfdir}/modules.devfs
install %{SOURCE1} 	$RPM_BUILD_ROOT%{_sysconfdir}/devfsd.conf

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/devfsd.conf
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/modules.devfs
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*.gz
