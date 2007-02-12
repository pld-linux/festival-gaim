Summary:	Voice plugin for gaim
Summary(pl.UTF-8):   Wtyczka głosowa dla gaima
Name:		festival-gaim
Version:	0.4.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://elrincondetux.d2g.com/tigrux/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	198f86d015ef65b4e8b65f1ca96a1e11
Patch0:		%{name}-tag.patch
BuildRequires:	gtk+-devel
Requires:	festival
Requires:	gaim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		datadir2	/usr/share

%description
This plugin speak your incoming messages from gaim. It uses festival
and is configurable.

%description -l pl.UTF-8
Ta wtyczka czyta na głos przychodzące wiadomości z gaima. Używa
festivala i jest konfigurowalna.

%prep
%setup -q
%patch0

%build
%{__make} FESTIVAL_VOICES_PATH=%{datadir2}/festival/lib/voices VERSION=%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gaim

%{__make} install \
	PLUGIN_GAIM_PATH=$RPM_BUILD_ROOT%{_libdir}/gaim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README LICENCE
%{_libdir}/gaim/festival.so
