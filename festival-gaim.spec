Name:		festival-gaim
Summary:	Voice plugin for gaim
Version:	0.4.2
Release:	1
Group:		Applications/Communications
License:	GPL
Source0:	http://elrincondetux.d2g.com/tigrux/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gaim festival
BuildRequires:	gtk+-devel

%define		datadir2	/usr/share
%define		_prefix		/usr/X11R6

%description
This plugin speak your incoming messages from gaim.
It uses festival and is configurable

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}-%{version}

%build
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/gaim
%{__make} FESTIVAL_VOICES_PATH=%{datadir2}/festival/lib/voices VERSION=%{version}

%install
%{__make} PLUGIN_GAIM_PATH=$RPM_BUILD_ROOT/%{_libdir}/gaim install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc INSTALL README LICENCE
%{_libdir}/gaim/festival.so
