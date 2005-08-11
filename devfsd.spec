%bcond_without	kernel25
Summary:	DevFS Daemon
Summary(pl):	Demon DevFS
Name:		devfsd
Version:	1.3.25
Release:	6
License:	GPL
Group:		Base
Source0:	ftp://ftp.atnf.csiro.au/pub/people/rgooch/linux/daemons/devfsd/%{name}-v%{version}.tar.gz
# Source0-md5:	44c6394b8e2e8feaf453aeddc8a3ee69
Source1:	%{name}.conf
Patch0:		%{name}-lirc.patch
Patch1:		%{name}-optflags.patch
Patch2:		%{name}-kernel2.5.patch
Patch3:		%{name}-drzewo.patch
Patch4:		%{name}-include.patch
URL:		http://www.atnf.csiro.au/~rgooch/linux/
Conflicts:	kernel =< 2.2
Requires:	devfs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define 	_sbindir	/sbin

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
%patch0 -p1
%patch1 -p1
%if %{with kernel25}
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CEXTRAS="%{rpmcflags} -I." \
	nsl_libs=`echo /%{_lib}/libnsl.so.*` \
	LIBNSL=`echo /%{_lib}/libnsl.so.*`

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
%{_mandir}/man?/*
