Name: meego-menus
Summary: Configuration and data files for the desktop menus
Version: 0.2.0
Release: %mkrel 1
Group: System/Desktop
License: GPLv2
URL: https://www.meego.com
Source0: %{name}-%{version}.tar.gz
BuildRequires: intltool
BuildRequires: gettext
Obsoletes: moblin-menus < 0.2.0

%description
Configuration and data files for MeeGo desktop menus

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang meego-menus

%files -f meego-menus.lang
%defattr(-,root,root,-)
%{_sysconfdir}/xdg/menus/*-merged
%{_sysconfdir}/xdg/menus/*.menu
%{_datadir}/desktop-directories/*.directory
