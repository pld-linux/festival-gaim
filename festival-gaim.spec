Summary:	Voice plugin for gaim
Summary(pl):	Wtyczka g³osowa dla gaima
Name:		festival-gaim
Version:	0.4.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://elrincondetux.d2g.com/tigrux/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gtk+-devel
Requires:	festival
Requires:	gaim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		datadir2	/usr/share
%define		_prefix		/usr/X11R6

%description
This plugin speak your incoming messages from gaim. It uses festival
and is configurable.

%description -l pl
Ta wtyczka czyta na g³os przychodz±ce wiadomo¶ci z gaima. U¿ywa
festivala i jest konfigurowalna.

%prep
%setup -q -n %{name}-%{version}

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
